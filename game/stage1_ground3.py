from pico2d import *
import server




class S1_Ground3:
    def __init__(self, x, y):
        self.image = load_image('stage1_ground3.png')
        self.x= x
        self.y= y

        self.width = 1021
        self.height = 60

    def update(self):        

    
       pass

    def crush_box(self):
        return self.x - server.boy.x, self.y-self.height, self.x + self.width * 2 - server.boy.x, self.y+self.height


    def draw(self):
        self.image.clip_draw_to_origin(0, 0 ,self.width, self.height, self.x - server.boy.x, self.y, self.width *2,self.height )



        draw_rectangle(*self.crush_box())

