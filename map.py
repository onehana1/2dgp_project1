from pico2d import *
import random
import game_framework
import start_state


# Game object class here
# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#     def draw(self):
#         self.image.draw(400,30)


class Stage1: # 3376x240
    # 바닥 20
    def __init__(self):
        self.image = load_image('stage1.png')
    def draw(self):
        self.image.draw(1688-mario.x,120)
        # self.image.draw(1688+mario.x,120+mario.y)


class Gameover:
    def __init__(self):
        self.image = load_image('gameover.png')
    def draw(self):
        self.image.draw(1688,120)


class Mario:

    
    def __init__(self):
        
        self.x, self.y = 10, 40  #위치 정함
        self.jump_state = False
        self.drop_state = False

        self.force = 1
        self.velocity = 1

        


        self.move = False
        self.dir = True
        self.image = load_image('m_mario_r.png')
        self.image2 = load_image('m_mario_l.png')

        self.image3 = load_image('mario_r.png')
        self.image4 = load_image('mario_l.png')
        

        # 19x20(1) // 19x38 (2)
        self.w= 19
        self.h= 20
        self.g= 20 #garo
        self.t=0

        self.time=0

        self.frame = 0

        #####################################################################
        self.life = 2 # 꼬마 마리오로 시작하니까 1 / 2되면 마리오 /3되면 플라워 마리오 

        



    def draw(self):

        # global dir
        # self.x += dir * 0.1
        
        if mario.life==0:
            self.image.clip_draw(20*1,0,self.w,self.h,self.x,self.y)
            delay(0.02)
            # 게임 오버 추가

 
        if mario.jump_state==True:

            if mario.dir ==True:
                if (mario.life==1):
                    self.image.clip_draw(20*6,0,self.w,self.h,self.x,self.y)
                if (mario.life==2):
                    self.image3.clip_draw(24*6,0,self.w,38,self.x,self.y+10)

            if mario.dir ==False:
                if (mario.life==1):
                    self.image2.clip_draw(0,0,19,20,self.x,self.y)
                if (mario.life==2):
                    self.image4.clip_draw(0,0,19,38,self.x,self.y+10)

        elif mario.drop_state==True:

            if mario.dir ==True:
                if (mario.life==1):
                    self.image.clip_draw(20*6,0,self.w,self.h,self.x,self.y)
                if (mario.life==2):
                    self.image3.clip_draw(20*6,0,self.w,38,self.x,self.y+10)
                    

            if mario.dir ==False:
                if (mario.life==1):
                    self.image2.clip_draw(0,0,19,20,self.x,self.y) 
                if (mario.life==2):
                    self.image4.clip_draw(0,0,19,38,self.x,self.y+10)     




        elif mario.dir==True:
            if mario.move==False:
                if (mario.life==1):
                    self.image.clip_draw(20*0,0,self.w,self.h,self.x,self.y)
                if (mario.life==2):
                    self.image3.clip_draw(24*1,0,self.w,38,self.x,self.y+10)

            if mario.move ==True:
                if self.t==1:
                    self.t=3
                
                elif self.t<=3:
                    if (mario.life==1):
                        self.image.clip_draw(20*3,0,self.w,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image3.clip_draw(24*3,0,self.w,38,self.x,self.y+10)
                elif self.t<=5:
                    if (mario.life==1):
                        self.image.clip_draw(19*4,0,self.w,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image3.clip_draw(24*4,0,self.w,38,self.x,self.y+10)
                elif self.t<=7:
                    if (mario.life==1):
                        self.image.clip_draw(19*5,0,self.w,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image3.clip_draw(24*5,0,self.w,38,self.x,self.y+10)
                elif self.t<=9:
                    if (mario.life==1):
                        self.image.clip_draw(19*4,0,self.w,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image3.clip_draw(24*4,0,self.w,38,self.x,self.y+10)

                
                if self.t>=9:
                    self.t=3  #다시 돌려고..

                self.t+=0.05
        
            


        elif mario.dir ==False:
            if mario.move==False:
                if (mario.life==1):
                    self.image2.clip_draw(20*6,0,20,20,self.x,self.y) 
                if (mario.life==2):
                    self.image4.clip_draw(24*5,0,20,38,self.x,self.y+10)  

            if mario.move ==True:
                if self.t==1:
                    self.t=3
                
                elif self.t<=3:
                    if (mario.life==1):
                        self.image2.clip_draw(19*3,0,19,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image4.clip_draw(26*3,0,19,38,self.x,self.y+10)
                elif self.t<=5:
                    if (mario.life==1):
                        self.image2.clip_draw(21*2,0,19,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image4.clip_draw(27*2,0,19,38,self.x,self.y+10)
                elif self.t<=7:
                    if (mario.life==1):
                        self.image2.clip_draw(19*1,0,self.w,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image4.clip_draw(28*1,0,self.w,38,self.x,self.y+10)
                elif self.t<=9:
                    if (mario.life==1):
                        self.image2.clip_draw(21*2,0,19,self.h,self.x,self.y)
                    if (mario.life==2):
                        self.image4.clip_draw(27*2,0,19,38,self.x,self.y+10)

                
                if self.t>=9:
                    self.t=3  #다시 돌려고..
                self.t+=0.05
            
  

class Gumba():
    def __init__(self):
        self.image = load_image('gumba.png')
        self.x, self.y = 50, 40
        self.life =1
        self.dir =True
        self.i =0
        self.j =0



    def draw(self):
        if gumba.life==1:
            if gumba.dir==True:
                self.image.clip_draw(0,0,22,22,self.x,self.y+3)
            



            elif gumba.dir==False:
                self.image.clip_draw(22,0,22,22,self.x,self.y+3)

        if gumba.life == 0:
            self.image.clip_draw(44,0,22,22,self.x,self.y+3)




class Koopas():
    def __init__(self):
        self.image = load_image('koopas_r.png')
        self.image2 = load_image('koopas_l.png')
        self.x, self.y = 100, 40
        self.life =1
        self.dir =True
        self.t =1
        self.i =0
        self.j =0



    def draw(self):
        if koopas.life==1:
            if koopas.dir==True:
                if koopas.t>=1 and koopas.t<=10:
                    self.image.clip_draw(29*2,0,29,31,self.x,self.y+3)
                    koopas.t+=0.1
                elif koopas.t>10 and koopas.t<=20:
                    self.image.clip_draw(29*3,0,29,31,self.x,self.y+3)
                    koopas.t+=0.1
                elif koopas.t>20:
                    koopas.t=1
            



            elif koopas.dir==False:
                if koopas.t>=1 and koopas.t<=10:
                    self.image2.clip_draw(29*3,0,29,31,self.x,self.y+3)
                    koopas.t+=0.1
                elif koopas.t>10 and koopas.t<=20:
                    self.image2.clip_draw(29*2,0,29,31,self.x,self.y+3)
                    koopas.t-=0.1
                elif koopas.t>20:
                    koopas.t=1

        if koopas.life == 0:
            self.image.clip_draw(29*5,0,29,31,self.x,self.y+3)

            

class Red_Koopas():
    def __init__(self):
        self.image = load_image('redkoopas_r.png')
        self.image2 = load_image('redkoopas_l.png')
        self.x, self.y = 150, 40
        self.life =1
        self.dir =True
        self.t =1
        self.i =0
        self.j =0



    def draw(self):
        if redkoopas.life==1:
            if redkoopas.dir==True:
                if redkoopas.t>=1 and redkoopas.t<=10:
                    self.image.clip_draw(29*2,0,29,31,self.x,self.y+3)
                    redkoopas.t+=0.1
                elif redkoopas.t>10 and redkoopas.t<=20:
                    self.image.clip_draw(29*3,0,29,31,self.x,self.y+3)
                    redkoopas.t+=0.1
                elif redkoopas.t>20:
                    redkoopas.t=1
            



            elif redkoopas.dir==False:
                if redkoopas.t>=1 and redkoopas.t<=10:
                    self.image2.clip_draw(29*3,0,29,31,self.x,self.y+3)
                    redkoopas.t+=0.1
                elif redkoopas.t>10 and redkoopas.t<=20:
                    self.image2.clip_draw(29*2,0,29,31,self.x,self.y+3)
                    redkoopas.t-=0.1
                elif redkoopas.t>20:
                    redkoopas.t=1

        if redkoopas.life == 0:
            self.image.clip_draw(29*5,0,29,31,self.x,self.y+3)

            




def gumba_run():
    if gumba.dir ==True:
        gumba.i+=0.1

        if gumba.i>10:
            gumba.dir=False
            gumba.i =0

    elif gumba.dir == False:
        gumba.i+=0.1

        if gumba.i>10:
            gumba.dir=True
            gumba.i =0



def gumba_move():
    
    if gumba.j<10 :
        gumba.x+=0.1
        gumba.j+=0.01
       

    elif gumba.j>10 :
        
        gumba.x-=0.1
        gumba.j+=0.01

    if gumba.j>20:
        gumba.j=0
        



def koopas_move():
    

    if koopas.j<10 :
        koopas.dir=True

        koopas.x+=0.1
        koopas.j+=0.01
       

    elif koopas.j>10 :
        koopas.dir=False
        koopas.x-=0.1
        koopas.j+=0.01

    if koopas.j>20:
        koopas.j=0
        
def redkoopas_move():
    

    if redkoopas.j<10 :
        redkoopas.dir=True

        redkoopas.x+=0.1
        redkoopas.j+=0.01
       

    elif redkoopas.j>10 :
        redkoopas.dir=False
        redkoopas.x-=0.1
        redkoopas.j+=0.01

    if redkoopas.j>20:
        redkoopas.j=0
        




        
def crush():
    if mario.x==gumba.x:
        mario.life=1
        print("와!")

         
   
        
        
        
    





def handle_events():
    
    global running
    global jump
    global monster




    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.dir =True
                mario.move = True
            elif event.key == SDLK_LEFT:
                mario.dir = False
                mario.move = True
            elif event.key == SDLK_UP:
                mario.jump_state = True

            elif event.key == SDLK_a:
                monster = True
            
            elif event.key == SDLK_b:
                mario.life=1

            elif event.key == SDLK_c:
                mario.life=2



            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                mario.move = False
                mario.dir = True
            elif event.key == SDLK_LEFT:
                mario.move = False
                mario.dir = False

            # elif event.key == SDLK_UP:
            #     mario.jump_state =False
                # mario.jump_state =False
                


# initialization code
#open_canvas(3376,240)
#open_canvas(1688,240)
open_canvas(500,240)

game_framework.run(start_state)

gameover = Gameover()
stage1= Stage1()
mario = Mario()
gumba = Gumba()
koopas = Koopas()
redkoopas = Red_Koopas()





running = True
moved=False
monster=False

jump= 0
tm =0
i =0
enemy_move = 0
# game main loop code
while running:
    handle_events()

    gumba_run()
    gumba_move()
    
    koopas_move()
    redkoopas_move()

   
    

    #game logic

    if mario.move ==True:
        # mario.velocity =0
        if mario.velocity>=2:
            mario.velocity=2

        

        if mario.dir == True:
         
            mario.velocity  += 0.005
            mario.x += 0.1 * mario.velocity
           
            moved = True

        elif mario.dir ==False:
         
            mario.velocity  += 0.005
            mario.x -=0.1 * mario.velocity
            
            moved = True


    # if mario.move ==False and moved==True:
    #     mario.x += mario.velocity*1.1
    #     moved=False

    if mario.move ==False:
        mario.velocity =0.1


    if mario.jump_state == True:
        if mario.move ==True:
            mario.y += 0.15 * mario.velocity
        else:
            mario.y += 0.3
        i+=0.1


        if i>10:
            mario.drop_state = True
            mario.jump_state = False
            i=0

    if mario.drop_state == True:
        if mario.move ==True:
            mario.y -= 0.15 * mario.velocity
        else:
            mario.y -= 0.3
        i+=0.1
        print(i)

        if i>10:
            mario.drop_state = False
            i=0


    



    

    # elif jump==1 and mario.jump_state ==False:
    #     mario.y-=0.5
    #     jump = 0






    #game drawing
    clear_canvas()
    stage1.draw()


    mario.draw()
    if monster ==True:
        gumba.draw()
        koopas.draw()
        redkoopas.draw()
        print("dd")


    # if mario.life==0:
    #     clear_canvas()
    #     gameover.draw
    #     update_canvas()
 

        

    update_canvas()

    # delay(0.05)


# finalization code
close_canvas()