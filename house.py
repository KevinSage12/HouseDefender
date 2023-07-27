import pygame
from settings import *


class House:
    def __init__(self):
        #house caracteristics
        self.xhouse = (WIDTH / 2) - (SIZEHOUSEX/2) 
        self.yhouse = (HEIGTH / 2) - (SIZEHOUSEY/2) 
        self.rect = pygame.Rect(self.xhouse, self.yhouse,SIZEHOUSEX,SIZEHOUSEY)
        self.color = pygame.Color(250,150,60)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
