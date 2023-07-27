import pygame
from settings import *
from players import Player
from house import House

class Collision:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.house = House()

    def out(self,PLAYERSPEED,xplayer,yplayer):
        if (xplayer > WIDTH - SIZEPLAYERX):
            xplayer = xplayer - PLAYERSPEED
        if (xplayer < 0):
            xplayer = xplayer + PLAYERSPEED
        if (yplayer > HEIGTH - SIZEPLAYERY):
            yplayer = yplayer - PLAYERSPEED
        if (yplayer < 0):
            yplayer = yplayer + PLAYERSPEED
        return xplayer , yplayer
    
    # def maison(self,PLAYERSPEED,xplayer,yplayer,dirx,diry):
    #     if (xplayer > int (self.house.xhouse - SIZEPLAYERX) & xplayer < int (self.house.xhouse + SIZEHOUSEX - SIZEPLAYERX)):
    #         if dirx == True:
    #             xplayer = xplayer - PLAYERSPEED
    #         if dirx == False:
    #             xplayer = xplayer + PLAYERSPEED
    #     if (yplayer > int (self.house.yhouse - SIZEPLAYERY) & yplayer < int (self.house.yhouse + SIZEHOUSEY - SIZEPLAYERY)):
    #         if diry == True:
    #             yplayer = yplayer - PLAYERSPEED
    #         if diry == False:
    #             yplayer = yplayer + PLAYERSPEED
    #     return xplayer , yplayer
    
    # def ingame(self,speed):
    #     colliDXH, colliDXL, colliDYH, colliDYL = False, False, False, False
    #     if (self.x > WIDTH - SIZEPLAYERX):
    #         colliDXH = True
    #         self.x = self.x - speed
    #     if (self.x < 0):
    #         colliDXL = True
    #         self.x = self.x + speed
    #     if (self.y > HEIGTH - SIZEPLAYERY):
    #         colliDYH = True
    #         self.y = self.y - speed
    #     if (self.y < 0):
    #         colliDYL = True
    #         self.y = self.y + speed
    #     return colliDXH,colliDYH,colliDXL, colliDYL