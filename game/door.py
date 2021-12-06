from pico2d import *
import game_world

import game_framework
import server
import collision

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 4
FRAMES_PER_ACTION = 1



class Door:
    font = None
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        self.image = load_image('start.png')
        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0
        self.state = 0
        
        self.w=159
        self.h=179





    def crush_box(self):
        return self.x- server.boy.x + 30, self.y, self.x + self.w - server.boy.x , self.y+ self.h 

    def do(self):
        pass
    
    def update(self):



        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3



        if collision.collide(server.boy, self):
            print("도착~")
            server.stage = 1





    def draw(self): 
        self.image.clip_draw_to_origin(0, 0, self.w, self.h, self.x- server.boy.x, self.y,self.w * 2,self.h * 2)
        draw_rectangle(*self.crush_box())




