import pygame

pygame.display.set_caption("Donkey Kong: Bird Island")
donkey_kong = pygame.image.load("images/original.png")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 350
GAME_SPEED = 10
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 35
MIN_HEIGHT = 255
SPEED_JUMP = 50
GRAVITY = 10


class Donkey(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('images/animations/Andar (1).png').convert_alpha(),
                      pygame.image.load('images/animations/Andar (2).png').convert_alpha(),
                      pygame.image.load('images/animations/Andar (3).png').convert_alpha(),
                      pygame.image.load('images/animations/Andar (4).png').convert_alpha(),
                      pygame.image.load('images/animations/Andar (5).png').convert_alpha(),
                      pygame.image.load('images/animations/Andar (6).png').convert_alpha()]

        self.speed = SPEED_JUMP

        self.current_image = 0
        self.image = pygame.image.load('images/original.png').convert_alpha()        
        self.rect = self.image.get_rect()
        self.rect[0] = 20
        self.rect[1] = 255

    def update(self):
        self.current_image = (self.current_image + 1) % 6
        self.image = self.images[self.current_image]

        self.speed += GRAVITY       
        self.rect[1] += self.speed

        if self.rect[1] > 255:
            self.rect[1] = 255
            self.speed = 0      
    
    def jump(self):
        self.speed = -SPEED_JUMP 
       

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

donkey_group = pygame.sprite.Group()
donkey = Donkey()
donkey_group.add(donkey)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

clock = pygame.time.Clock()


# Principal
count_jump = 0
running = True
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if count_jump < 2:
                    donkey.jump()
                    count_jump += 1
                else:
                    count_jump = 0
                
    screen.blit(BACKGROUND, (0, 0))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(GROUND_WIDTH - 50)
        ground_group.add(new_ground)

    donkey_group.update()
    donkey_group.draw(screen)
    ground_group.update()
    ground_group.draw(screen)
    
    pygame.display.update()

pygame.quit()