import pygame
import random
from settings import *


class TopPipe(pygame.sprite.Sprite):
    def __init__(self, app, gap_y_pos):
        super().__init__(app.pipe_group, app.all_sprites_group)
        self.image = app.top_pipe_image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = WIDTH, gap_y_pos - HALF_GAP_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect.left -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()


class BottomPipe(TopPipe):
    def __init__(self, app, gap_y_pos):
        super().__init__(app, gap_y_pos)
        self.image = app.bottom_pipe_image
        self.rect = self.image.get_rect()
        self.rect.topleft = WIDTH, gap_y_pos + HALF_GAP_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect.left -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()


class PipeHandler:
    def __init__(self, game):
        self.game = game
        self.pipe_dist = DIST_BETWEEN_PIPES

    def update(self):
        self.generate_pipes()

    @staticmethod
    def get_gap_y_position():
        return random.randint(GAP_HEIGHT, HEIGHT - GAP_HEIGHT)

    def generate_pipes(self):
        if self.game.bird.first_jump:
            return
        self.pipe_dist += SCROLL_SPEED
        if self.pipe_dist > DIST_BETWEEN_PIPES:
            self.pipe_dist = 0
            gap_y = self.get_gap_y_position()

            TopPipe(self.game, gap_y)
            BottomPipe(self.game, gap_y)
