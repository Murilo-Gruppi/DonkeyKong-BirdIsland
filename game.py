import pygame
pygame.init()

screen = pygame.display.set_mode((800, 350))
pygame.display.set_caption("Donkey Kong: Bird Island")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
