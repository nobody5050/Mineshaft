import pygame

class WorldLayerGroup(pygame.sprite.Group):
    def __init__(self, gid=None):
        self.gid = gid
