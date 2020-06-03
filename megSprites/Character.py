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
        self.sprite = self.graphics[self.direction][0]
        self.rect = self.sprite.get_rect()
