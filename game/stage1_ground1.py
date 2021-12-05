from pico2d import *
import server



class S1_Ground1:
    def __init__(self):
        self.image = load_image('stage1_ground1.png')
        self.x=0
        self.y=0

        self.width = 2206
        self.height = 60



    def update(self):        

        # self.window_left = clamp(0, int(server.boy.x) - server.background.canvas_width // 2, server.background.w - server.background.canvas_width)
        # self.window_bottom = clamp(0, int(server.boy.y) - server.background.canvas_height // 2, server.background.h - server.background.canvas_height)
        self.crush_box()
    
        pass

    def crush_box(self):
        # return (self.x - server.boy.x), self.y, self.width- server.boy.x, self.height
        return self.x-self.width- server.boy.x, self.y-self.height, self.x + self.width- server.boy.x, self.y+self.height


    def draw(self):
        # self.image.draw(self.x, self.y ,2206,60)

        self.image.clip_draw_to_origin(0, 0 ,self.width, self.height, self.x - server.boy.x, self.y)
        # self.image.clip_draw_to_origin(self.window_left, self.window_bottom ,self.width, self.height, 0, 0)
        # self.image.draw(self.x -server.boy.x, self.y ,self.width ,self.height)
        # self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background.canvas_width, server.background.canvas_height, 0, 0)
        pass


        draw_rectangle(*self.crush_box())

