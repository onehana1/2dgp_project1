import game_framework
import pico2d
import next_stage
import die_state

# import main_state
import world_build_state as start_state

pico2d.open_canvas(1600, 600)
# game_framework.run(start_state)
game_framework.run(next_stage)

pico2d.close_canvas()  