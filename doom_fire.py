import pygame
from pygame import gfxdraw
from random import randint
from settings import *


class DoomFire:
    def __init__(self, game):
        self.game = game
        self.pallete = self.get_pallete()
        self.fire_array = self.get_fire_array()
        self.fire_surf = pygame.Surface((PIXEL_SIZE * FIRE_WIDTH, HEIGHT))
        self.fire_surf.set_colorkey("black")
        self.theme_sound = pygame.mixer.Sound("assets/sound/theme.mp3")
        self.theme_sound.set_volume(0.1)

        self.behelit_risen = False
        self.behelit_image = pygame.image.load(
            "assets/images/behelit2.png"
        ).convert_alpha()
        behelit_size = (
            self.behelit_image.get_width() * BEHELIT_SCALE,
            self.behelit_image.get_height() * BEHELIT_SCALE,
        )

        self.behelit_image = pygame.transform.scale(self.behelit_image, behelit_size)
        self.behelit_pos = [(WIDTH // 2) - self.behelit_image.get_width() // 2, HEIGHT]

    def rise_behelit(self):
        self.behelit_pos[1] -= 5
        if self.behelit_pos[1] <= (HEIGHT // 2) - (
            self.behelit_image.get_height() // 1.75
        ):
            self.behelit_risen = True
            self.theme_sound.play()

    def draw_behelit(self):
        self.game.screen.blit(
            self.behelit_image, (self.behelit_pos[0], self.behelit_pos[1])
        )
        # pygame.draw.rect(self.behelit_image, "yellow", self.behelit_image.get_rect(), 4)

    def do_fire(self):
        for x in range(FIRE_WIDTH):
            for y in range(1, FIRE_HEIGHT):
                color_index = self.fire_array[y][x]
                if color_index:
                    # BEST
                    rnd = randint(0, 3)
                    self.fire_array[y - 1][(x - rnd + 1) % FIRE_WIDTH] = (
                        color_index - rnd % 2
                    )

                    # SECOND
                    # rnd = randint(0, 1)
                    # self.fire_array[y - 1][x] = color_index - rnd

                    # THIRD
                    # self.fire_array[y - 1][x] = color_index - 1
                else:
                    self.fire_array[y - 1][x] = 0

    def draw_fire(self):
        self.fire_surf.fill("black")
        for y, row in enumerate(self.fire_array):
            for x, color_index in enumerate(row):
                if color_index:
                    color = self.pallete[color_index]
                    gfxdraw.box(
                        self.fire_surf,
                        (
                            x * PIXEL_SIZE,
                            y * PIXEL_SIZE,
                            PIXEL_SIZE,
                            PIXEL_SIZE,
                        ),
                        color,
                    )
        for i in range(FIRE_REPETITIONS):
            # pygame.draw.rect(self.game.screen, "green", self.fire_surf.get_rect(), 4)
            self.game.screen.blit(self.fire_surf, (i * FIRE_WIDTH * PIXEL_SIZE, 0))

    def get_fire_array(self):
        fire_array = [[0 for i in range(FIRE_WIDTH)] for j in range(FIRE_HEIGHT)]
        for i in range(FIRE_WIDTH):
            fire_array[FIRE_HEIGHT - 1][i] = len(self.pallete) - 1
        return fire_array

    def draw_pallete(self):
        size = 45
        for i, color in enumerate(self.pallete):
            pygame.draw.rect(
                self.game.screen, color, (i * size, HEIGHT // 2, size - 5, size - 5)
            )

    @staticmethod
    def get_pallete():
        pallete = [(0, 0, 0)]
        for i, color in enumerate(COLORS[:-1]):
            c1, c2 = color, COLORS[i + 1]
            for step in range(STEPS_BETWEEN_COLORS):
                c = pygame.Color(c1).lerp(c2, (step + 0.5) / STEPS_BETWEEN_COLORS)
                pallete.append(c)
        return pallete

    def update(self):
        self.do_fire()
        # if not self.behelit_risen:
        #     self.rise_behelit()

    def draw(self):
        # self.draw_pallete()
        # self.draw_behelit()
        self.draw_fire()
