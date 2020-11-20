import pygame
from .tools import load_img

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 350
GAME_SPEED = 25
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 35


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = load_img('ground.fw.png')
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED
