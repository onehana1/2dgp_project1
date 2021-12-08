from math import trunc
import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server
import world_build_state
import next_stage
import die_state
import gameover_state




from mario import Boy
from fire import Fire

from grass import Grass
from sky import Sky
from back import Back

from pype import Pype



from stage1_ground1 import S1_Ground1
from stage1_ground2 import S1_Ground2
from stage1_ground3 import S1_Ground3
from door import Door




from box import Box
from box2 import Box2
from box3 import Box3



from block import Block


from powerup import Mushroom
from powerup import Flower
from powerup import Coin
from powerup import Star




from ball import Ball
from gumba import Gumba
from koopas import Koopas
from redkoopas import redKoopas



from background import FixedBackground as Background


name = "MainState"





def enter():
    for koopas in server.koopass:  
        server.koopass.remove(koopas)
        game_world.remove_object(koopas)

    for a in server.redkoopass:  
        server.redkoopass.remove(a)
        game_world.remove_object(a)

    for a in server.gumbas:  
        server.gumbas.remove(a)
        game_world.remove_object(a)

    for a in server.boxs:  
        server.boxs.remove(a)
        game_world.remove_object(a)

    for a in server.boxs2:  
        server.boxs2.remove(a)
        game_world.remove_object(a)

    for a in server.boxs3:  
        server.boxs3.remove(a)
        game_world.remove_object(a)


    for a in server.blocks:  
        server.blocks.remove(a)
        game_world.remove_object(a)

    for a in server.mushrooms:  
        server.mushrooms.remove(a)
        game_world.remove_object(a)

    for a in server.flowers:  
        server.flowers.remove(a)
        game_world.remove_object(a)

    for a in server.coins:  
        server.coins.remove(a)
        game_world.remove_object(a)

        
    for a in server.stars:  
        server.stars.remove(a)
        game_world.remove_object(a)

        
    for a in server.fires:  
        server.fires.remove(a)
        game_world.remove_object(a)

                
    for a in server.pypes:  
        server.pypes.remove(a)
        game_world.remove_object(a)
    

    game_world.remove_object(server.block)
    game_world.remove_object(server.box)
    game_world.remove_object(server.box2)
    game_world.remove_object(server.box3)

    game_world.remove_object(server.pype)
    game_world.remove_object(server.boy)
    game_world.remove_object(server.background)
    game_world.remove_object(server.door)
    game_world.remove_object(server.stage1_ground1)
    game_world.remove_object(server.stage1_ground4)
    game_world.remove_object(server.stage1_ground2)
    game_world.remove_object(server.stage1_ground3)
    
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

    for data in monster_data_list:
        server.df_g = []

######################거북###########################
    with open('koopa_data.json', 'r') as f:
        monster_data_list = json.load(f)

    for data in monster_data_list:
        server.df_k = Koopas(data['k_name'], data['k_x'], data['k_y'])
        server.koopass.append(server.df_k)
    
    game_world.add_objects(server.koopass, 1)

    for data in monster_data_list:
        server.df_k = []

#==========빨거북==========#
    with open('redkoopa_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_k = redKoopas(data['k_name'], data['k_x'], data['k_y'])
        server.redkoopass.append(server.df_k)

    game_world.add_objects(server.redkoopass, 1)

    for data in monster_data_list:
        server.df_k = []

#==========파이프==========#
    with open('pype_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_p = Pype(data['g_name'], data['g_x'], data['g_y'])
        server.pypes.append(server.df_p)

    game_world.add_objects(server.pypes, 1)
    for data in monster_data_list:
        server.df_p = []

#==========박스==========#
    with open('box_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_b = Box(data['k_name'], data['k_x'], data['k_y'])
        server.boxs.append(server.df_b)

    game_world.add_objects(server.boxs, 1)

    for data in monster_data_list:
        server.df_b = []

#==========박스2==========#
    with open('box2_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_b2 = Box2(data['k_name'], data['k_x'], data['k_y'])
        server.boxs2.append(server.df_b2)

    game_world.add_objects(server.boxs2, 1)

    for data in monster_data_list:
        server.df_b2 = []

#==========박스3==========#
    with open('box3_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_b3 = Box3(data['k_name'], data['k_x'], data['k_y'])
        server.boxs3.append(server.df_b3)

    game_world.add_objects(server.boxs3, 1)

    for data in monster_data_list:
        server.df_b3 = []

#==========블록==========#
    with open('block_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_block = Block(data['k_name'], data['k_x'], data['k_y'])
        server.blocks.append(server.df_block)

    game_world.add_objects(server.blocks, 1)

    for data in monster_data_list:
        server.df_block = []
    

#######################템m##########################
    with open('box_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_m = Mushroom(data['k_name'], data['k_x'], data['k_y'])
        server.mushrooms.append(server.df_m)

    game_world.add_objects(server.mushrooms, 1)

    for data in monster_data_list:
        server.df_m = []

    # server.mushrooms = Mushroom('1',100,50)
    # game_world.add_object(server.mushroom, 1)
#==========템f==========#
    with open('box2_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_f = Flower(data['k_name'], data['k_x'], data['k_y'])
        server.flowers.append(server.df_f)

    game_world.add_objects(server.flowers, 1)

    for data in monster_data_list:
        server.df_f = []

#==========템s==========#
    with open('box3_data.json', 'r') as f:
        monster_data_list = json.load(f)
        
    for data in monster_data_list:
        server.df_s = Star(data['k_name'], data['k_x'], data['k_y'])
        server.stars.append(server.df_s)

    game_world.add_objects(server.stars, 1)

    for data in monster_data_list:
        server.df_s = []



    server.boy = Boy()
    game_world.add_object(server.boy, 1)

 
    # server.sky = Sky()
    # game_world.add_object(server.sky, 0)

    server.background = Background()
    game_world.add_object(server.background, 0)


    server.door = Door(5950,36) 
    game_world.add_object(server.door, 1)


    server.stage1_ground1 = S1_Ground1()
    game_world.add_object(server.stage1_ground1, 1)

    server.stage1_ground2 = S1_Ground2(2406,0)
    game_world.add_object(server.stage1_ground2, 1)


    server.stage1_ground3 = S1_Ground3(2800,0)
    game_world.add_object(server.stage1_ground3, 1)

    
    server.stage1_ground4 = S1_Ground3(5042,0)
    game_world.add_object(server.stage1_ground4, 1)







def exit():

    for koopas in server.koopass:  
        server.koopass.remove(koopas)
        game_world.remove_object(koopas)

    for a in server.redkoopass:  
        server.redkoopass.remove(a)
        game_world.remove_object(a)

    for a in server.gumbas:  
        server.gumbas.remove(a)
        game_world.remove_object(a)

    for a in server.boxs:  
        server.boxs.remove(a)
        game_world.remove_object(a)

    for a in server.boxs2:  
        server.boxs2.remove(a)
        game_world.remove_object(a)

    for a in server.boxs3:  
        server.boxs3.remove(a)
        game_world.remove_object(a)


    for a in server.blocks:  
        server.blocks.remove(a)
        game_world.remove_object(a)

    for a in server.mushrooms:  
        server.mushrooms.remove(a)
        game_world.remove_object(a)

    for a in server.flowers:  
        server.flowers.remove(a)
        game_world.remove_object(a)

    for a in server.coins:  
        server.coins.remove(a)
        game_world.remove_object(a)

        
    for a in server.stars:  
        server.stars.remove(a)
        game_world.remove_object(a)

        
    for a in server.fires:  
        server.fires.remove(a)
        game_world.remove_object(a)

                
    for a in server.pypes:  
        server.pypes.remove(a)
        game_world.remove_object(a)
    

    game_world.remove_object(server.block)
    game_world.remove_object(server.box)
    game_world.remove_object(server.box2)
    game_world.remove_object(server.box3)

    game_world.remove_object(server.pype)
    game_world.remove_object(server.boy)
    game_world.remove_object(server.background)
    game_world.remove_object(server.door)
    game_world.remove_object(server.stage1_ground1)
    game_world.remove_object(server.stage1_ground4)
    game_world.remove_object(server.stage1_ground2)
    game_world.remove_object(server.stage1_ground3)

    game_world.clear()
    print("나간다!!!")
    



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
    for game_object in game_world.all_objects():
        game_object.update()

    if server.mario_die ==True and server.mario_life > 0:
        game_framework.change_state(die_state)
        server.mario_die = False

    elif server.mario_life == 0:
        game_framework.change_state(gameover_state)

    if server.stage == 1:
        game_framework.change_state(next_stage)




    


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







