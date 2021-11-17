from pico2d import *
import random

class Back:
    def __init__(self):
        self.image = load_image('back.png')
        self.x = random.randint(0,800)
        self.y = random.randint(100,600)


    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(4, 60,53,25,self.x,self.y)
