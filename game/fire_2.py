from pico2d import *
import game_world
import game_framework
import random
import server
import collision
# import main_state


# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# monster Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 20
FRAMES_PER_ACTION = 1



class Fire:
    image = None
    def __init__(self):
        if Fire.image == None:
            Fire.image = load_image('fireball.png')
        
        self.x, self.y, self.dir = server.boy.x, server.boy.y + 40, server.boy.dir
        global cam

        self.velocity = 0
        self.jump_timer = 0
        self.frame = 0
        self.timer = 1

        self.state = 0
      


    def crush_box(self):
        return self.x-12 , self.y-13, self.x +12, self.y+13

    def do(self):
        pass
    
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.timer -= game_framework.frame_time
        
        if(self.timer <= 0):
            self.state = 1
            self.timer = 1

        self.velocity = RUN_SPEED_PPS
        if self.dir==1:
            self.x +=  self.velocity * game_framework.frame_time
            print(" +! : ",self.velocity)

        if self.dir== -1:
            self.x -=  self.velocity * game_framework.frame_time
            print(" -! : ",self.velocity)

        if self.y < 50 :
            game_world.remove_object(self)



        for koopas in server.koopass:  

            if collision.collide(self, koopas):
                server.koopass.remove(koopas)
                game_world.remove_object(koopas)
                game_world.remove_object(self)
                print("불로처치")
                server.score += 500

        for redkoopas in server.redkoopass:  

            if collision.collide(self, redkoopas): 
                server.redkoopass.remove(redkoopas)
                game_world.remove_object(redkoopas)
                game_world.remove_object(self)
                print("불로처치")
                server.score += 500

        for gumba in server.gumbas:  

            if collision.collide(self, gumba): 
                server.gumbas.remove(gumba)
                game_world.remove_object(gumba)
                game_world.remove_object(self)
                print("불로처치")
                server.score += 500

        for pype in server.pypes:  
            if collision.collide(self, pype): 
                game_world.remove_object(self)




    def draw(self):
        if self.state==0:
            self.image.clip_draw( 1 + int(self.frame)*1, 4, 12, 13, self.x, self.y, 24, 26)
        if self.state==1:
            game_world.remove_object(self)
        





        draw_rectangle(*self.crush_box())
