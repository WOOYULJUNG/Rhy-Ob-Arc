import pygame, sys, random, time
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 900
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Rhy O')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

SPEED = 5000
firsttime1 = 0
firsttime2 = 0
first_constant1 = 1
first_constant2 = 1
while True:
    windowSurface.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:               
            if event.key == ord('z'):
                firsttime1 = time.time()
                print(firsttime1)
            if event.key == ord('/'):
                firsttime2 = time.time()
                print(firsttime2)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == ord('z'):
                fist_constant1 = 1
            if event.key == ord('/'):
                fist_constant2 = 1
    pygame.display.update()
    mainClock.tick(SPEED)
