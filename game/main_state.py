import random
import json
import os

from pico2d import *
import game_framework
import game_world

from mario import Boy
from grass import Grass
from ball import Ball
from gumba import Gumba
from koopas import Koopas





name = "MainState"

boy = None
grass = None
gumba = None
koopas = None



def enter():
    global boy, grass, gumba, koopas
    boy = Boy()
    grass = Grass()
    gumba = Gumba()
    koopas = Koopas()



def exit():
    global boy, grass, gumba, koopas
    del boy
    del grass
    del gumba
    del koopas

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
    boy.update()
    gumba.update()
    koopas.update()





def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    gumba.draw()
    koopas.draw()
    #delay(0.05)
    
    update_canvas()







