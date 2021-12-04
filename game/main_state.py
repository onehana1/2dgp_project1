from math import trunc
import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server


from mario import Boy
from fire import Fire

from grass import Grass
from sky import Sky
from back import Back


from stage1_ground1 import S1_Ground1
from stage1_ground2 import S1_Ground2


from box import Box
from box2 import Box2


from block import Block


from powerup import Mushroom
from powerup import Flower
from powerup import Coin



from ball import Ball
from gumba import Gumba
from koopas import Koopas
from redkoopas import redKoopas






name = "MainState"





def enter():

    server.gumbas = [Gumba() for i in range(2)]
    game_world.add_objects(server.gumbas, 1)

    server.boy = Boy()
    game_world.add_object(server.boy, 1)

 
    server.sky = Sky()
    game_world.add_object(server.sky, 0)



    server.stage1_ground1 = S1_Ground1()
    game_world.add_object(server.stage1_ground1, 0)



 

    server.stage1_ground2 = S1_Ground2()
    game_world.add_object(server.stage1_ground2, 0)








    server.boxs = [Box() for i in range(1)]
    game_world.add_objects(server.boxs, 1)


    server.boxs2 = [Box2() for i in range(1)]
    game_world.add_objects(server.boxs2, 1)


    server.block = Block()
    game_world.add_object(server.block, 1)


    server.mushroom = Mushroom()
    game_world.add_object(server.mushroom, 1)

    server.flower = Flower()
    game_world.add_object(server.flower, 1)

    server.coin = Coin()
    game_world.add_object(server.coin, 1)




    for server.box in server.boxs:  
        server.mushroom.x = server.box.x

    for server.box2 in server.boxs2:  
        server.flower.x = server.box2.x


    server.koopass = [Koopas() for i in range(1)]
    game_world.add_objects(server.koopass, 1)


    server.redkoopass = [redKoopas() for i in range(1)]
    game_world.add_objects(server.redkoopass, 1)







def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass

def cam():
    # if boy.x < 700:
    #     boy.cam = 0
                
    # if boy.x > 800:
    server.boy.cam =  server.boy.velocity * game_framework.frame_time 


    # box.x -= boy.cam 
    server.block.x -= server.boy.cam 
    
    server.stage1_ground1.x -= server.boy.cam 
    server.stage1_ground2.x -= server.boy.cam 

    server.mushroom.x -= server.boy.cam 
    server.flower.x -= server.boy.cam 
    server.coin.x -= server.boy.cam 
    for koopas in server.koopass: 
        koopas.x -= server.boy.cam 
    for redkoopas in server.redkoopass: 
        redkoopas.x -= server.boy.cam 





    for gumba in server.gumbas:  
        gumba.x -= server.boy.cam

    for box in server.boxs:  
        box.x -= server.boy.cam

    for box2 in server.boxs2:  
        box2.x -= server.boy.cam


    
    
    



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.boy.handle_event(event)



def update():

    server.coin.x = server.block.x
    server.coin.y = server.block.y

    cam()

    for game_object in game_world.all_objects():
        game_object.update()




    


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    #delay(0.5)

    
    update_canvas()







