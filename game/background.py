import random
import server

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('stage1_background.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h


    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background.canvas_width, server.background.canvas_height, 0, 0, server.background.canvas_width * 2, server.background.canvas_height )
        pass

    def update(self):
        # fill here
        self.window_left = clamp(0, int(server.boy.x) - server.background.canvas_width // 2, server.background.w - server.background.canvas_width)
        self.window_bottom = clamp(0, int(server.boy.y) - server.background.canvas_height // 2, server.background.h -server.background.canvas_height)

        pass

    def handle_event(self, event):
        pass







