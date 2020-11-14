import pygame
pygame.init()

screen = pygame.display.set_mode((800, 350))
pygame.display.set_caption("Donkey Kong: Bird Island")
background = pygame.image.load("images/background.png")
ground = pygame.image.load("images/ground.fw.png")
donkey_kong = pygame.image.load("images/donkey-kong.fw.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(ground, (0, 315))
    screen.blit(donkey_kong, (20, 255))
    pygame.display.update()

pygame.quit()