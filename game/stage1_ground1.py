from pico2d import *




class S1_Ground1:
    def __init__(self):
        self.image = load_image('stage1_ground1.png')
        self.x=1103
        self.y=30



    def update(self):        


    
        pass

    def crush_box(self):
        return self.x-1103, self.y-30, self.x + 1103, self.y+30


    def draw(self):
        self.image.draw(self.x, self.y ,2206,60)


        draw_rectangle(*self.crush_box())

