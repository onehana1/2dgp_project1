from pico2d import *
import server



class S2_Ground1:
    def __init__(self):
        self.image = load_image('stage2_ground1.png')
        self.x=0
        self.y=0

        self.width = 2206
        self.height = 60
        self.bgm = load_music('sound/mario2.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()




    def update(self):        
        if server.mario_state == -1 or server.stage != 1:
            self.bgm.stop()
            print("ss")
        else:
            self.bgm.resume()


        # self.window_left = clamp(0, int(server.boy.x) - server.background.canvas_width // 2, server.background.w - server.background.canvas_width)
        # self.window_bottom = clamp(0, int(server.boy.y) - server.background.canvas_height // 2, server.background.h - server.background.canvas_height)
        self.crush_box()
    
        pass

    def crush_box(self):
        return self.x-self.width, self.y-self.height, self.x + self.width, self.y+self.height


    def draw(self):

        self.image.clip_draw_to_origin(0, 0 ,self.width, self.height, self.x, self.y)
       


        draw_rectangle(*self.crush_box())

