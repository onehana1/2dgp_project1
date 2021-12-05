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
        self.timer = 0
        self.frame = 0

        self.count = count
        if Koopas.font is None:
            Koopas.font = load_font('ENCR10B.TTF', 16)

    def crush_box(self):
        return self.x-25, self.y-30, self.x +25, self.y+30

    def do(self):
        pass
    
    def update(self):
        self.timer += 1

        if(self.timer%1000 == 0):
            self.dir += 1

        if ((self.dir % 2) == 1):
            self.x += 0.5
        else:
            self.x -= 0.5


        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2



        for server.koopas in server.koopass:  
            if collision.collide_floor(server.boy, server.koopas): #밟 처치
                server.boy.jumping_mon = True
                server.koopas.state = 1
                server.koopass.remove(server.koopas)
                game_world.remove_object(server.koopas)
                print("1")
                server.boy.score += 500

                
            elif collision.collide_monster(server.boy, server.koopas):  #충돌
                if(server.boy.inv==False):
                    server.boy.state = 0
                    if server.boy.state == 0:
                        server.boy.x += - server.boy.dir*35
                        server.boy.y += 35
                        server.boy.jumping_mon = True
                        server.boy.inv = True
                        
                        print("2")



        pass

    def draw(self):
        if ((self.dir % 2) == 1):
            self.image.clip_draw(55 + 31*int(self.frame), 5, 31, 24, self.x, self.y,60,70)
        else:
            self.image2.clip_draw(85 - 31*int(self.frame), 5, 31, 24, self.x, self.y,60,70)


        Koopas.font.draw(self.x - 30, self.y + 50, self.count, (255, 255, 0))


        draw_rectangle(*self.crush_box())

