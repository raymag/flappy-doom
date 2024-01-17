import pygame, sys
from bird import *
from pipe import *
from game_objects import *
from settings import *


class FlappyDoom:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Doom")
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.load_assets()
        self.sound = Sound()
        self.score = Score(self)
        self.new_game()

    def load_assets(self):
        icon = pygame.image.load("assets/bird/0.png").convert_alpha()
        pygame.display.set_icon(icon)
        # bird
        self.bird_images = [
            pygame.image.load(f"assets/bird/{i}.png").convert_alpha() for i in range(5)
        ]
        bird_image = self.bird_images[0]
        bird_size = (
            bird_image.get_width() * BIRD_SCALE,
            bird_image.get_height() * BIRD_SCALE,
        )
        self.bird_images = [
            pygame.transform.scale(sprite, bird_size) for sprite in self.bird_images
        ]
        # bird mask
        self.bird_mask_image = pygame.image.load("assets/bird/mask.png").convert_alpha()
        bird_mask_size = (
            bird_image.get_width() * BIRD_SCALE,
            bird_image.get_height() * BIRD_SCALE,
        )
        self.bird_mask_image = pygame.transform.scale(
            self.bird_mask_image, bird_mask_size
        )

        # background
        self.background_image = pygame.image.load("assets/images/bg.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, RES)
        # ground
        self.ground_image = pygame.image.load("assets/images/ground.png").convert()
        self.ground_image = pygame.transform.scale(
            self.ground_image, (WIDTH, GROUND_HEIGHT)
        )
        # pipes
        self.top_pipe_image = pygame.image.load(
            "assets/images/top_pipe.png"
        ).convert_alpha()
        self.top_pipe_image = pygame.transform.scale(
            self.top_pipe_image, (PIPE_WIDTH, PIPE_HEIGHT)
        )
        self.bottom_pipe_image = pygame.transform.flip(self.top_pipe_image, False, True)

    def new_game(self):
        self.all_sprites_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()
        self.bird = Bird(self)
        self.background = Background(self)
        self.ground = Ground(self)
        self.pipe_handler = PipeHandler(self)

    def draw(self):
        self.background.draw()
        self.all_sprites_group.draw(self.screen)
        self.ground.draw()
        self.score.draw()

        # self.bird.mask.to_surface(
        #     self.screen, unsetcolor=None, dest=self.bird.rect, setcolor="purple"
        # )
        pygame.display.flip()

    def update(self):
        self.background.update()
        self.all_sprites_group.update()
        self.ground.update()
        self.pipe_handler.update()
        self.clock.tick(FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.bird.check_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = FlappyDoom()
    game.run()
