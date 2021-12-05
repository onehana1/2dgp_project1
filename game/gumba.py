from pico2d import *
import game_world
import game_framework
import random

import server
import collision



# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 20
FRAMES_PER_ACTION = 1



class Gumba:
    font = None

    def __init__(self, count = '1', x = 0, y = 0):
        self.x, self.y = x , y
        self.image = load_image('gumba.png')
        global cam

        self.dir = 1
        self.velocity = 0
        self.jump_timer = 0
        self.frame = 0
        self.timer = 0

        self.state = 0

        self.count = count
        if Gumba.font is None:
            Gumba.font = load_font('ENCR10B.TTF', 16)


    def crush_box(self):
        return self.x - 20 - server.boy.x, self.y-18, self.x + 20 - server.boy.x, self.y+18

    def do(self):
        pass
    
    def update(self):

        self.velocity = 0
        self.timer += 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        if self.state == 0:
            if(self.timer%1000 == 0):
                self.dir += 1

            if ((self.dir % 2) == 1):
                self.velocity += RUN_SPEED_PPS
                self.x += self.velocity * game_framework.frame_time
            else:
                self.velocity -= RUN_SPEED_PPS
                self.x += self.velocity * game_framework.frame_time
        if self.state == 1:
            self.velocity += RUN_SPEED_PPS
            self.y -= self.velocity * game_framework.frame_time
            pass


        for gumba in server.gumbas:  

            if collision.collide_head_mon(server.boy, gumba): #밟 처치
                server.boy.y += 35
                gumba.state = 1
                server.boy.jumping_mon = True

                server.gumbas.remove(gumba)
                game_world.remove_object(gumba)
                print("1")
                server.boy.score += 500


            if collision.collide(server.boy, gumba):  #충돌
                if(server.boy.inv==False):
                    if(server.boy.state==2):server.boy.state = 1
                    elif(server.boy.state==1):server.boy.state = 0
                
                    if server.boy.state == 0:
                        server.boy.x += - server.boy.dir * 35
                        server.boy.y += 35
                        server.boy.jumping_mon = True
                        server.boy.inv = True
                        
                        print("2")




        pass

    def draw(self):
        if self.state==0:
            self.image.clip_draw( 2 + int(self.frame)*20, 2, 20, 18, self.x - server.boy.x, self.y, 40, 36)
    
        else:
            self.image.clip_draw( 2 + 2*20  , 2, 20, 18, self.x - server.boy.x, self.y, 40, 36)

        if self.state==1:
            self.image.clip_composite_draw( 44, 2, 20, 18, 3.141592/2,'', self.x- server.boy.x, self.y, 40, 36)

        Gumba.font.draw(self.x - 30 - server.boy.x, self.y + 50, self.count, (255, 255, 0))

        draw_rectangle(*self.crush_box())





