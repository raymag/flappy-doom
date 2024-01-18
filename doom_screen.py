import pygame, sys
from settings import *
from doom_fire import *


class DoomScreen:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Doom Fire")
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.doom_fire = DoomFire(self)

    def draw(self):
        self.screen.fill("black")
        self.doom_fire.draw()

    def update(self):
        pygame.display.set_caption(f"Doom Fire - {self.clock.get_fps():.0f}fps")

        self.doom_fire.update()
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = DoomScreen()
    game.run()
