from pico2d import *
import game_world
import random

class redKoopas:

    def __init__(self):
        self.x, self.y = 400, 90
        self.image = load_image('redKoopas_r.png')
        self.image2 = load_image('redKoopas_l.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0


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


        self.frame = (self.frame + 1) % 2


        pass

    def draw(self):
        if ((self.dir % 2) == 1):
            self.image.clip_draw(55 + 31*self.frame, 5, 31, 24, self.x, self.y,60,70)
        else:
            self.image2.clip_draw(85 - 31*self.frame, 5, 31, 24, self.x, self.y,60,70)

        draw_rectangle(*self.crush_box())


