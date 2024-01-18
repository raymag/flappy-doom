# Game settings
import math


RES = WIDTH, HEIGHT = 1280, 900
FPS = 60
SCROLL_SPEED = 8

# Bird settings
BIRD_POS = WIDTH // 4, HEIGHT // 3
BIRD_SCALE = 1.1
BIRD_ANIMATION_TIME = 200
GRAVITY = 1
BIRD_JUMP_FORCE = -16
BIRD_JUMP_ANGLE = 20  # deg

# Ground settings
GROUND_HEIGHT = HEIGHT // 12
GROUND_Y = HEIGHT - GROUND_HEIGHT

# Pipe settings
PIPE_WIDTH = 250
PIPE_HEIGHT = HEIGHT
DIST_BETWEEN_PIPES = 650
GAP_HEIGHT = 300
HALF_GAP_HEIGHT = GAP_HEIGHT // 2

# Doom Fire settings
STEPS_BETWEEN_COLORS = 12  # 10
# COLORS = ["black", "red", "orange", "yellow", "white"]
COLORS = ["black", "darkorchid4", "blueviolet", "purple", "white"]
# COLORS = ["black", "chartreuse4", "chartreuse2", "chartreuse", "white"]
PIXEL_SIZE = 3  # 3
FIRE_REPETITIONS = 12
FIRE_WIDTH = math.ceil(WIDTH / (PIXEL_SIZE * FIRE_REPETITIONS))
FIRE_HEIGHT = HEIGHT // PIXEL_SIZE

# Behelit settings
BEHELIT_SCALE = 8
