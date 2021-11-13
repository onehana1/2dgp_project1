from pico2d import *

class Sky:
    def __init__(self):
        self.image = load_image('background_color1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800, 300,1600,600)
