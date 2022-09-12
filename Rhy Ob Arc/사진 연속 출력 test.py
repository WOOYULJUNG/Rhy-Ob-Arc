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
YELLOW = (255, 255, 0)

Image = []
ok = False
picx = [[]for row in range(5)]
picy = [[]for row in range(5)]
pic = [[]for row in range(5)]
picture=[]

for num in range(4):
    picture.append(open('6.%d.txt'%(num),"r"))
    for line in picture[num]:
        pictur = line.split(',')
        for word in pictur:
            pic[num].append(int(word))
    longg = len(pic[num]) 
    picy[num] = pic[num][(longg)//2:]
    picx[num] = pic[num][:(longg)//2]

SPEED = 500
onc = 1
i=0
j=1

def printpicture(num):
    num=num//100
    for i in range(len(picx[num])):
        pygame.draw.circle(windowSurface, YELLOW, (picx[num][i], picy[num][i]), 2, 0)
        if i == len(picx[num])-1 and ok:
            pygame.draw.line(windowSurface, GREEN, (picx[num][i], picy[num][i]), (picx[num][0], picy[num][0]), 2)
        if i > 0:
            pygame.draw.line(windowSurface, GREEN, (picx[num][i], picy[num][i]), (picx[num][i-1], picy[num][i-1]), 2)

while True:
    windowSurface.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    while onc:
        printpicture(i)
        onc = 0
        i += 2*j
        if i == 398 or i==0:
            j=j*(-1)
    onc = 1
    pygame.display.update()
    mainClock.tick(SPEED)
    
''' 박자 맞춰서 애들 색깔 바뀌게'''
