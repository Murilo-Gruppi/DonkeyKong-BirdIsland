import pygame

pygame.display.set_caption("Donkey Kong: Bird Island")
donkey_kong = pygame.image.load("images/donkey-kong.fw.png")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 350
GAME_SPEED = 10
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 35

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/ground.fw.png')
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/background.png")

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    screen.blit(BACKGROUND, (0, 0))
    screen.blit(donkey_kong, (20, 255))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(GROUND_WIDTH - 50)
        ground_group.add(new_ground)

    ground_group.update()
    ground_group.draw(screen)
    
    pygame.display.update()

pygame.quit()