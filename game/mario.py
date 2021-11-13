from pico2d import *
import game_world
import game_framework





# mario Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER,UP_DOWN,UP_UP = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,

}

# mario Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# mario Jump speed
JUMP_SPEED_KMPH = 20.0 # Km / Hour
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

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
        boy.timer = 1000

    def exit(boy, event):
        pass

    def do(boy):
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(202, 103, 30, 35, boy.x, boy.y,60,70)
        else:
            boy.image.clip_draw(173, 103, 30, 35, boy.x, boy.y,60,70)




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
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.timer -= 1
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(232 + 30*int(boy.frame), 103, 30, 35, boy.x, boy.y,60,70)
        else:
            boy.image.clip_draw(143 - 30*int(boy.frame), 103, 30, 35, boy.x, boy.y,60,70)



class JumpState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.jump_timer=0
        if event == UP_DOWN:
            boy.jump_timer += JUMP_SPEED_PPS


    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.timer -= 1
        boy.x += boy.velocity * game_framework.frame_time
        boy.y += boy.jump_timer * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)
        boy.fall = 0

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(352, 103, 30, 35, boy.x, boy.y,60,70)
        else:
            boy.image.clip_draw(22, 103, 30, 35, boy.x, boy.y,60,70)


class FallState:

    def enter(boy, event):
        boy.g -= JUMP_SPEED_PPS

        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
            
        boy.g=0


    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.timer -= 1
        boy.x += boy.velocity * game_framework.frame_time
        boy.y += boy.g * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(352, 103, 30, 35, boy.x, boy.y,60,70)
        else:
            boy.image.clip_draw(22, 103, 30, 35, boy.x, boy.y,60,70)



class SleepState:

    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(202, 103, 30, 35, boy.x, boy.y,60, 70)
        else:
            boy.image.clip_draw(173, 103, 30, 35, boy.x, boy.y,60, 70)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, UP_DOWN: JumpState, UP_UP:IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: JumpState, UP_UP: RunState },
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState, UP_DOWN: IdleState, UP_UP:IdleState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, UP_DOWN: JumpState, UP_UP:IdleState}
}


class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 100
        self.image = load_image('mario_sheet.png')


        self.dir = 1
        self.velocity = 0
        self.jump_timer = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.fall = 0

        self.g = 0

    def crush_box(self):
        return self.x-15, self.y-35, self.x + 15, self.y+35



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if(self.fall==1):
            self.y -= 1
        if(self.y > 500):
            self.y =10
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir) + '  State:' + str(self.cur_state))
        draw_rectangle(*self.crush_box())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

