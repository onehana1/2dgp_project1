from pico2d import *


class Gumba:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('gumba.png')


        self.dir = 1
        self.velocity = 0
        self.jump_timer = 0
        self.frame = 0
        self.timer = 0


    def do(self):
        pass
    
    def update(self):
        self.timer += 1
        self.frame = (self.frame + 1) % 2

        if(self.timer%1000 == 0):
            self.dir += 1

        if ((self.dir % 2) == 1):
            self.x += 0.5
        else:
            self.x -= 0.5
        

        pass

    def draw(self):
        self.image.clip_draw(2 + self.frame*20, 2, 20, 22, self.x, self.y, 46, 44)




