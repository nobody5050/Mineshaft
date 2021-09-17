import pygame
import pygame_menu
from resources.colors import *
from resources.constants import *



class Mineshaft(object):
    def __init__(self):
        self._pygame_init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self._menu_init(WIDTH, HEIGHT)


    def _pygame_init(self):
        pygame.init()
        pygame.display.set_caption("Mineshaft", "Mineshaft")
        #pygame.mouse.set_visible(False)

    def _menu_init(self, width, height):
        self.menu = pygame_menu.Menu("Mineshaft", width-100, height-100)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def update_game(self):

        events = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self._menu_init(event.w, event.h)
            elif event.type==pygame.QUIT:
                pygame.quit()


        if self.menu.is_enabled():
            self.menu.update(events)



    def draw_game(self):

        self.screen.fill(WHITE)

        if self.menu.is_enabled():
            self.menu.draw(self.screen)


        pygame.display.flip()

        self.clock.tick(60)





game = Mineshaft()


while True:
    game.update_game()
    game.draw_game()
