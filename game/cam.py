#cam추가

from pico2d import *

from mario import Boy
import game_framework
import game_world

boy = None

class Camera:
    

    def __init__(self):
        global boy
        self.x = 3
        self.y = 0
        boy = Boy()
        
    
    def cam(self):
        self.x = 3
        print(self.x)
