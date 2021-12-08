from pico2d import *
import game_world
import random

import server
import collision

import game_framework



# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 4
FRAMES_PER_ACTION = 1



class Box3:
    font = None

    def __init__(self, count = '1', x = 0, y = 0):
        self.x, self.y = x , y

        self.image = load_image('box.png')
        self.image2 = load_image('block.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0

        self.state = 0
        self.item = True

        self.count = count
        if Box3.font is None:
            Box3.font = load_font('ENCR10B.TTF', 16)




    def crush_box(self):
        return self.x-18- server.boy.x, self.y-18, self.x +18- server.boy.x, self.y+17

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        for box3 in server.boxs3:  

            if collision.collide_head(server.boy, box3):
                print("박스 open")
                if box3.state != 1:
                    server.boy.stomb_sound.play() 
                box3.state = 1
                
                server.boy.fall = 1
        


        pass

    def draw(self): 
        if self.state == 0:
            self.image.clip_draw(1 + 18*int(self.frame), 18, 18, 18, self.x- server.boy.x, self.y,36,36)
        else:
            self.image2.clip_draw(2, 78, 18, 18, self.x- server.boy.x, self.y,36,36)

        # Box3.font.draw(self.x - 30 - server.boy.x, self.y + 50, self.count, (255, 255, 0))

        # draw_rectangle(*self.crush_box())






