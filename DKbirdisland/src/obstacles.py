import pygame
from random import randrange
from .tools import load_img

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 350
GROUND_HEIGHT = 35
GAME_SPEED = 25

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.images = [load_img('snake1.png').convert_alpha(),
                        load_img('barris.png').convert_alpha()]

        range = randrange(0, 2)

        self.image = self.images[range]
        if range == 0:
            self.image = pygame.transform.scale(self.image, (40, 70))
        elif range == 1:
            self.image = pygame.transform.scale(self.image, (73, 70))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT - 70

    def update(self):
        self.rect[0] -= GAME_SPEED