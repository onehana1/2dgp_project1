from pico2d import *
import game_world
import game_framework
import random
import main_state


# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 0.1 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 20
FRAMES_PER_ACTION = 1



class Fire:
    image = None
    def __init__(self, x = 400, y = 500, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image('fireball.png')
        
        self.x, self.y, self.velocity = x, y, velocity
        global cam

        self.dir = 1
        self.velocity = 0
        self.jump_timer = 0
        self.frame = 0
        self.timer = 0

        self.state = 0
      


    def crush_box(self):
        return self.x-12, self.y-13, self.x +12, self.y+13

    def do(self):
        pass
    
    def update(self):

        
        self.timer += 1
        if(self.timer%100 == 0):
            self.state = 1

        self.velocity = RUN_SPEED_PPS
        if self.dir==1:
            self.x +=  self.velocity
        else:
            self.x -=  self.velocity

        
        
        
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2


    def draw(self):
        if self.state==0:
            self.image.clip_draw( 1 + int(self.frame)*1, 4, 12, 13, self.x, self.y, 24, 26)
        if self.state==1:
            game_world.remove_object(self)
        





        draw_rectangle(*self.crush_box())
