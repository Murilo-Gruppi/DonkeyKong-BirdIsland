import pygame
from . import tools
from .game import game


def menu(screen):
    pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    class Main_Menu:
        def __init__(self):
            self.press = tools.load_img('press.png')
            self.background = tools.load_img("menu.png")
            self.verify = 1

        def update(self):
            if self.verify:
                screen.blit(self.press, (130, 300))
                self.verify = 0
            else:
                self.verify = 1

        def draw(self):
            screen.blit(self.background, (0, 0))

    pygame.display.set_caption('Donkey Kong: Bird Island')

    # Plays music
    volume = 0.3
    tools.play_music('music_menu.wav', volume)
    menu = Main_Menu()
    running = True

    while running:
        pygame.time.delay(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.stop()
                screen.fill((0, 0, 0))
                pygame.display.update()
                pygame.time.wait(400)
                game(screen)

        menu.draw()
        menu.update()

        pygame.display.update()

    pygame.quit()