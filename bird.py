import pygame
from settings import *
from collections import deque


class Bird(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game.all_sprites_group)
        self.game = game
        self.image = game.bird_images[0]
        self.mask = pygame.mask.from_surface(game.bird_mask_image)
        self.rect = self.image.get_rect()
        self.rect.center = BIRD_POS

        self.images = deque(game.bird_images)
        self.animation_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.animation_event, BIRD_ANIMATION_TIME)

        self.falling_velocity = 0
        self.first_jump = True
        self.angle = 0

    def check_collision(self):
        hit = pygame.sprite.spritecollide(
            self,
            self.game.pipe_group,
            dokill=False,
            collided=pygame.sprite.collide_mask,
        )
        if (
            hit
            or self.rect.bottom > GROUND_Y
            or self.rect.top < -self.image.get_height()
        ):
            self.game.sound.hit_sound.play()
            pygame.time.wait(1000)
            self.game.new_game()

    def rotate(self):
        if not self.first_jump:
            if self.falling_velocity < -BIRD_JUMP_FORCE:
                self.angle = BIRD_JUMP_ANGLE
            else:
                self.angle = max(-2.5 * self.falling_velocity, -90)
            self.image = pygame.transform.rotate(self.image, self.angle)
            # new mask
            mask_image = pygame.transform.rotate(self.game.bird_mask_image, self.angle)
            self.mask = pygame.mask.from_surface(mask_image)

    def jump(self):
        self.game.sound.wing_sound.play()
        self.first_jump = False
        self.falling_velocity = BIRD_JUMP_FORCE

    def apply_gravity(self):
        if not self.first_jump:
            self.falling_velocity += GRAVITY
            self.rect.y += self.falling_velocity + 0.5 * GRAVITY

    def update(self):
        self.check_collision()
        self.apply_gravity()

    def animate(self):
        self.images.rotate(-1)
        self.image = self.images[0]

    def check_event(self, event):
        if event.type == self.animation_event:
            self.animate()
            self.rotate()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.jump()
