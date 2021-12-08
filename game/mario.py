from math import trunc
from pico2d import *
import game_world
import game_framework

from fire import Fire


import server
import collision



# mario Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER,UP_DOWN,UP_UP ,z_DOWN,z_UP ,down_UP,down_DOWN = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,

    (SDL_KEYDOWN, SDLK_DOWN): down_DOWN,
    (SDL_KEYUP, SDLK_DOWN): down_UP,

    (SDL_KEYDOWN, SDLK_z): z_DOWN,
    (SDL_KEYUP, SDLK_z): z_UP


}


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm

# mario Run Speed
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# mario Jump speed
JUMP_SPEED_KMPH = 40.0 # Km / Hour
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

# mario Fall speed
Fall_SPEED_KMPH = 30.0 # Km / Hour
Fall_SPEED_MPM = (Fall_SPEED_KMPH * 1000.0 / 60.0)
Fall_SPEED_MPS = (Fall_SPEED_MPM / 60.0)
Fall_SPEED_PPS = (Fall_SPEED_MPS * PIXEL_PER_METER)

# mario Action Speed
TIME_PER_ACTION = 3
ACTION_PER_TIME = 20
FRAMES_PER_ACTION = 1

# mario States

class IdleState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        elif event == z_DOWN:
            boy.attact = True
            boy.fire = True
        elif event == z_UP:
            boy.attact = False

        boy.timer = 1000


    def exit(boy, event):
        if event == UP_DOWN:

            # boy.jump_v += JUMP_SPEED_PPS * boy.jump_timer
            if  boy.jumping == True:
                boy.one = 0
            else:
                boy.one =1

            if  boy.jumping == True:
                boy.two = 0
            else:
                boy.two =1

            boy.jumping = True

        if event == UP_UP:
            # boy.jump_v += JUMP_SPEED_PPS * boy.jump_timer
    
            pass

        if event == z_DOWN:
            boy.attact = True
            boy.fire_ball()

        if event == z_UP:
            boy.attact = False





        pass

    def do(boy):
        boy.timer -= 1
        if boy.timer == 0:
            #boy.add_event(SLEEP_TIMER)
            pass
        



    def draw(boy):
        cx, cy = boy.x - server.background.window_left, boy.y - server.background.window_bottom
        if server.mario_star == 0:
            if server.mario_state == 0:
                if boy.dir == 1:
                    if boy.fall == 0 and boy.jumping == False:
                        boy.image.clip_draw(202, 171, 30, 18, cx, cy,60,35)
                    elif boy.jumping == True:
                        boy.image.clip_draw(356, 171, 30, 18, cx, cy,60,35)
                    else:
                        boy.image.clip_draw(352, 103, 30, 35, cx, cy,60,35)    
                else:
                    if boy.fall == 0 and boy.jumping == False:
                        boy.image.clip_draw(173, 171, 30, 18, cx, cy,60,35)
                    elif boy.jumping == True:
                        boy.image.clip_draw(26, 171, 30, 18, cx, cy,60,35)
                    else:
                        boy.image.clip_draw(22, 103, 30, 35, cx, cy,60,35)

            if server.mario_state == 1:
                if boy.dir == 1:
                    if boy.fall == 0 and boy.jumping == False:
                        boy.image.clip_draw(202, 103, 30, 35, cx, cy + 35,60,70)
                    elif boy.jumping == True:
                        boy.image.clip_draw(356, 103, 30, 35, cx, cy,60,70)
                    else:
                        boy.image.clip_draw(352, 103, 30, 35, cx, cy + 35,60,70)   
                else:
                    if boy.fall == 0 and boy.jumping == False:
                        boy.image.clip_draw(173, 103, 30, 35, cx, cy + 35,60,70)
                    elif boy.jumping == True:
                        boy.image.clip_draw(26, 103, 30, 35, cx, cy,60,70)
                    else:
                        boy.image.clip_draw(22, 103, 30, 35, cx, cy + 35,60,70)

            if server.mario_state == 2:
                if boy.dir == 1:
                    if boy.fall == 0 and boy.jumping == False:
                            if boy.attact==True:
                                boy.image.clip_draw(310, 33, 21, 35, cx, cy+ 35,42,70)
                            else:
                                boy.image.clip_draw(202, 32,  25, 37, cx, cy + 35,50,70)

                    elif boy.jumping == True:
                        boy.image.clip_draw(358, 32, 30, 35, cx, cy + 35,50,70)
                    else:
                        boy.image.clip_draw(358, 32, 25, 37, cx, cy + 35,50,70)
                else:
                    if boy.fall == 0 and boy.jumping == False:
                        if boy.attact==True:
                            boy.image.clip_draw(74, 33, 23, 35, cx, cy+ 35,46,70)
                        else: 
                            boy.image.clip_draw(173, 32,  25, 37, cx, cy + 35,50,70)

                    elif boy.jumping == True:
                        boy.image.clip_draw(20, 32, 30, 35, cx, cy + 35,50,70)

                    else:
                        boy.image.clip_draw(24, 32, 25, 37, cx, cy + 35,50,70)
        else:
            if server.mario_state == 0:
                    if boy.dir == 1:
                        if boy.fall == 0:
                            boy.image_star.clip_draw(202, 171, 30, 18, cx, cy,60,35)
                        else:
                            boy.image_star.clip_draw(352, 103, 30, 35, cx, cy,60,35)    
                    else:
                        if boy.fall == 0:
                            boy.image_star.clip_draw(173, 171, 30, 18, cx, cy,60,35)
                        else:
                            boy.image_star.clip_draw(22, 103, 30, 35, cx, cy,60,35)

            if server.mario_state == 1:
                if boy.dir == 1:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(202, 103, 30, 35, cx, cy + 35,60,70)
                    else:
                        boy.image_star.clip_draw(352, 103, 30, 35, cx, cy + 35,60,70)   
                else:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(173, 103, 30, 35, cx, cy + 35,60,70)
                    else:
                        boy.image_star.clip_draw(22, 103, 30, 35, cx, cy + 35,60,70)

            if server.mario_state == 2:
                if boy.dir == 1:
                    if boy.fall == 0:
                            if boy.attact==True:
                                boy.image_star.clip_draw(310, 33, 21, 35, cx, cy+ 35,42,70)
                            else:
                                boy.image_star.clip_draw(202, 32,  25, 37, cx, cy + 35,50,70)
                    else:
                        boy.image_star.clip_draw(358, 32, 25, 37, cx, cy + 35,50,70)
                else:
                    if boy.fall == 0:
                        if boy.attact==True:
                            boy.image_star.clip_draw(74, 33, 23, 35, cx, cy+ 35,46,70)
                        else: 
                            boy.image_star.clip_draw(173, 32,  25, 37, cx, cy + 35,50,70)
                    else:
                        boy.image_star.clip_draw(24, 32, 25, 37, cx, cy + 35,50,70)


            

        
        




class RunState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            if boy.go == 1:
                boy.velocity += RUN_SPEED_PPS

        elif event == LEFT_DOWN:
            if boy.go == 1:
                boy.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            if boy.go == 1:
                boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            if boy.go == 1:
                boy.velocity += RUN_SPEED_PPS

                

        boy.dir = clamp(-1, boy.velocity, 1)

    def exit(boy, event):
        if event == UP_DOWN:
            #boy.jump_v += JUMP_SPEED_PPS
            if  boy.jumping == True:
                boy.one = 0
            else:
                boy.one =1

            if  boy.jumping == True:
                boy.two = 0
            else:
                boy.two =1
                
            boy.jumping =True

        if event == UP_UP:
            #boy.jump_v -= JUMP_SPEED_PPS
            pass
            

        if event == z_DOWN:
            boy.attack = True 
            boy.fire_ball()

        if event == z_UP:
            boy.attack = False

        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.timer -= 1
        if boy.stopping==False:
            boy.x += boy.velocity * game_framework.frame_time

        # boy.x = clamp(25, boy.x, 1600 - 25)

    def draw(boy):
        cx, cy = boy.x - server.background.window_left, boy.y - server.background.window_bottom
        #print(cx)
        #print(boy.x)

        if server.mario_star == 0:
            if server.mario_state == 0:
                if boy.dir == 1:
                    if boy.fall == 0:
                        boy.image.clip_draw(232 + 30*int(boy.frame), 173, 30, 35, cx, cy,60,35)
                    else:
                        boy.image.clip_draw(352, 103, 30, 35, cx, cy,60,35)
                else:
                    if boy.fall == 0:
                        boy.image.clip_draw(143 - 30*int(boy.frame), 173, 30, 35, cx, cy,60,35)
                    else:
                        boy.image.clip_draw(22, 103, 30, 35, cx, cy,60,35)

            if server.mario_state==1:
                if boy.dir == 1:
                    if boy.fall == 0:
                        boy.image.clip_draw(232 + 30*int(boy.frame), 103, 30, 35, cx, cy + 35,60,70)
                    else:
                        boy.image.clip_draw(352, 103, 30, 35, cx, cy + 35,60,70)
                else:
                    if boy.fall == 0:
                        boy.image.clip_draw(143 - 30 *int(boy.frame), 103, 30, 35, cx, cy + 35,60,70)
                    else:
                        boy.image.clip_draw(22, 103, 30, 35, cx, cy + 35,60,70)

            if server.mario_state== 2:
                if boy.dir == 1:
                    if boy.fall == 0:
                        boy.image.clip_draw(232 + 25*int(boy.frame), 32, 25, 35, cx, cy + 35,50,70)
                    else:
                        boy.image.clip_draw(358, 32, 25, 37, cx, cy + 35,60,70)
                else:
                    if boy.fall == 0:
                        boy.image.clip_draw(143 - 25*int(boy.frame), 32, 25, 35, cx, cy + 35,50,70)
                    else:
                        boy.image.clip_draw(24, 32, 25, 37, cx, cy + 35,50,70)

        if server.mario_star == 1:
            if server.mario_state == 0:
                if boy.dir == 1:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(232 + 30*int(boy.frame), 173, 30, 35, cx, cy,60,35)
                    else:
                        boy.image_star.clip_draw(352, 103, 30, 35, cx, cy,60,35)
                else:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(143 - 30*int(boy.frame), 173, 30, 35, cx, cy,60,35)
                    else:
                        boy.image_star.clip_draw(22, 103, 30, 35, cx, cy,60,35)

            if server.mario_state==1:
                if boy.dir == 1:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(232 + 30*int(boy.frame), 103, 30, 35, cx, cy + 35,60,70)
                    else:
                        boy.image_star.clip_draw(352, 103, 30, 35, cx, cy + 35,60,70)
                else:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(143 - 30 *int(boy.frame), 103, 30, 35, cx, cy + 35,60,70)
                    else:
                        boy.image_star.clip_draw(22, 103, 30, 35, cx, cy + 35,60,70)

            if server.mario_state== 2:
                if boy.dir == 1:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(232 + 25*int(boy.frame), 32, 25, 35, cx, cy + 35,50,70)
                    else:
                        boy.image_star.clip_draw(358, 32, 25, 37, cx, cy + 35,60,70)
                else:
                    if boy.fall == 0:
                        boy.image_star.clip_draw(143 - 25*int(boy.frame), 32, 25, 35, cx, cy + 35,50,70)
                    else:
                        boy.image_star.clip_draw(24, 32, 25, 37, cx, cy + 35,50,70)


class CrouchState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        elif event == z_DOWN:
            boy.attact = True
            boy.fire = True
        elif event == z_UP:
            boy.attact = False

        event = down_DOWN



    def exit(boy, event):
        pass


    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        
        

    def draw(boy):
        cx, cy = boy.x - server.background.window_left, boy.y - server.background.window_bottom

        if server.mario_star == 0:
            if server.mario_state == 0:
                if boy.dir == 1:
                    boy.image.clip_draw(387, 107, 20, 26, cx, cy,40,35)

                else:
                    boy.image.clip_draw(0, 107, 20, 26, cx, cy,40,35)


            if server.mario_state==1:
                if boy.dir == 1:
                    boy.image.clip_draw(387, 107, 20, 26, cx, cy,40,52)

                else:
                    boy.image.clip_draw(0, 107, 20, 26, cx, cy,40,52)

            if server.mario_state== 2:
                if server.mario_state==1:
                    if boy.dir == 1:
                        boy.image.clip_draw(387, 37, 20, 26, cx, cy,40,52)

                    else:
                        boy.image.clip_draw(0, 37, 20, 26, cx, cy,40,52)

        if server.mario_star == 1:
            if server.mario_state == 0:
                if boy.dir == 1:
                    boy.image_star.clip_draw(387, 107, 20, 26, cx, cy,40,35)

                else:
                    boy.image_star.clip_draw(0, 107, 20, 26, cx, cy,40,35)


            if server.mario_state==1:
                if boy.dir == 1:
                    boy.image_star.clip_draw(387, 107, 20, 26, cx, cy,40,52)

                else:
                    boy.image_star.clip_draw(0, 107, 20, 26, cx, cy,40,52)

            if server.mario_state== 2:
                if server.mario_state==1:
                    if boy.dir == 1:
                        boy.image_star.clip_draw(387, 37, 20, 26, cx, cy,40,52)

                    else:
                        boy.image_star.clip_draw(0, 37, 20, 26, cx, cy,40,52)


        

class DieState:

    def enter(boy, event):
        # server.mario_state = 4
        # if event == UP_DOWN:
        #     server.mario_state = 1
        server.mario_state = -1
        # boy.die_sound.play(1)
        # boy.life = 0

    def exit(boy, event):
        boy.die_timer < 0
        print("die 끝")
        
        pass


    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.y -= boy.velocity * game_framework.frame_time
        

    def draw(boy):
        boy.image.clip_draw(386, 155, 19, 21, boy.x, boy.y+100, 38, 42)
        # boy.image3.clip_draw(0,0,512,301,800,300,1600,600)

        


class SleepState:

    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        if event == UP_DOWN:
            #boy.jump()
            boy.jumping =True

        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(202, 103, 30, 35, boy.x, boy.y,60, 70)
        else:
            boy.image.clip_draw(173, 103, 30, 35, boy.x, boy.y,60, 70)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, 
    UP_DOWN: IdleState, UP_UP:IdleState,z_DOWN:IdleState,z_UP:IdleState 
    ,down_DOWN:CrouchState,down_UP:IdleState},

    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, 
    UP_DOWN: RunState, UP_UP: RunState,z_DOWN:RunState,z_UP:RunState 
    ,down_DOWN:CrouchState,down_UP:RunState },

    DieState: {RIGHT_UP: DieState, LEFT_UP: DieState, RIGHT_DOWN: DieState, LEFT_DOWN: DieState,
     UP_DOWN: DieState, UP_UP:DieState,z_DOWN:DieState,z_UP:DieState 
     ,down_DOWN:DieState,down_UP:DieState},

    CrouchState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, 
    UP_DOWN: IdleState, UP_UP:IdleState,z_DOWN:IdleState,z_UP:IdleState
    ,down_DOWN:IdleState,down_UP:IdleState }

}
   # JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState, UP_DOWN: IdleState, UP_UP:IdleState},
    # SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, UP_DOWN: IdleState, UP_UP:SleepState}

class Boy:

    def __init__(self):
        self.x, self.y = 200, 150
        self.image = load_image('mario_sheet.png')
        self.image2 = load_image('mario_sheet_80.png')
        self.image3 = load_image('gameover.png')
        self.image_star = load_image('mario_sheet_star.png')

        self.jump_small_sound = load_wav('sound/jump_small.wav')
        self.jump_small_sound.set_volume(32)

        self.jump_super_sound = load_wav('sound/jump_super.wav')
        self.jump_super_sound.set_volume(32)

        self.die_sound = load_wav('sound/mariodie.wav')
        self.die_sound.set_volume(32)

        self.dump_sound = load_wav('sound/bump.wav')
        self.dump_sound.set_volume(32)

        self.kick_sound = load_wav('sound/kick.wav')
        self.kick_sound.set_volume(32)

        self.coin_sound = load_wav('sound/coin.wav')
        self.coin_sound.set_volume(16)

        self.stomb_sound = load_wav('sound/stomp.wav')
        self.stomb_sound.set_volume(32)

        self.fireball_sound = load_wav('sound/fireball.wav')
        self.fireball_sound.set_volume(32)

        self.powerup_sound = load_wav('sound/powerup.wav')
        self.powerup_sound.set_volume(32)

        self.star_sound = load_wav('sound/star.wav')
        self.star_sound.set_volume(32)

        self.gameover_sound = load_wav('sound/gameover.wav')
        self.gameover_sound.set_volume(32)







        self.font = load_font('supermariobros.ttf', 30)
        self.one = 1
        self.two = 1

        self.score = 0
        self.coin = 0

        self.star = False
        self.star_timer = 5


        
        self.stage = 0

        self.dir = 1
        self.velocity = 0
        self.jump_timer = 0
        self.jump_timer_m = 0

        self.jump_power = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.attact = False
        self.fire = False

        # self.cam = 800

    
        self.fall = 1
        self.g = 0

        self.jumping = False
        self.jumping_mon = False

        self.jump_v = 0
        self.stopping = False

        self.state = 0
        self.die_timer = 2

        self.go = 1

        self.inv = False #무적상태
        self.inv_timer = 0 #무적상태 time
        
        self.time = 100

    # def camera(self):
    

    #     self.x = self.x
    #     self.x= clamp(600,  self.x, 900)


    #     # if self.x < 700:
    #     #     self.cam = 0
            
        
    #     # if self.x > 800:
    #     #     self.cam +=  self.velocity * game_framework.frame_time

    def fire_ball(self):
        if self.attact == True and server.mario_state == 2:
            # print("어택!")
            fire = Fire()
            game_world.add_object(fire, 1)

        # server.df_fire = Fire(self.x, self.y+40, self.dir)

        # server.fires.append(server.df_fire)
        # game_world.add_objects(server.fires, 1)






    def crush_box(self):
        cx, cy = self.x - server.background.window_left, self.y - server.background.window_bottom
        
        if server.mario_state==0:
            return cx-15, cy-18, cx + 15, cy+18

        if server.mario_state==1:
            return cx-15, cy, cx + 15, cy+70

        if server.mario_state==2:
            return cx-15, cy, cx + 15, cy+70

        if server.mario_state== -1:
            return cx, cy, cx , cy




        print("점프")
        pass
        

    def jump(self):
        self.jump_v = JUMP_SPEED_PPS
        self.jump_v -= game_framework.frame_time * self.jump_timer * JUMP_SPEED_PPS


        if (self.jumping == True and self.fall == 0):
            self.jump_timer += 1 * game_framework.frame_time
            #self.y += 100
            self.y += self.jump_v * game_framework.frame_time


            # print("jumpv",self.jump_v)
            # print(self.jump_timer)

            if server.mario_state==0 and self.one == 1:
                self.jump_small_sound.play(1)
                print(self.one)

            self.one -= game_framework.frame_time

            if server.mario_state > 0 and self.two == 1:
                self.jump_super_sound.play(1)

            self.two -= game_framework.frame_time
            


   

        if (self.jump_timer > 0.7 or self.fall == 1):
            self.jump_timer = 0
            self.jump_timer_m = 0
            self.jump_v = 0

            self.fall = 1


            
        if(self.fall == 1 and self.jumping == True):
            self.jumping = False

        if self.jumping == False:
            self.fall = True


    def jump_mon(self):


        if (self.jumping_mon == True and self.fall == 0):
            self.jump_v = JUMP_SPEED_PPS
            self.jump_v -= game_framework.frame_time * self.jump_timer * JUMP_SPEED_PPS
            self.jump_timer_m += 1
            self.jumping = False
            #self.y += 100
            self.y += self.jump_v * game_framework.frame_time  
            # print("mon")


        if (self.jump_timer_m > 75):
            self.jump_timer_m = 0
            self.jump_timer = 0
            self.jump_v = 0

            self.fall = 1

            
        if(self.fall == 1 and self.jumping_mon == True):
            self.jumping_mon = False








    def drop(self):
        if(self.fall == 1 and self.jumping ==False and self.jumping_mon ==False):

            self.y -= Fall_SPEED_PPS * game_framework.frame_time





    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.time += game_framework.frame_time

        self.cur_state.do(self)

        if server.mario_star == 0:
            server.boy.star_sound.set_volume(0) 
        if server.mario_star == 1:
            server.boy.star_sound.set_volume(64)

        if server.mario_star ==True:
            self.star_timer -= game_framework.frame_time

        if self.star_timer <=0:
            server.mario_star = False
            self.star_timer = 5

        if self.inv ==True:
            self.inv_timer += 1 * game_framework.frame_time
            # print(self.inv_timer)

        if self.inv_timer >=3:
            self.inv = False
            self.inv_timer = 0

        # self.camera()
        self.drop()
        
        self.jump_mon()
        self.jump()

        if server.mario_state == -1:
            self.cur_state = DieState
            self.die_timer -= game_framework.frame_time

        if self.y <= -10:
            self.cur_state = DieState
            
            self.die_timer -= game_framework.frame_time
            

        if self.die_timer <0 :
            self.die_timer = 2
            self.die_sound.play(1)
            server.mario_die = True

            # server.mario_life -= 1
            # print(self.cur_state)
            # print(server.mario_life)


        # if(self.y < 0):
        #     self.state=4
        
        self.x = clamp(50, self.x, server.background.w - 50)
        # self.y = clamp(-50, self.y, server.background.h - 50)
                        

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if collision.collide_floor(self, server.stage1_ground1):
            # print("땅에 있음")
            self.fall = 0

        if collision.collide_floor(self, server.stage1_ground2):
            # print("땅에 있음")
            self.fall = 0

        if collision.collide_floor(self, server.stage1_ground3):
            # print("땅에 있음")
            self.fall = 0

        if collision.collide_floor(self, server.stage1_ground4):
            # print("땅에 있음")
            self.fall = 0

        for box in server.boxs:  
            if collision.collide_floor(self, box):
                server.boy.fall = 0
                print("박스 밟음")
            elif collision.collide_side(self, box):
                print("박스 사이드")
                self.x -= self.velocity * game_framework.frame_time

        for box2 in server.boxs2:  
            if collision.collide_floor(self, box2):
                server.boy.fall = 0
                print("박스2 밟음")
            elif collision.collide_side(self, box2):
                print("박스2 사이드")
                self.x -= self.velocity * game_framework.frame_time

        for box3 in server.boxs3:  
            if collision.collide_floor(self, box3):
                server.boy.fall = 0
                print("박스2 밟음")
            elif collision.collide_side(self, box3):
                print("박스2 사이드")
                self.x -= self.velocity * game_framework.frame_time


        for block in server.blocks:  
            if collision.collide_floor(self, block):
                server.boy.fall = 0
                print("박스2 밟음")
            elif collision.collide_side(self, block):
                print("박스2 사이드")
                self.x -= self.velocity * game_framework.frame_time


        # print(self.x)
        for pype in server.pypes:  
            if collision.collide_floor(self, pype):
                print("파이프 밟")
                self.fall = 0
            elif collision.collide_side(self, pype):
                print("파이프 사이드")
               
                self.x -= self.velocity * game_framework.frame_time

                # print(self.x)
                # print(pype.x)

                
        
                

        # if not collision.collide_floor(self, server.stage1_ground1)and not collision.collide_floor(self, server.stage1_ground2) and not collision.collide_floor(self, server.box):
        # # print("fall!!")
        #     self.fall = 1





        




    def draw(self):
        self.cur_state.draw(self)
        # debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir) + '  State:' + str(self.cur_state))
        # draw_rectangle(*self.crush_box())
        self.font.draw(1300, 560, 'Time: %3.0f' % (server.time - self.time), (255, 255, 255))
        self.font.draw(700, 560, 'Score: %3.0f' % server.score, (0, 0, 0))
        self.font.draw(100, 500, 'Life: %3.0f' % server.mario_life, (255, 0, 0))
        self.font.draw(100, 560, 'Coin: %3.0f' % server.coin, (255, 255, 0))


        cx, cy = self.x - server.background.window_left, self.y - server.background.window_bottom
        # self.font.draw(cx - 40, cy + 40, '(%d, %d)' % (self.x, self.y), (255, 255, 0))
        






    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        

