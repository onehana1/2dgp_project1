from math import trunc
from pico2d import *
import game_world
import game_framework

from fire import Fire


import server
import collision



# mario Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER,UP_DOWN,UP_UP ,SPACE_DOWN,SPACE_UP,z_DOWN,z_UP = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP,
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
JUMP_SPEED_KMPH = 20.0 # Km / Hour
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

# mario Fall speed
Fall_SPEED_KMPH = 20.0 # Km / Hour
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
            boy.attect = True
        elif event == z_UP:
            boy.attect = False

        boy.timer = 1000


    def exit(boy, event):
        if event == UP_DOWN:

            # boy.jump_v += JUMP_SPEED_PPS * boy.jump_timer
            boy.jumping = True

        if event == UP_UP:
            # boy.jump_v += JUMP_SPEED_PPS * boy.jump_timer
    
            pass

        if event == z_DOWN:
            boy.fire_ball()




        pass

    def do(boy):
        boy.timer -= 1
        if boy.timer == 0:
            #boy.add_event(SLEEP_TIMER)
            pass
        



    def draw(boy):
        if boy.state == 0:
            if boy.dir == 1:
                if boy.fall == 0:
                    boy.image.clip_draw(202, 171, 30, 18, boy.draw_x, boy.y,60,35)
                else:
                    boy.image.clip_draw(352, 103, 30, 35, boy.draw_x, boy.y,60,35)    
            else:
                if boy.fall == 0:
                    boy.image.clip_draw(173, 171, 30, 18, boy.draw_x, boy.y,60,35)
                else:
                    boy.image.clip_draw(22, 103, 30, 35, boy.draw_x, boy.y,60,35)

        if boy.state == 1:
            if boy.dir == 1:
                if boy.fall == 0:
                    boy.image.clip_draw(202, 103, 30, 35, boy.draw_x, boy.y + 35,60,70)
                else:
                    boy.image.clip_draw(352, 103, 30, 35, boy.draw_x, boy.y + 35,60,70)   
            else:
                if boy.fall == 0:
                    boy.image.clip_draw(173, 103, 30, 35, boy.draw_x, boy.y + 35,60,70)
                else:
                    boy.image.clip_draw(22, 103, 30, 35, boy.draw_x, boy.y + 35,60,70)

        if boy.state == 2:
            if boy.dir == 1:
                if boy.fall == 0:
                        if boy.attect==True:
                            boy.image.clip_draw(310, 33, 21, 35, boy.draw_x, boy.y+ 35,42,70)
                        else:
                            boy.image.clip_draw(202, 32,  25, 37, boy.draw_x, boy.y + 35,50,70)
                else:
                    boy.image.clip_draw(358, 32, 25, 37, boy.draw_x, boy.y + 35,50,70)
            else:
                if boy.fall == 0:
                    if boy.attect==True:
                        boy.image.clip_draw(74, 33, 23, 35, boy.draw_x, boy.y+ 35,46,70)
                    else: 
                        boy.image.clip_draw(173, 32,  25, 37, boy.draw_x, boy.y + 35,50,70)
                else:
                    boy.image.clip_draw(24, 32, 25, 37, boy.draw_x, boy.y + 35,50,70)

        
        




class RunState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS

        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        boy.dir = clamp(-1, boy.velocity, 1)

    def exit(boy, event):
        if event == UP_DOWN:
            boy.jump_v += JUMP_SPEED_PPS
            boy.jumping =True

        if event == UP_UP:
            boy.jump_v -= JUMP_SPEED_PPS
            

        if event == z_DOWN:
            boy.fire_ball()

        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.timer -= 1
        if boy.stopping==False:
            boy.x += boy.velocity * game_framework.frame_time

        # boy.x = clamp(25, boy.x, 1600 - 25)

    def draw(boy):

        if boy.state == 0:
            if boy.dir == 1:
                if boy.fall == 0:
                    boy.image.clip_draw(232 + 30*int(boy.frame), 173, 30, 35, boy.draw_x, boy.y,60,35)
                else:
                    boy.image.clip_draw(352, 103, 30, 35, boy.draw_x, boy.y,60,35)
            else:
                if boy.fall == 0:
                    boy.image.clip_draw(143 - 30*int(boy.frame), 173, 30, 35, boy.draw_x, boy.y,60,35)
                else:
                    boy.image.clip_draw(22, 103, 30, 35, boy.draw_x, boy.y,60,35)

        if boy.state==1:
            if boy.dir == 1:
                if boy.fall == 0:
                    boy.image.clip_draw(232 + 30*int(boy.frame), 103, 30, 35, boy.draw_x, boy.y + 35,60,70)
                else:
                    boy.image.clip_draw(352, 103, 30, 35, boy.draw_x, boy.y + 35,60,70)
            else:
                if boy.fall == 0:
                    boy.image.clip_draw(143 - 30 *int(boy.frame), 103, 30, 35, boy.draw_x, boy.y + 35,60,70)
                else:
                    boy.image.clip_draw(22, 103, 30, 35, boy.draw_x, boy.y + 35,60,70)

        if boy.state== 2:
            if boy.dir == 1:
                if boy.fall == 0:
                    boy.image.clip_draw(232 + 25*int(boy.frame), 32, 25, 35, boy.draw_x, boy.y + 35,50,70)
                else:
                    boy.image.clip_draw(358, 32, 25, 37, boy.draw_x, boy.y + 35,60,70)
            else:
                if boy.fall == 0:
                    boy.image.clip_draw(143 - 25*int(boy.frame), 32, 25, 35, boy.draw_x, boy.y + 35,50,70)
                else:
                    boy.image.clip_draw(24, 32, 25, 37, boy.draw_x, boy.y + 35,50,70)


class DieState:

    def enter(boy, event):
        boy.state = 4
        if event == UP_DOWN:
            boy.state = 1

    def exit(boy, event):
        pass


    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.y -= boy.velocity * game_framework.frame_time

    def draw(boy):
        boy.image.clip_draw(386, 155, 19, 21, boy.draw_x, boy.y+100, 38, 42)
        boy.image3.clip_draw(0,0,512,301,800,300,1600,600)

        





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
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: IdleState, UP_UP:IdleState,z_DOWN:IdleState,z_UP:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: RunState, UP_UP: RunState,z_DOWN:RunState,z_UP:RunState },
    DieState: {RIGHT_UP: DieState, LEFT_UP: DieState, RIGHT_DOWN: DieState, LEFT_DOWN: DieState, UP_DOWN: IdleState, UP_UP:DieState,z_DOWN:DieState,z_UP:DieState}

}
   # JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState, UP_DOWN: IdleState, UP_UP:IdleState},
    # SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, UP_DOWN: IdleState, UP_UP:SleepState}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 100
        self.image = load_image('mario_sheet.png')
        self.image2 = load_image('mario_sheet_80.png')
        self.image3 = load_image('gameover.png')


        self.font = load_font('ENCR10B.TTF', 30)

        self.score = 0
        self.coin = 0


        self.draw_x = 0


        self.dir = 1
        self.velocity = 0
        self.jump_timer = 0
        self.jump_timer_m = 0

        self.jump_power = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.attect = False

        # self.cam = 800


        self.fall = 1
        self.g = 0

        self.jumping = False
        self.jumping_mon = False

        self.jump_v = 0
        self.stopping = False

        self.state = 0

        self.inv = False #????????????
        self.inv_timer = 0 #???????????? time


    # def camera(self):
    

    #     self.draw_x = self.x
    #     self.draw_x= clamp(600,  self.x, 900)


    #     # if self.x < 700:
    #     #     self.cam = 0
            
        
    #     # if self.x > 800:
    #     #     self.cam +=  self.velocity * game_framework.frame_time

    def fire_ball(self):
        fire = Fire(self.x, self.y+40, self.dir*3)
        game_world.add_object(fire, 1)





    def crush_box(self):
        if self.state==0:
            return self.draw_x-15, self.y-18, self.draw_x + 15, self.y+18

        if self.state==1:
            return self.draw_x-15, self.y, self.draw_x + 15, self.y+70

        if self.state==2:
            return self.draw_x-15, self.y, self.draw_x + 15, self.y+75

        if self.state==4:
            return self.draw_x, self.y, self.draw_x , self.y




        print("??????")
        pass
        

    def jump(self):
        self.jump_v = JUMP_SPEED_PPS
        self.jump_v -= game_framework.frame_time * self.jump_timer * JUMP_SPEED_PPS


        if (self.jumping == True and self.fall == 0):
            self.jump_timer += 1
            #self.y += 100
            self.y += self.jump_v * game_framework.frame_time  
            print("jumpv",self.jump_v)
            print(self.jump_timer)
            


   

        if (self.jump_timer > 100 or self.fall == 1):
            self.jump_timer = 0
            self.fall = 1


            
        if(self.fall == 1 and self.jumping == True):
            self.jumping = False

        if self.jumping == False:
            self.fall = True


    def jump_mon(self):
        self.jump_v = JUMP_SPEED_PPS
        self.jump_v -= game_framework.frame_time * self.jump_timer * JUMP_SPEED_PPS

        if (self.jumping_mon == True and self.fall == 0):
            self.jump_timer_m += 1
            self.jumping = False
            #self.y += 100
            self.y += self.jump_v * game_framework.frame_time  
            print("mon")


        if (self.jump_timer_m > 75):
            self.jump_timer_m = 0
            self.fall = 1

            
        if(self.fall == 1 and self.jumping_mon == True):
            self.jumping_mon = False








    def drop(self):
        if(self.fall == 1 and self.jumping ==False and self.jumping_mon ==False):

            self.y -= Fall_SPEED_PPS * game_framework.frame_time








    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        

        # self.camera()
        self.drop()
        
        self.jump_mon()
        self.jump()

        if self.state == 4:
            self.cur_state = DieState


        # if(self.y < 0):
        #     self.state=4
                        

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if collision.collide_floor(self, server.stage1_ground1):
            # print("?????? ??????")
            self.fall = 0

        if collision.collide_floor(self, server.stage1_ground2):
            # print("?????? ??????")
            self.fall = 0


        # if not collision.collide_floor(self, server.stage1_ground1)and not collision.collide_floor(self, server.stage1_ground2) and not collision.collide_floor(self, server.box):
        # # print("fall!!")
        #     self.fall = 1





        




    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir) + '  State:' + str(self.cur_state))
        draw_rectangle(*self.crush_box())
        self.font.draw(1300, 550, 'Time: %3.0f' % (300 -get_time()), (255, 255, 255))
        self.font.draw(700, 550, 'Score: %3.0f' % self.score, (0, 255, 0))
        self.font.draw(100, 550, 'Coin: %3.0f' % self.coin, (255, 255, 0))
        






    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        

