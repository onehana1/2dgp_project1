import random
import server

from pico2d import *


class Fixedbackground:

    def __init__(self):
        self.image = load_image('s1_back.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h


    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background2.canvas_width, server.background2.canvas_height, 0, 0, server.background2.canvas_width * 2, server.background2.canvas_height )
        pass

    def update(self):
        # fill here
        self.window_left = clamp(0, int(server.boy.x) - server.background2.canvas_width // 2, server.background2.w - server.background2.canvas_width)
        self.window_bottom = clamp(0, int(server.boy.y) - server.background2.canvas_height // 2, server.background2.h -server.background2.canvas_height)

        pass

    def handle_event(self, event):
        pass







