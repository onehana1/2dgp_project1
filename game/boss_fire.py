from pico2d import *
import game_world
import game_framework
import random
import server
import collision
# import main_state


# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 20
FRAMES_PER_ACTION = 1



class Boss_Fire:
    image = None
    def __init__(self):
        if Boss_Fire.image == None:
            Boss_Fire.image = load_image('boss_fire.png')
        
        self.x, self.y, self.dir = server.boss.x, server.boss.y + 40, server.boss.dir
        global cam

        self.velocity = 0
        self.jump_timer = 0
        self.frame = 0
        self.timer = 3

        self.state = 0
      


    def crush_box(self):
        return self.x-14 , self.y-6, self.x +15, self.y+7

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.timer -= game_framework.frame_time
        
        if(self.timer <= 0):
            self.state = 1
            self.timer = 3

        self.velocity = RUN_SPEED_PPS
        if self.dir==1:
            self.x +=  self.velocity * game_framework.frame_time
            # print(" +! : ",self.velocity)

        elif self.dir== 0:
            self.x -=  self.velocity * game_framework.frame_time
            
            print(" -! : ",self.velocity)

        if self.y < 50 :
            game_world.remove_object(self)


        if collision.collide(self, server.boy):
            if server.boy.inv == False:
                server.mario_state -= 1
                server.boy.x +=  -server.boy.dir * 35
                server.boy.y += 35
            server.boy.inv = True
            
            game_world.remove_object(self)
            print("보스 어택")







    def draw(self):
        if self.state==0:
            self.image.clip_draw( 1 + int(self.frame)*1, 3, 31, 13, self.x, self.y, 62, 26)
        if self.state==1:
            game_world.remove_object(self)
        





        draw_rectangle(*self.crush_box())
