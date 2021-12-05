from pico2d import *
import game_world

import game_framework
import collision
import server


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



class Mushroom:
    font = None
    

    def __init__(self, count = '1', x = 0, y = 0):
        self.x, self.y = x, y
        self.image = load_image('powerup.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0

        self.state = 0
        self.fall = 1

        self.count = count
        if Mushroom.font is None:
            Mushroom.font = load_font('ENCR10B.TTF', 16)


    def crush_box(self):
        return self.x-21- server.boy.x, self.y-19, self.x +21- server.boy.x, self.y+19

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

            self.fall = 1
       

        for mushroom in server.mushrooms:   

            for box in server.boxs: 
                if collision.collide_floor(mushroom, box):
                    mushroom.fall = 0

            if collision.collide_floor(mushroom, server.stage1_ground1):
                    mushroom.fall = 0
            
            if(mushroom.fall== 1 and mushroom.state >=1):
                    mushroom.y -= 1

            if mushroom.state == 0:
                if collision.collide_head(server.boy, mushroom):
                    mushroom.state += 1 
                    if mushroom.state == 1:
                        mushroom.y += 36
                        
                    if mushroom.state >= 10:
                        print("버섯 나와라")
                        server.mushrooms.remove(mushroom)
                        game_world.remove_object(mushroom)

                        if(server.boy.state == 0):
                            server.boy.state = 1

            else: 
                if collision.collide(server.boy, mushroom):
                    mushroom.state += 1 
                    if mushroom.state == 1:
                        mushroom.y += 36
                        
                    if mushroom.state >= 1:
                        print("변신!!")
                        server.mushrooms.remove(mushroom)
                        game_world.remove_object(mushroom)

                        if(server.boy.state == 0):
                            server.boy.state = 1




                
                
                    


    def draw(self): 
        if self.state >=1:
            self.image.clip_draw(21, 60, 21, 19, self.x- server.boy.x, self.y,42,38)


        draw_rectangle(*self.crush_box())


class Flower:
    font = None

    def __init__(self, count = '1', x = 0, y = 0):
        self.x, self.y = x, y
        self.image = load_image('powerup.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0

        self.state = 0
        self.fall = 1

        self.count = count
        if Flower.font is None:
            Flower.font = load_font('ENCR10B.TTF', 16)

    def crush_box(self):
        return self.x-19- server.boy.x, self.y-20, self.x +19- server.boy.x, self.y+20

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        if(self.fall==1 and self.state >=1):
            self.y -= 1

        for flower in server.flowers:      
            if collision.collide(server.boy, flower):
                if server.flower.state == 1:
                    print("변신!!")
                    game_world.remove_object(flower)
                    server.boy.state = 2
                    # boy.score += 1000







        pass

    def draw(self): 
        if self.state >= 1:
            self.image.clip_draw(2 + 19*int(self.frame), 40, 19, 20, self.x- server.boy.x, self.y,38,40)

        draw_rectangle(*self.crush_box())


class Coin:
    font = None
    def __init__(self, count = '1', x = 0, y = 0):
        self.x, self.y = x, y
        self.image = load_image('coin.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 1000
        self.frame = 0

        self.state = 0

        self.count = count
        if Coin.font is None:
            Coin.font = load_font('ENCR10B.TTF', 16)


    def crush_box(self):
        return self.x-19- server.boy.x, self.y-20, self.x +19- server.boy.x, self.y+20

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
            self.image.clip_draw(1, 32, 12, 16, self.x- server.boy.x, self.y,24,32)
            

        draw_rectangle(*self.crush_box())
