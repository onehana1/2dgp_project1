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





name = "next_stage"

next = None
font = None

def enter():
    global next
    global font

    next = load_image('next.png')
    font = load_font('supermariobros.ttf', 60)
    hide_cursor()
    hide_lattice()

def exit():
    global next
    del next
    global font
    del font

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
                game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            game_framework.change_state(main_stage_2)



def update():
    pass



def draw():
    clear_canvas()
    next.draw(get_canvas_width()//2, get_canvas_height()//2)
    font.draw(get_canvas_width()//2 - 250, get_canvas_height()//2 - 100, 'Coin : %3.0f' % server.coin, (255, 255, 0))
    font.draw(get_canvas_width()//2 - 250, get_canvas_height()//2 - 200, 'Score : %3.0f' % server.score, (255, 255, 255))

    update_canvas()






