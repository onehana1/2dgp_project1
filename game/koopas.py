from pico2d import *
import game_world
import random

import game_framework
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



class Koopas:
    font = None
    def __init__(self, count = '1', x = 0, y = 0):
        self.x, self.y = x,y
        self.image = load_image('Koopas_r.png')
        self.image2 = load_image('Koopas_l.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 5
        self.frame = 0

        self.count = count
        if Koopas.font is None:
            Koopas.font = load_font('ENCR10B.TTF', 16)

    def crush_box(self):
        return self.x-25 - server.boy.x, self.y-30, self.x +25 - server.boy.x, self.y+30

    def do(self):

        pass
    
    def update(self):
        
        self.velocity = 0
        self.timer -=  game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

  
        if self.timer <= 0 and self.dir == 0:
            self.dir = 1
            self.timer = 5.0
        elif self.timer <= 0 and self.dir == 1:
            self.dir = 0
            self.timer = 5.0


        if self.dir== 1:
            self.velocity = RUN_SPEED_PPS
            self.x += self.velocity * game_framework.frame_time
            
        else:
            self.velocity = RUN_SPEED_PPS
            self.x -= self.velocity * game_framework.frame_time




        for koopas in server.koopass:  



            if collision.collide_floor(server.boy, koopas): #밟 처치
                server.boy.y += 35
                koopas.state = 1
                server.boy.jumping_mon = True

                server.koopass.remove(koopas)
                game_world.remove_object(koopas)
                print("1")
                server.score += 500


            if collision.collide_side(server.boy, koopas):  #충돌
                if server.mario_star == 1:
                    server.koopass.remove(koopas)
                    game_world.remove_object(koopas)
                    print("1")
                    server.score += 500
                if server.mario_star == 0:
                    if(server.boy.inv==False):
            
                        if server.mario_state == 2 or server.mario_state ==1 or server.mario_state == 0:
                            server.boy.x +=  -server.boy.dir * 35
                            server.boy.y += 35
                            server.boy.jumping_mon = True
                            server.boy.inv = True
                            
                            print("2")

                    if(server.mario_state==2):server.mario_state = 1
                    elif(server.mario_state==1):server.mario_state = 0
                    elif(server.mario_state==0):server.mario_state = -1



            for pype in server.pypes:  
                if collision.collide_side(koopas, pype) and koopas.timer!=5:
                    if koopas.dir == 1:
                        koopas.dir = 0
                    else:
                        koopas.dir = 1
                    koopas.timer = 5
                    




    def draw(self):
        if ((self.dir % 2) == 1):
            self.image.clip_draw(55 + 31*int(self.frame), 5, 31, 24, self.x - server.boy.x, self.y,60,70)
        else:
            self.image2.clip_draw(85 - 31*int(self.frame), 5, 31, 24, self.x - server.boy.x, self.y,60,70)


        Koopas.font.draw(self.x - 30  - server.boy.x, self.y + 50, self.count, (255, 255, 0))


        draw_rectangle(*self.crush_box())

