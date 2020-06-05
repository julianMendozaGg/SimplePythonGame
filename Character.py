import pygame
from pygame.sprite import Sprite
from pygame import*
import time


class Character(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.direction = 1
        self.cont = 0
        self.speed = 20
        self.movementLeft = True
        self.movementRight = True

    def defPositions(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY

    def set_sprites(self, images):
        self.graphics = images
        self.image = self.graphics[self.direction][self.cont]
        #self.rect = self.sprite.get_rect()

    def update(self):
        #self.image= self.graphics [1][0]
        pressed = pygame.key.get_pressed()

        if pressed[K_SPACE]:
            self.direction = 4
            time.sleep(0.2)

        if self.movementLeft:
            if pressed[K_LEFT]:
                self.posX -= self.speed
                time.sleep(0.08)
                self.direction = 0
        if self.movementRight:
            if pressed[K_RIGHT]:
                self.posX += self.speed
                time.sleep(0.08)
                self.direction = 1

                """elif pressed[K_UP]:
            self.direction = 2
            for i in range(0,3):
                self.posY -= self.speed
                self.image = self.graphics[self.direction][i]
                print("me voy de la casa si esto no funiona xdd :(")
                time.sleep(0.3)
        elif pressed[K_DOWN]:
            self.posY += self.speed
            self.direction = 3
            time.sleep(0.08)"""

        
        if pressed[K_RIGHT] or pressed[K_LEFT] or pressed[K_SPACE]:
            self.image = self.graphics[self.direction][self.cont]
            self.cont += 1
            self.cont %= len(self.graphics[self.direction])

            if self.posX < 0:
                self.movementLeft = False
            else:
                self.movementLeft = True
            if self.posX > 600:
                self.movementRight = False
            else:
                self.movementRight = True
        else:
            self.cont = 0
            self.image = self.graphics[self.direction][0]

    def drawCharacter(self, screen):
        screen.blit(self.image, (self.posX, self.posY))
