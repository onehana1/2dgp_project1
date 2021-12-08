from pico2d import *
import game_world

import game_framework
import server
import collision

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 4
FRAMES_PER_ACTION = 1



class Block:
    font = None
    def __init__(self, count = '1', x = 0, y = 0):
        self.x, self.y = x, y
        self.image = load_image('block.png')
        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0
        self.state = 0
        self.count = count
        if Block.font is None:
            Block.font = load_font('ENCR10B.TTF', 16)


    def crush_box(self):
        return self.x-18- server.boy.x, self.y-18, self.x +18- server.boy.x, self.y+18

    def do(self):
        pass
    
    def update(self):
        self.timer += 1

        if(self.timer%1000 == 0):
            self.dir += 1


        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        for block in server.blocks:  

            if collision.collide_head(server.boy, block):
                print("블록 깨기")
                block.state = 1
                server.boy.fall = 1

                server.coin += 50

                

                server.blocks.remove(block)
                game_world.remove_object(block)
                server.boy.coin_sound.play()

        pass

    def draw(self): 
        self.image.clip_draw(2, 96, 18, 18, self.x- server.boy.x, self.y,36,36)
        # draw_rectangle(*self.crush_box())




