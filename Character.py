import pygame
from pygame.sprite import Sprite
from pygame import*


class Character(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.direction = 0
        self.cont = 0
        self.speed = 20

    def set_sprites(self, images):
        self.graphics = images
        #self.sprite = self.graphics[self.direction][0]
        #self.rect = self.sprite.get_rect()
        

    def udpate(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_RIGHT]:
            self.direction = 0
            print("derecha")
        elif pressed[K_LEFT]:
            self.direction = 1
        elif pressed[K_UP]:
            self.direction = 2
        elif pressed[K_DOWN]:
            self.direction = 3
        elif pressed[K_SPACE]:
            self.direction = 4
        if pressed[K_RIGHT] or pressed[K_LEFT] or pressed[K_UP] or pressed[K_DOWN] or pressed[K_SPACE]:
            self.sprite = self.graphics [self.direction][self.cont]
            self.cont+=1 
            self.cont %=7


    def drawCharacter(self,screen,posTup):
        self.defaultImage = self.graphics[1][0]
        screen.blit(self.defaultImage ,posTup)
