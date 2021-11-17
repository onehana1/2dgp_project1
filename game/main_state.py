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

from box import Box
from block import Block
from powerup import Mushroom
from powerup import Flower



from ball import Ball
from gumba import Gumba
from koopas import Koopas
from redkoopas import redKoopas






name = "MainState"



boy = None
grass = None
sky = None

stage1_ground1 = None

box = None
block = None

mushroom = None
flower = None




gumba = None
koopas = None
redkoopas = None


gumbas = []


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True




def collide_floor(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    if left_a > right_b: return False
    elif right_a < left_b: return False
    elif top_a < bottom_b: return False
    elif bottom_a > top_b: return False

    elif bottom_a <= top_b: return True #발로 밟기



def collide_head(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    
    if left_a > right_b: return False
    elif right_a < left_b: return False
    elif top_a < bottom_b: return False
    elif bottom_a > top_b: return False

    elif top_a >= bottom_b: return True #머리 박기

def collide_monster(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    
    if top_a >= bottom_b: return False

    return True






def enter():
    global boy, grass,sky, koopas, redkoopas
    global stage1_ground1
    global box, block
    global mushroom, flower

    global gumba
    global gumbas
    gumbas = [Gumba() for i in range(2)]
    game_world.add_objects(gumbas, 1)

    boy = Boy()
    grass = Grass()
    sky = Sky()

    stage1_ground1 = S1_Ground1()


    global boxs 
    boxs = [Box() for i in range(2)]
    game_world.add_objects(boxs, 1)

    box = Box()
    block = Block()

    mushroom = Mushroom()
    flower = Flower()



    gumba = Gumba()
    koopas = Koopas()
    redkoopas = redKoopas()

    game_world.add_object(sky, 0)
    # game_world.add_object(grass, 0)
    game_world.add_object(stage1_ground1, 0)

    # game_world.add_object(box, 1)
    game_world.add_object(block, 1)

    game_world.add_object(mushroom, 1)
    game_world.add_object(flower, 1)




    game_world.add_object(boy, 1)
    # game_world.add_object(gumba, 1)
    # game_world.add_object(koopas, 1)
    # game_world.add_object(redkoopas, 1)






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
    boy.cam =  boy.velocity * game_framework.frame_time 


    # box.x -= boy.cam 
    block.x -= boy.cam 
    stage1_ground1.x -= boy.cam 
    mushroom.x -= boy.cam 
    flower.x -= boy.cam 


    for gumba in gumbas:  
        gumba.x -= boy.cam

    for box in boxs:  
        box.x -= boy.cam


    
    
    



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

    cam()

    for game_object in game_world.all_objects():
        game_object.update()

    if boy.inv==True:
        boy.inv_timer += 1
        if (boy.inv_timer % 500 == 0):
            boy.inv = False
    
    for gumba in gumbas:  

        if collide_floor(boy, gumba): #밟 처치
            boy.y += 35
            gumba.state = 1
            # gumbas.remove(gumba)
            # game_world.remove_object(gumba)
            print("1")
        elif collide_monster(boy, gumba):  #충돌
            if(boy.inv==False):
                boy.state = 0
                if boy.state == 0:
                    boy.x += - boy.dir*35
                    boy.y += 35
                    boy.inv = True
                    print("2")




    if collide(boy, mushroom):
        if mushroom.state >= 1:
            # print("변신!!")
            game_world.remove_object(mushroom)
            boy.state = 1

        

    # 땅에 붙어있자..
    if collide_floor(boy, stage1_ground1):
        # print("땅에 있음")
        boy.fall = 0

    if collide_floor(mushroom, stage1_ground1):
        # print("땅에 있음")
        mushroom.fall = 0


    if collide_head(boy, box):
        # print("박스 open")
        box.state = 1
        if boy.state==0:
            boy.y = box.y -37
        if boy.state==1:
            boy.y = box.y - 90

        mushroom.state += 1 
        
        if mushroom.state == 1:
            mushroom.y += 36
        
        # box.remove(box)
        # game_world.remove_object(box)
        pass

    if collide_floor(boy, box):
        # print("박스 위에 있음")
        boy.fall = 0

    if collide_floor(mushroom, box):
        # print("박스 위에 있음")
        mushroom.fall = 0

    if collide_floor(boy, block):
        # print("블록 위에 있음")
        boy.fall = 0

    if collide_floor(mushroom, block):
        # print("블록 위에 있음")
        mushroom.fall = 0
    


    if collide_head(boy, block):
        # print("block 부심")
        # block.state = 1
        # box.remove(box)
        game_world.remove_object(block)
        pass


    # if not collide(boy, box):
    #     #print("돌아와")
    #     # game_world.remove_object(gumba)
    #     boy.stopping = False
    #     pass


        
    if not collide_floor(boy, stage1_ground1) and not collide_floor(boy, box):
        # print("fall!!")
        boy.fall = 1

    if collide_floor(mushroom, stage1_ground1)!=1 and collide_floor(mushroom, box)!=1 :
        # print("fall!!")
        mushroom.fall = 1
        






def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    #delay(0.5)
    
    update_canvas()







