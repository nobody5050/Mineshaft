import pygame
import screeninfo
import os
import random
import screeninfo
import pygame_menu
from resources.colors import *
from resources.constants import *
from resources.themes import *



class Mineshaft(object):
    def __init__(self):
        self._pygame_init()
<<<<<<< HEAD
        self.currentpanoramapos = [random.randint(-1000, 0),random.randint(-500, 0)]
        self.panorama_x_direction = random.randint(0,1)
        self.panorama_y_direction = random.randint(0,1)
=======
        self.currentpanoramapos = (random.randint(-1000, 0),random.randint(-500, 0))
        self.panorama_direction = random.randint(0,1)
>>>>>>> 8bf6f3c7992aabb890f745c957adf0cb2cd08796
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self._menu_init(WIDTH, HEIGHT)


    def _pygame_init(self):
        pygame.init()
        pygame.display.set_caption("Mineshaft", "Mineshaft")
        pygame.mouse.set_visible(False)

    def _menu_init(self, width, height):
        self.menu = pygame_menu.Menu("Mineshaft", width-100, height-100, theme=MINESHAFT_DEFAULT_THEME)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        monitor = screeninfo.get_monitors()[0]

        self.menu.background = pygame.image.load(os.path.join(os.path.abspath(os.getcwd()), "assets", "panorama.jpeg"))
        self.menu.background = pygame.transform.scale(self.menu.background, (monitor.width, monitor.height))

    def _update_panorama(self, currentpos):
        if currentpos[0]==0:
<<<<<<< HEAD
            self.panorama_x_direction = 1

        elif currentpos[0]==-1000:
            self.panorama_x_direction = 0

        if currentpos[1]==0:
            self.panorama_y_direction = 1

        elif currentpos[1]==-500:
            self.panorama_y_direction = 0

        if self.panorama_x_direction == 0:
            currentpos[0]+=1

        elif self.panorama_x_direction == 1:
            currentpos[0]-=1

        if self.panorama_y_direction == 0:
            currentpos[1]+=1

        elif self.panorama_y_direction == 1:
            currentpos[1]-=1

        return currentpos

=======
            self.panorama_direction = 1

        elif currentpos[0]==-1000:
            self.panorama_direction = 0

        if self.panorama_direction == 0:
            return (currentpos[0]+1, currentpos[1])

        elif self.panorama_direction == 1:
            return (currentpos[0]-1, currentpos[1])
>>>>>>> 8bf6f3c7992aabb890f745c957adf0cb2cd08796



    def update_game(self):

        events = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self._menu_init(event.w, event.h)
            elif event.type==pygame.QUIT:
                pygame.quit()


        if self.menu.is_enabled():
            self.currentpanoramapos = self._update_panorama(self.currentpanoramapos)
            self.menu.update(events)




    def draw_game(self):

        self.screen.fill(WHITE)


        if self.menu.is_enabled():
            self.screen.blit(self.menu.background, self.currentpanoramapos)
            self.menu.draw(self.screen)



        pygame.display.flip()

        self.clock.tick(60)





game = Mineshaft()


while True:
    game.update_game()
    game.draw_game()
