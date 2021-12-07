from math import trunc
import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server
import world_build_state

from sky import Sky

from boss import Boss

from mario2 import Boy

from stage2_ground1 import S2_Ground1



name = "MainState2"





def enter():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    server.boss = Boss()
    game_world.add_object(server.boss, 1)

    server.sky = Sky()
    game_world.add_object(server.sky, 0)

    server.stage2_ground1 = S2_Ground1()
    game_world.add_object(server.stage2_ground1, 0)




 






def exit():
    game_world.clear()
    for game_object in game_world.all_objects():
        game_world.remove_object()
        pass

def pause():
    pass


def resume():
    pass






    



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(world_build_state)
        else:
            server.boy.handle_event(event)



def update(): 
    for game_object in game_world.all_objects():
        game_object.update()

    pass




    


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    
    update_canvas()







