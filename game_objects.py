import pygame
from settings import *


class Sound:
    def __init__(self):
        self.hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
        self.point_sound = pygame.mixer.Sound("assets/sound/point.wav")
        self.wing_sound = pygame.mixer.Sound("assets/sound/wing.wav")


class Background:
    def __init__(self, game):
        self.game = game
        self.x = 0
        self.y = 0
        self.speed = SCROLL_SPEED - 2
        self.image = self.game.background_image

    def update(self):
        self.x = (self.x - self.speed) % -WIDTH

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))
        self.game.screen.blit(self.image, (WIDTH + self.x, self.y))


class Ground(Background):
    def __init__(self, game):
        super().__init__(game)
        self.y = GROUND_Y
        self.speed = SCROLL_SPEED
        self.image = self.game.ground_image
