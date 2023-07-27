import pygame
from settings import *

class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,SIZEPLAYERX,SIZEPLAYERY)
        self.x = x
        self.y = y
        self.color = pygame.Color(250,150,60)
        self.dx = 0
        self.dy = 0
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.speed = PLAYERSPEED
        self.dirx = True
        self.diry = True


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
    def move(self):
        self.dx = 0
        self.dy = 0
# déplacement direction Gauche
        if self.left_pressed and not self.right_pressed:
            self.dx = -self.speed
            self.dirx = False
# déplacement direction Droite
        if self.right_pressed and not self.left_pressed:
            self.dx = self.speed
            self.dirx = True
# déplacement direction Haut
        if self.up_pressed and not self.down_pressed:
            self.dy = -self.speed
            self.dirx = False
# déplacement direction Bas
        if self.down_pressed and not self.up_pressed:
            self.dy = self.speed
            self.dirx = True
        self.x += self.dx
        self.y += self.dy
        return self.dirx,self.diry
        
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, SIZEPLAYERX, SIZEPLAYERY)
        return self.x , self.y

 