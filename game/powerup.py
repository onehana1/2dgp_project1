from pico2d import *
import game_world

import game_framework


# item Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 4
FRAMES_PER_ACTION = 1

box = None


class Mushroom:

    def __init__(self):
        self.x, self.y = 1600 // 2, 180
        self.image = load_image('powerup.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0

        self.state = 0
        self.fall = 1



    def crush_box(self):
        return self.x-21, self.y-19, self.x +21, self.y+19

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        if self.state >= 1:
            if(self.timer%1000 == 0):
                self.dir += 1

            if ((self.dir % 2) == 1):
                self.velocity += RUN_SPEED_PPS
                self.x += self.velocity * game_framework.frame_time
            else:
                self.velocity -= RUN_SPEED_PPS
                self.x += self.velocity * game_framework.frame_time

        
        if(self.fall==1 and self.state >=1):
            self.y -= 1

            pass

    def draw(self): 
        if self.state >=1:
            self.image.clip_draw(21, 60, 21, 19, self.x, self.y,42,38)


        draw_rectangle(*self.crush_box())


class Flower:

    def __init__(self):
        self.x, self.y = 600, 180
        self.image = load_image('powerup.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0

        self.state = 0
        self.fall = 1


    def crush_box(self):
        return self.x-19, self.y-20, self.x +19, self.y+20

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        if(self.fall==1 and self.state >=1):
            self.y -= 1

        pass

    def draw(self): 
        if self.state >= 1:
            self.image.clip_draw(2 + 19*int(self.frame), 40, 19, 20, self.x, self.y,38,40)

        draw_rectangle(*self.crush_box())


class Coin:

    def __init__(self):
        self.x, self.y = 600, 180
        self.image = load_image('coin.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 1000
        self.frame = 0

        self.state = 0


    def crush_box(self):
        return self.x-19, self.y-20, self.x +19, self.y+20

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if self.state==1:
            self.timer -= 1
            print("coin:",self.timer)
        pass

    def draw(self): 
        if self.state == 1 and self.timer >=0:
            self.image.clip_draw(1, 32, 12, 16, self.x, self.y,24,32)
            

        draw_rectangle(*self.crush_box())
