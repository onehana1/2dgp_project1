from math import trunc
import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server



import main_state
import main_stage_2
import world_build_state





name = "clear_state"

next = None
font = None
font2 = None


def enter():
    global next
    global font
    global font2
    


    next = load_image('black.png')
    font = load_font('supermariobros.ttf', 60)
    font2 = load_font('supermariobros.ttf', 30)
    hide_cursor()
    hide_lattice()
    server.mario_life = 1
    server.mario_state = 0

def exit():
    global next
    del next
    global font
    del font
    global font2
    del font2

def pause():
    pass

def resume():
    pass




def create_new_world():
    pass

def load_saved_world():
    # fill here
    pass



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            server.stage2_ground1.bgm.stop()
            game_framework.change_state(world_build_state)
            
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            server.stage2_ground1.bgm.stop()
            game_framework.change_state(world_build_state)






def update():
    if server.stage ==0:
        server.background.bgm.stop()
    pass



def draw():
    clear_canvas()
    next.draw(get_canvas_width()//2, get_canvas_height()//2)
    font2.draw(get_canvas_width()//2 - 400, get_canvas_height()//2 + 100, 'GAME CLEAR!', (255, 255, 255))
    font2.draw(get_canvas_width()//2, get_canvas_height()//2 + 100, 'PRESS N TO MAIN', (255, 0, 0))

    font.draw(get_canvas_width()//2 - 300, get_canvas_height()//2 - 0, 'life :  %3.0f' % server.mario_life, (255, 0, 0))
    font.draw(get_canvas_width()//2 - 300, get_canvas_height()//2 - 100, 'Coin :  %3.0f' % server.coin, (255, 255, 0))
    font.draw(get_canvas_width()//2 - 300, get_canvas_height()//2 - 200, 'Score : %3.0f' % server.score, (255, 255, 255))

    update_canvas()






