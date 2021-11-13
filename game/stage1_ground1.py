from pico2d import *

class S1_Ground1:
    def __init__(self):
        self.image = load_image('stage1_ground1.png')
        self.x=800
        self.y=30


    def update(self):
        pass

    def crush_box(self):
        return self.x-1102, self.y-35, self.x + 1102, self.y+33


    def draw(self):
        self.image.draw(1102, 30 ,2204,64)
        draw_rectangle(*self.crush_box())

