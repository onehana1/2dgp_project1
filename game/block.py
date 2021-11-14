from pico2d import *
import game_world

import game_framework


# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 4
FRAMES_PER_ACTION = 1



class Block:

    def __init__(self):
        self.x, self.y = 400, 180
        self.image = load_image('block.png')
        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0
        self.state = 0


    def crush_box(self):
        return self.x-18, self.y-18, self.x +18, self.y+18

    def do(self):
        pass
    
    def update(self):
        self.timer += 1

        if(self.timer%1000 == 0):
            self.dir += 1


        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        pass

    def draw(self): 
        self.image.clip_draw(2, 96, 18, 18, self.x, self.y,36,36)
        draw_rectangle(*self.crush_box())




