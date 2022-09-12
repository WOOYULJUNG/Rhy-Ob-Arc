import pygame, sys, random
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
print(len(sizelist))
height1=open('height.txt','r')
for line in height1:
    heightlist = line.split()
print(len(heightlist))
red1=open('red.txt','r')
for line in red1:
    redlist = line.split()
green1=open('green.txt','r')
for line in green1:
    greenlist = line.split()
blue1=open('blue.txt','r')
for line in blue1:
    bluelist = line.split()
    
class box1:
    def __init__(self):
        self.height = 0
        self.right = WINDOWWIDTH/6
        self.size = 0
        self.bottom = WINDOWHEIGHT
        self.red = 0
        self.blue = 0
        self.green = 0

class box2:
    def __init__(self):
        self.height = 0
        self.left = WINDOWWIDTH/6*5
        self.size = 0
        self.bottom = WINDOWHEIGHT
        self.red = 0
        self.blue = 0
        self.green = 0
        
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
        player1box[i].height = int(heightlist[i])
        player1box[i].size = sizelist[i]
        if int(player1box[i].height) >= 50 and int(player1box[i].height) <= 150:
            player1box[i].red = redlist[int(heightlist[i])//10%10]
            player1box[i].green = greenlist[int(heightlist[i])//10%10]
            player1box[i].blue = bluelist[int(heightlist[i])//10%10]
            print(1)
        if i > 0:
            player1box[i].bottom = player1box[i-1].bottom - int(player1box[i-1].size)
    for i in range(len(sizelist)):
        BOX=box2()
        player2box.append(BOX)
        player2box[i].height = int(heightlist[i])
        player2box[i].size = sizelist[i]
        if int(player2box[i].height) >= 50 and int(player2box[i].height) <= 150:
            player2box[i].red = redlist[int(heightlist[i])//10%10]
            player2box[i].green = greenlist[int(heightlist[i])//10%10]
            player2box[i].blue = bluelist[int(heightlist[i])//10%10]
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

def movebox():
    global Movespeed
    global sizelist
    global player1box
    global player2box
    for i in range(len(sizelist)):
        player1box[i].bottom += Movespeed
        player2box[i].bottom += Movespeed

def drawbox():
    global windowSurface
    global player1box
    global player2box
    global player1
    global player2
    for i in range(len(player1box)):
        pygame.draw.rect(windowSurface, (int(player1box[i].red), int(player1box[i].green), int(player1box[i].blue)), player1[i])
        pygame.draw.rect(windowSurface, (int(player2box[i].red), int(player2box[i].green), int(player2box[i].blue)), player2[i])
                
while True:
    windowSurface.fill(BLACK)
    event()
    while Once:
        makebox()
        Once = False
    appendbox()
    drawbox()
    movebox()
    pygame.display.update()
    mainClock.tick(SPEED)
