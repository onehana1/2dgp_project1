import random
import json
import os

from pico2d import *
import game_framework
import game_world

from mario import Boy
from grass import Grass
from sky import Sky

from stage1_ground1 import S1_Ground1

from ball import Ball
from gumba import Gumba
from koopas import Koopas
from redkoopas import redKoopas






name = "MainState"

boy = None
grass = None
stage1_ground1 = None
sky = None

gumba = None
koopas = None
redkoopas = None


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global boy, grass,sky, gumba, koopas, redkoopas
    global stage1_ground1

    boy = Boy()
    grass = Grass()
    sky = Sky()

    stage1_ground1 = S1_Ground1()

    gumba = Gumba()
    koopas = Koopas()
    redkoopas = redKoopas()

    game_world.add_object(sky, 0)
    game_world.add_object(grass, 0)
    game_world.add_object(stage1_ground1, 0)

    

    game_world.add_object(boy, 1)
    game_world.add_object(gumba, 1)
    # game_world.add_object(koopas, 1)
    # game_world.add_object(redkoopas, 1)






def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
 

    for game_object in game_world.all_objects():
        game_object.update()
    
    if collide(boy, gumba):
        print("ccc!!")

    if collide(boy, stage1_ground1):
        boy.fall = 0
        
    if collide(boy, stage1_ground1)!=1:
        print("떨어진다!!")
        boy.fall = 1
        






def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    #delay(0.5)
    
    update_canvas()







