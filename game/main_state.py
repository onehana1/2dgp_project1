from math import trunc
import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server
import world_build_state


from mario import Boy
from fire import Fire

from grass import Grass
from sky import Sky
from back import Back

from pype import Pype



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



from background import FixedBackground as Background


name = "MainState"





def enter():

    # server.gumbas = [Gumba('1',100,50) for i in range(2)]
    # game_world.add_objects(server.gumbas, 1)

    # server.gumbas = [Gumba('1',100,50), Gumba('2',200,150), Gumba('3',300,150)]
    # game_world.add_objects(server.gumbas, 1)

######################굼바###########################
    with open('gumba_data.json', 'r') as f:
        monster_data_list = json.load(f)

    for data in monster_data_list:
        server.df_g = Gumba(data['g_name'], data['g_x'], data['g_y'])
        server.gumbas.append(server.df_g)
        
    game_world.add_objects(server.gumbas, 1)

######################거북###########################
    with open('koopa_data.json', 'r') as f:
        monster_data_list = json.load(f)

    for data in monster_data_list:
        server.df_k = Koopas(data['k_name'], data['k_x'], data['k_y'])
        server.koopass.append(server.df_k)
    
    game_world.add_objects(server.koopass, 1)

#==========빨거북==========#
    with open('redkoopa_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_k = redKoopas(data['k_name'], data['k_x'], data['k_y'])
        server.redkoopass.append(server.df_k)

    game_world.add_objects(server.redkoopass, 1)

#==========파이프==========#
    with open('pype_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_p = Pype(data['g_name'], data['g_x'], data['g_y'])
        server.pypes.append(server.df_p)

    game_world.add_objects(server.pypes, 1)

#==========박스==========#
    with open('box_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_b = Box(data['k_name'], data['k_x'], data['k_y'])
        server.boxs.append(server.df_b)

    game_world.add_objects(server.boxs, 1)

#######################템m##########################
    with open('box_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_m = Mushroom(data['k_name'], data['k_x'], data['k_y'])
        server.mushrooms.append(server.df_m)

    game_world.add_objects(server.mushrooms, 1)

    # server.mushrooms = Mushroom('1',100,50)
    # game_world.add_object(server.mushroom, 1)
#######################템f##########################
    with open('box_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_f = Mushroom(data['k_name'], data['k_x'], data['k_y'])
        server.flowers.append(server.df_f)

    # game_world.add_objects(server.flower, 1)

        
    #server.flower = Flower('1',100,50)
    #game_world.add_object(server.flower, 1)

    server.coin = Coin('1',100,50)
    game_world.add_object(server.coin, 1)


    server.boy = Boy()
    game_world.add_object(server.boy, 1)

 
    # server.sky = Sky()
    # game_world.add_object(server.sky, 0)

    server.background = Background()
    game_world.add_object(server.background, 0)



    server.stage1_ground1 = S1_Ground1()
    game_world.add_object(server.stage1_ground1, 1)



 

    server.stage1_ground2 = S1_Ground2()
    game_world.add_object(server.stage1_ground2, 1)









    server.boxs2 = [Box2() for i in range(1)]
    game_world.add_objects(server.boxs2, 1)


    server.block = Block()
    game_world.add_object(server.block, 1)







    # for server.box in server.boxs:  
    #     server.mushroom.x = server.box.x

    # for server.box2 in server.boxs2:  
    #     server.flower.x = server.box2.x









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
            server.boy.handle_event(event)



def update():

    # server.coin.x = server.block.x
    # server.coin.y = server.block.y

  

    for game_object in game_world.all_objects():
        game_object.update()




    


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    #delay(0.5)

    
    update_canvas()







