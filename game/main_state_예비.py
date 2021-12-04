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
    #if bottom_a > top_b: return False


    return True

def collide_head_mon(a,b):
    left_a, bottom_a, right_a, top_a = a.crush_box()
    left_b, bottom_b, right_b, top_b = b.crush_box()

    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    if bottom_a <= top_b: 
        if top_a > top_b:
            return False

        return True







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

            

    if server.boy.inv==True:
        server.boy.inv_timer += 1
        if (server.boy.inv_timer % 500 == 0):
            server.boy.inv = False
    
    for gumba in server.gumbas:  

        # if collide_floor(boy, gumba): #밟 처치
        #     boy.y += 35
        #     gumba.state = 1
        #     # gumbas.remove(gumba)
        #     # game_world.remove_object(gumba)
        #     print("1")
        #     boy.score += 500


        if collide(server.boy, gumba):  #충돌
            if(server.boy.inv==False):
                if(server.boy.state==2):server.boy.state = 1
                elif(server.boy.state==1):server.boy.state = 0
               
                if server.boy.state == 0:
                    server.boy.x += - server.boy.dir*35
                    server.boy.y += 35
                    server.boy.inv = True
                    
                    print("2")


    for server.koopas in server.koopass:  
        if collide_floor(server.boy, server.koopas): #밟 처치
            server.boy.y += 35
            server.koopas.state = 1
            server.koopass.remove(server.koopas)
            game_world.remove_object(server.koopas)
            print("1")
            server.boy.score += 500


        elif collide_monster(server.boy, server.koopas):  #충돌
            if(server.boy.inv==False):
                server.boy.state = 0
                if server.boy.state == 0:
                    server.boy.x += - server.boy.dir*35
                    server.boy.y += 35
                    server.boy.inv = True
                    
                    print("2")


    for server.redkoopas in server.redkoopass:  

        if collide_floor(server.boy, server.redkoopas): #밟 처치
            server.boy.y += 35
            server.redkoopas.state = 1
            server.redkoopass.remove(server.redkoopas)
            game_world.remove_object(server.redkoopas)
            print("1")
            server.boy.score += 500


        elif collide_monster(server.boy, server.redkoopas):  #충돌
            if(server.boy.inv==False):
                server.boy.state = 0
                if server.boy.state == 0:
                    server.boy.x += - server.boy.dir*35
                    server.boy.y += 35
                    server.boy.inv = True
                    
                    print("2")

    




    if collide(server.boy, server.mushroom):
        if server.mushroom.state == 1:
            # print("변신!!")
            game_world.remove_object(server.mushroom)
            
            server.boy.state = 1
            # boy.score += 100

    # for gumba in gumbas: 
    #     if collide(boy, gumba):
    #         gumba.state=1


    
    if collide(server.boy, server.flower):
        if server.flower.state == 1:
            print("변신!!")
            game_world.remove_object(server.flower)
            server.boy.state = 2
            # boy.score += 1000



    # 땅에 붙어있자..
    if collide_floor(server.boy, server.stage1_ground1):
        # print("땅에 있음")
        server.boy.fall = 0

    if collide_floor(server.boy, server.stage1_ground2):
        # print("땅에 있음")
        server.boy.fall = 0

    if collide_floor(server.mushroom, server.stage1_ground1):
        # print("땅에 있음")
        server.mushroom.fall = 0

    if collide_floor(server.mushroom, server.stage1_ground2):
        # print("땅에 있음")
        server.mushroom.fall = 0

    if collide_floor(server.flower, server.stage1_ground1):
        # print("땅에 있음")
        server.flower.fall = 0

    for server.box in server.boxs:  
        if collide_head(server.boy, server.box):
            # print("박스 open")
            server.box.state = 1
            if server.boy.state==0:
                server.boy.y = server.box.y -37
  
            if server.boy.state==1:
                server.boy.y = server.box.y - 90

            server.mushroom.state += 1 
            
            if server.mushroom.state == 1:
                server.mushroom.y += 36
            
            # box.remove(box)
            # game_world.remove_object(box)

        if collide_floor(server.mushroom, server.box):
            # print("박스 위에 있음")
            server.mushroom.fall = 0
        

    for server.box2 in server.boxs2:  
        if collide_head(server.boy, server.box2):
            # print("박스 open")
            server.box2.state = 1
            if server.boy.state==0:
                server.boy.y = server.box2.y -37
            if server.boy.state==1:
                server.boy.y = server.box2.y - 90

            server.flower.state += 1 
            
            # if flower.state == 1:
            #     flower.y += 36
            
            # box.remove(box)
            # game_world.remove_object(box)
        if collide_floor(server.boy, server.box2):
            # print("박스 위에 있음")
            server.boy.fall = 0




    



    


    if collide_floor(server.boy, server.block):
        # print("블록 위에 있음")
        server.boy.fall = 0

    if collide_floor(server.mushroom, server.block):
        # print("블록 위에 있음")
       
        server.mushroom.fall = 0
    


    if collide_head(server.boy, server.block):
        # print("block 부심")
        # block.state = 1
        # box.remove(box)
        game_world.remove_object(server.block)
        

        server.coin.y = server.block.y + 30
        server.coin.state += 1
        server.boy.coin =1
        game_world.remove_object(server.coin)
        pass
    




    # if not collide(boy, box):
    #     #print("돌아와")
    #     # game_world.remove_object(gumba)
    #     boy.stopping = False
    #     pass


        
    if not collide_floor(server.boy, server.stage1_ground1)and not collide_floor(server.boy, server.stage1_ground2) and not collide_floor(server.boy, server.box):
        # print("fall!!")
        server.boy.fall = 1

    if collide_floor(server.mushroom, server.stage1_ground1)!=1 and collide_floor(server.mushroom, server.stage1_ground2)!=1 and collide_floor(server.mushroom, server.box)!=1 :
        # print("fall!!")
        server.mushroom.fall = 1

    
        
    


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    #delay(0.5)

    
    update_canvas()







