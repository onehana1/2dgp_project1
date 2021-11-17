from pico2d import *
import game_world
import random



import game_framework


from powerup import Mushroom

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 4
FRAMES_PER_ACTION = 1



class Box2:

    def __init__(self):
        self.x, self.y = 1100, 180

        self.image = load_image('box.png')
        self.image2 = load_image('block.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0

        self.state = 0
        self.item = True




    def crush_box(self):
        return self.x-18, self.y-18, self.x +18, self.y+17

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        pass

    def draw(self): 
        if self.state ==0:
            self.image.clip_draw(1 + 18*int(self.frame), 18, 18, 18, self.x, self.y,36,36)
        else:
            self.image2.clip_draw(2, 78, 18, 18, self.x, self.y,36,36)

        draw_rectangle(*self.crush_box())






