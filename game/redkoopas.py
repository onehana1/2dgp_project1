from pico2d import *
import game_world
import random


import server
import collision

class redKoopas:

    def __init__(self):
        self.x, self.y = 50, 90
        self.image = load_image('redKoopas_r.png')
        self.image2 = load_image('redKoopas_l.png')

        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.frame = 0


    def crush_box(self):
        return self.x-25, self.y-30, self.x +25, self.y+30

    def do(self):
        pass
    
    def update(self):
        self.timer += 1

        if(self.timer%1000 == 0):
            self.dir += 1

        if ((self.dir % 2) == 1):
            self.x += 0.5
        else:
            self.x -= 0.5


        self.frame = (self.frame + 1) % 2


        
        for server.redkoopas in server.redkoopass:  

            if collision.collide_floor(server.boy, server.redkoopas): #밟 처치
                server.boy.y += 35
                server.boy.jumping_mon = True
                server.redkoopas.state = 1
                server.redkoopass.remove(server.redkoopas)
                game_world.remove_object(server.redkoopas)
                print("1")
                server.boy.score += 500


            elif collision.collide_monster(server.boy, server.redkoopas):  #충돌
                if(server.boy.inv==False):
                    server.boy.state = 0
                    if server.boy.state == 0:
                        server.boy.x += - server.boy.dir*35
                        server.boy.y += 35
                        server.boy.jumping_mon = True
                        server.boy.inv = True
                        
                        print("2")


        pass

    def draw(self):
        if ((self.dir % 2) == 1):
            self.image.clip_draw(55 + 31*self.frame, 5, 31, 24, self.x, self.y,60,70)
        else:
            self.image2.clip_draw(85 - 31*self.frame, 5, 31, 24, self.x, self.y,60,70)

        draw_rectangle(*self.crush_box())


