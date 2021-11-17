from pico2d import *




class S1_Ground2:
    def __init__(self):
        self.image = load_image('stage1_ground2.png')
        self.x= 2650
        self.y=60



    def update(self):        

    
       pass

    def crush_box(self):
        return self.x-400, self.y-30, self.x + 400, self.y+30


    def draw(self):
        self.image.draw(self.x, self.y ,800,60)
        self.image.draw(self.x , self.y ,800,60)



        draw_rectangle(*self.crush_box())

