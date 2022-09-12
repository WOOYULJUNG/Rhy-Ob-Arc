import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Rhy O')

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

SPEED = 50
Movespeed = SPEED/10
Once = True
player1_click = 0
player2_click = 0
player1box = []
player2box = []
player1 = []
player2 = []

size1=open('size.txt',"r")
for line in size1:
    sizelist = line.split()
height1=open('height.txt','r')
for line in height1:
    heightlist = line.split()

class box1:
    def __init__(self):
        self.height = 0
        self.right = WINDOWWIDTH/8
        self.size = 0
        self.bottom = WINDOWHEIGHT

class box2:
    def __init__(self):
        self.height = 0
        self.left = WINDOWWIDTH/8*7
        self.size = 0
        self.bottom = WINDOWHEIGHT
        
def event():
    global player1_click
    global player2_click
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:               
            if event.key == ord('z') :
                player1_click = True
            if event.key == ord('0') :
                player2_click = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()

def makebox():
    global sizelist
    global player1box
    global player1
    global player2box
    global player2
    global sizelist
    global heightlist
    for i in range(len(sizelist)):
        BOX=box1()
        player1box.append(BOX)
        player1box[i].height = heightlist[i]  
        player1box[i].size = sizelist[i]
        if i > 0:
            player1box[i].bottom = player1box[i-1].bottom - int(player1box[i-1].size)
    for i in range(len(sizelist)):
        BOX=box2()
        player2box.append(BOX)
        player2box[i].height = heightlist[i]  
        player2box[i].size = sizelist[i]
        if i > 0:
            player2box[i].bottom = player2box[i-1].bottom - int(player2box[i-1].size) 

def appendbox():
    global sizelist
    global player1box
    global player1
    global player2
    global player2box
    player1 = []
    player2 = []
    for i in range(len(sizelist)):
        player1.append(pygame.Rect(player1box[i].right - int(player1box[i].height), player1box[i].bottom - int(player1box[i].size), int(player1box[i].height), int(player1box[i].size)))
        player2.append(pygame.Rect(player2box[i].left, player2box[i].bottom - int(player2box[i].size), int(player2box[i].height), int(player2box[i].size)))

\

def movebox():
    global Movespeed
    global sizelist
    global player1box
    global player2box
    for i in range(len(sizelist)):
        player1box[i].bottom += Movespeed
        player2box[i].bottom += Movespeed

def drawbox():
    global player1box
    global player1
    global player2
    for i in range(len(player1box)):
        pygame.draw.rect(windowSurface, WHITE, player1[i])
        pygame.draw.rect(windowSurface, WHITE, player2[i])
                
while True:
    windowSurface.fill(BLACK)
    event()
    while Once:
        makebox()
        Once = False
    appendbox()
    drawbox()
    #movebox()
    pygame.display.update()
    mainClock.tick(SPEED)
