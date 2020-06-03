import pygame
import sys
from pygame.locals import *
from random import randint
from Products import *


class Juego():
    
    i=0
    width = 900
    height = 800
    colour = (227,166,162)
    empezar = True
    megaman = rightMegaman()
    auxlist = megaman.get_sprites()
    
    

    pygame.init()
    posX=100
    posY=400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Prueba")
    clock = pygame.time.Clock()
    
    while empezar:
        screen.fill(colour)
        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
                empezar = False
                sys.exit()
                
        
        for i in range(0,5):
            screen.blit(auxlist[i],(posX,posY))
            posX=posX+100
            
        pygame.display.update()
        




