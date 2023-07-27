#imports_____________________________________________________
import pygame, sys
from settings import *
from level import Level
from players import Player
from house import House
from collision import Collision

#____________________________________________________________

class Game:
    def __init__(self):
        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Arena Fighting Game')
        self.level = Level() # instance level créée
        self.player = Player(0,0)
        self.house = House()
        self.collision = Collision(0,0)
        self.dirplayerx = True
        self.dirplayery = True

    def run(self):

        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

# ZQSD déplacement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        self.player.up_pressed = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.down_pressed = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        self.player.left_pressed = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.right_pressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        self.player.up_pressed = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.down_pressed = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        self.player.left_pressed = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.right_pressed = False
#_________________________________________________________________________________

            self.screen.fill('black')
            
            self.dirplayerx,self.dirplayery = self.player.move()
            self.player.x,self.player.y = self.collision.out(PLAYERSPEED,self.player.x,self.player.y)
          #  self.player.x,self.player.y = self.collision.maison(PLAYERSPEED,self.player.x,self.player.y, self.dirplayerx,self.dirplayery)

# Affichage joueur
            self.player.update()
            self.player.draw(self.screen)

# Affichage maison
            self.house.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)
            self.level.run() # Ajoute 1 instance level dans la boucle while
            

if __name__ == '__main__':
    game = Game()
    game.run()