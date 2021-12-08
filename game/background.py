import random
import server

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('s1_back.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.bgm = load_music('sound/mario.mp3')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()


    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background.canvas_width, server.background.canvas_height, 0, 0, server.background.canvas_width * 2, server.background.canvas_height )
        pass

    def update(self):
        # fill here
        

        if server.mario_star == 1:
            self.bgm.pause()
        else:
            self.bgm.resume()

        if server.mario_state == -1 or server.stage != 0 or server.mario_die == True :
            self.bgm.stop()

        self.window_left = clamp(0, int(server.boy.x) - server.background.canvas_width // 2, server.background.w - server.background.canvas_width)
        self.window_bottom = clamp(0, int(server.boy.y) - server.background.canvas_height // 2, server.background.h -server.background.canvas_height)

        pass

    def handle_event(self, event):
        pass







