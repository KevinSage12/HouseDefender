import pygame
from settings import *


class Level:
    def __init__(self):
        #get the display surface 
        self.display_surface = pygame.display.get_surface()

        #sprites setup
        self.visible_sprites = pygame.sprite.Group() 
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
       # update and draw the game
       pass