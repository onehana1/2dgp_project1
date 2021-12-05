import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state

import server

from mario import Boy
from gumba import Gumba


mario = None


name = "WorldBuildState"

menu = None

def enter():
    global menu
    menu = load_image('menu.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass




def create_new_world():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    # fill here
    with open('zombie_data.json', 'r') as f:
        zombie_data_list = json.load(f)

    for data in zombie_data_list:
        zombie = Gumba(data['name'], data['x'], data['y'])
        game_world.add_object(zombie, 1)



def load_saved_world():
    # fill here
    pass



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            create_new_world()
            game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_l:
            load_saved_world()
            game_framework.change_state(main_state)

def update():
    pass

def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update_canvas()






