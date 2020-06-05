import pygame
import sys
from pygame.locals import *
from random import randint
from Products import *
import time
import Character
from Director import *
from Builder import *
from Character import *
import loadImages


class Juego():
    
    i=0
    width = 900
    height = 600
    colour = (227,166,162)
    empezar = True
    megaman = rightMegaman()
    auxlist = megaman.get_sprites()
    

    pygame.init()                
    posX=100
    posY=250
    posTup = (posX,posY)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Prueba")
    speed=20
    auxDirector = Director()
    auxDirector.setBuilder(GokuBuilder())
    charac= auxDirector.getChar()
    charac.defPositions(posX,posY)
    jugando =True
    background = loadImages.load("background/mexBack.jpeg")
    
    while empezar:
        
        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
                empezar = False
                sys.exit()
        #screen.fill(colour)
        #if jugando:
        screen.blit(background,(0,0))
        charac.update()
        charac.drawCharacter(screen)
        pygame.display.update()
        
        """elif i.type == pygame.KEYDOWN:
                if i.key==K_LEFT:
                    megaman = leftMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0, 7):
                        if i==6:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posX-= speed
                            pygame.display.update()
                            time.sleep(0.1)
                        else:
                            screen.fill(colour)
                            screen.blit(auxlist[i], (posX, posY))
                            posX -= speed
                            pygame.display.update()
                            time.sleep(0.1)

                elif i.key==K_RIGHT:
                    megaman = rightMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,7):
                        if i==6:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posX-= speed
                            pygame.display.update()
                            time.sleep(0.1)
                        else:
                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))
                            posX += speed
                            pygame.display.update()
                            time.sleep(0.1)
                elif i.key==K_UP:
                    megaman = upMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,3):
                        if i==3:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posY-= speed
                            pygame.display.update()
                            time.sleep(0.1)
                        else:

                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))
                            posY -= speed
                            pygame.display.update()
                            time.sleep(0.1)
                elif i.key==K_DOWN:
                    megaman = downMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,2):
                        if i==2:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))
                            posY+= speed
                            pygame.display.update()
                            time.sleep(0.15)
                        else:

                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))
                            posY += speed
                            pygame.display.update()
                            time.sleep(0.15)
                elif i.key==K_SPACE:
                    megaman = spaceMegaman()
                    auxlist = megaman.get_sprites()
                    for i in range(0,3):
                        if i==3:
                            screen.fill(colour)
                            screen.blit(auxlist[0], (posX, posY))

                            pygame.display.update()
                            time.sleep(0.2)
                        else:

                            screen.fill(colour)
                            screen.blit(auxlist[i],(posX, posY))

                            pygame.display.update()
                            time.sleep(0.2)"""   
        
        
        




