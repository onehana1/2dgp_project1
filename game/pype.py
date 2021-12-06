from pico2d import *
import game_world
import random


import server
import collision

import game_framework



# from powerup import Flower

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 4
FRAMES_PER_ACTION = 1



class Pype:
    font = None

    def __init__(self, count = '1', x = 0, y = 0):
        # self.x, self.y = 500, 180
        self.x, self.y = x , y

        self.image = load_image('pype.png')
        self.image2 = load_image('block.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0

        self.state = 0
        self.item = True

        self.count = count
        if Pype.font is None:
            Pype.font = load_font('ENCR10B.TTF', 16)


    def crush_box(self):
        return self.x +86 - server.boy.x, self.y, self.x +148- server.boy.x, self.y+164

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3



    def draw(self): 

        self.image.clip_draw_to_origin(0, 0, 74, 82, self.x- server.boy.x, self.y,148,164)

        Pype.font.draw(self.x - 30 - server.boy.x, self.y + 50, self.count, (255, 255, 0))

        draw_rectangle(*self.crush_box())






