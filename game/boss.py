from os import terminal_size
from pico2d import *
import game_world
import game_framework
import random

import server
import collision

from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode



# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


Fall_SPEED_KMPH = 30.0 # Km / Hour
Fall_SPEED_MPM = (Fall_SPEED_KMPH * 1000.0 / 60.0)
Fall_SPEED_MPS = (Fall_SPEED_MPM / 60.0)
Fall_SPEED_PPS = (Fall_SPEED_MPS * PIXEL_PER_METER)

JUMP_SPEED_KMPH = 30.0 # Km / Hour
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

# monster Action Speed
TIME_PER_ACTION = 4
ACTION_PER_TIME = 20
FRAMES_PER_ACTION = 1



class Boss:
    font = None

    def __init__(self):
        self.x, self.y = 1000 , 300
        self.image = load_image('boss_l.png')
        self.image2 = load_image('boss_r.png')

        self.image3 = load_image('boss_l_r.png')
        self.image4 = load_image('boss_r_r.png')


        self.w = 41
        self.h = 36

        self.dir = 1
        self.velocity = 0
        self.jumping= 0
        self.frame = 0
        self.timer = 2
        self.jump_timer = 5
        self.jumping_timer = 0

        self.jump_v = 0

        self.fall = 1

        self.inv = False
        self.inv_timer = 2



        self.state = 0
        self.life = 5


        self.life_test = 0


        self.build_behavior_tree()


    def wander(self):


        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        self.jump_timer -= game_framework.frame_time

        if self.jump_timer <= 0 :
            self.jumping = 1
            self.jump_timer = 5.0

  
        if self.timer <= 0 and self.dir == 0:
            self.dir = 1
            self.timer = 2.0

        elif self.timer <= 0 and self.dir == 1:
            self.dir = 0
            self.timer = 2.0

            return BehaviorTree.SUCCESS
                
        else:
            return BehaviorTree.RUNNING

    def find_player(self):

        self.jump_timer -= game_framework.frame_time
        distance = (server.boy.x - self.x)**2 + (server.boy.y - self.y)**2
        if distance < (PIXEL_PER_METER * 20)**2:

            if self.jump_timer <= 0 :
                self.jumping = 1
                self.jump_timer = 5.0


            if server.boy.x > self.x:
                self.dir = 1
            else: self. dir = 0

            

            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
   
    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.jump_v = JUMP_SPEED_PPS
        return BehaviorTree.SUCCESS


    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_chase_node)



    def crush_box(self):
        return self.x, self.y, self.x + self.w * 2, self.y + self.h * 2

    def do(self):
        pass

    def jump(self):
        self.jump_v = JUMP_SPEED_PPS
        self.jump_v -= game_framework.frame_time * self.jumping_timer * JUMP_SPEED_PPS


        if (self.jumping == True and self.fall == 0):
            self.jumping_timer += 1 * game_framework.frame_time
            self.y += self.jump_v * game_framework.frame_time


        if (self.jumping_timer > 0.7 or self.fall == 1):   
            self.jumping_timer = 0
            self.jump_v = 0

            self.fall = 1
            
        if(self.fall == 1 and self.jumping == True):
            self.jumping = False

        if self.jumping == False:
            self.fall = True



    def drop(self):
        if(self.fall == 1 and self.jumping == False):

            self.y -= Fall_SPEED_PPS * game_framework.frame_time

    
    def update(self): 
        self.velocity = 0
        self.fall = 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        self.frame2 = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if self.inv ==True:
            self.inv_timer -= game_framework.frame_time

        if self.inv_timer <= 0:
            self.inv = False
            self.inv_timer = 2

        # self.jump()
        self.drop()


        self.bt.run()


        if self.dir== 1:
            self.velocity = RUN_SPEED_PPS
            self.x += self.velocity * game_framework.frame_time
            
        else:
            self.velocity = RUN_SPEED_PPS
            self.x -= self.velocity * game_framework.frame_time


        if self.jumping == 1:
            # print("뛸게")
            self.velocity = JUMP_SPEED_PPS
            self.y += self.velocity * game_framework.frame_time
            pass

        if self.jumping == 1 and self.y >= 300:
            self.jumping = 0 
            self.fall = 1
            # print("그만뛸게")


      
        if collision.collide_floor(self, server.stage2_ground1): 
            self.fall = 0
            # print(self.fall)


        if collision.collide_floor(server.boy, self): #밟 처치
            server.boy.y += 70
            
            server.boy.x +=  -server.boy.dir * 70

            server.boy.jumping_mon = True

            if self.inv ==False:
                self.life -= 1

            if (self.inv == True) and server.boy.inv == False:
                print("??")
                if (self.inv == True):
                    self.life_test += 1
                    print("테스트 라이프",self.life_test)

                    server.boy.inv = True
                    server.boy.x +=  -server.boy.dir * 70
                    server.boy.y += 70
                    if(server.mario_state==2):server.mario_state = 1
                    elif(server.mario_state==1):server.mario_state = 0

            self.inv = True
            #print(self.life)
            


            if self.life == 0 :
                game_world.remove_object(self)
                print("보스 처치")

                server.score += 5000

          
        # #화날때 밟으면 아파용
        # if collision.collide_floor(server.boy, self):
        #     if (self.inv == True):
        #         self.life_test += 1
        #         print("테스트 라이프",self.life_test)

        #         server.boy.inv = True
        #         server.boy.x +=  -server.boy.dir * 70
        #         server.boy.y += 35
        #         if(server.mario_state==2):server.mario_state = 1
        #         elif(server.mario_state==1):server.mario_state = 0



        if collision.collide_side(server.boy, self):  #충돌
                if(server.boy.inv==False):
        
                    if server.mario_state == 2 or server.mario_state ==1 or server.mario_state == 0:
                        server.boy.x +=  -server.boy.dir * 70
                        server.boy.y += 35
                        server.boy.jumping_mon = True
                        server.boy.inv = True
                        
                        print("2")

                if(server.mario_state==2):server.mario_state = 1
                elif(server.mario_state==1):server.mario_state = 0


        self.x = clamp(60, self.x, 1550)
        self.y = clamp(60, self.y, 500)




        pass

    def draw(self):
        # print(int(self.frame))
        if self.dir==0:
            if self.inv == False:
                self.image.clip_draw_to_origin(self.w * int(self.frame), 0, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)
            else:
                self.image3.clip_draw_to_origin(self.w * int(self.frame), 0, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)

 
    
        if self.dir==1:
            if self.inv == False:
                self.image2.clip_draw_to_origin(self.w*int(self.frame), 0, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)
            else:
                self.image4.clip_draw_to_origin(self.w*int(self.frame), 0, self.w, self.h, self.x, self.y, self.w * 2, self.h * 2)


        if self.state==1:
            self.image.clip_composite_draw( 44, 2, 20, 18, 3.141592/2,'', self.x, self.y, 40, 36)

        # Boss.font.draw(self.x - 30 - server.boy.x, self.y + 50, (255, 255, 0))

        draw_rectangle(*self.crush_box())





