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

SPEED = 500
Movespeed = 1200/SPEED
Once = True
player1_click = False
player2_click = False
player1box = []
player2box = []
player1 = []
player2 = []
top1line=[]
mid1line=[]
bot1line=[]
top2line=[]
mid2line=[]
bot2line=[]
timebox1 = []
timebox2 = []
firsttime1 = 0
firsttime2 = 0
lasttime = 0
first_constant1 = 1
first_constant2 = 1
lastclickupdate1 = 0
lastclickupdate2 = 0
lasttimeupdate = 0
player1boxnumber = 1
player2boxnumber = 1
timeboxnumber = 1
oncemeet = 1
onceclick1 = 0
onceclick2 = 0

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
    global first_constant1
    global first_constant2
    global firsttime1
    global firsttime2
    global onceclick1
    global onceclick2
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:               
            if event.key == ord('z'):
                player1_click = True
                onceclick1 = 1
                while first_constant1:
                    firsttime1 = time.time()
                    first_constant1 = 0
            if event.key == ord('/'):
                player2_click = True
                onceclick2 = 1
                while first_constant2:
                    firsttime2 = time.time()
                    first_constant2 = 0
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == ord('z'):
                player1_click = False
                first_constant1 = 1
                onceclick1 = 1
            if event.key == ord('/'):
                player2_click = False
                first_constant2 = 1
                onceclick2 =1 

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

def drawline():
    global player1_click
    global player2_click
    global windowSurface
    global top1line
    global mid1line
    global bot1line
    global top2line
    global mid2line
    global bot2line
    top1line=[]
    mid1line=[]
    bot1line=[]
    top2line=[]
    mid2line=[]
    bot2line=[]
    top1line.append(pygame.Rect(0, WINDOWHEIGHT/64*50, WINDOWWIDTH/6, 1))
    mid1line.append(pygame.Rect(0, WINDOWHEIGHT/64*51, WINDOWWIDTH/6, 2))
    bot1line.append(pygame.Rect(0, WINDOWHEIGHT/64*52, WINDOWWIDTH/6, 1))
    top2line.append(pygame.Rect(WINDOWWIDTH/6*5, WINDOWHEIGHT/64*50, WINDOWWIDTH/6, 1))
    mid2line.append(pygame.Rect(WINDOWWIDTH/6*5, WINDOWHEIGHT/64*51, WINDOWWIDTH/6, 2))
    bot2line.append(pygame.Rect(WINDOWWIDTH/6*5, WINDOWHEIGHT/64*52, WINDOWWIDTH/6, 1))
    if player2_click:
        pygame.draw.rect(windowSurface,(0, 0, 0), mid2line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), top2line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), bot2line[0])
        pygame.draw.rect(windowSurface,(174, 174, 174), mid1line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), top1line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), bot1line[0])
    if player1_click:
        pygame.draw.rect(windowSurface,(0, 0, 0), mid1line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), top1line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), bot1line[0])
        pygame.draw.rect(windowSurface,(174, 174, 174), mid2line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), top2line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), bot2line[0])
    if player1_click and player2_click:
        pygame.draw.rect(windowSurface,(0, 0, 0), mid1line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), top1line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), bot1line[0])
        pygame.draw.rect(windowSurface,(0, 0, 0), mid2line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), top2line[0])
        pygame.draw.rect(windowSurface,(255, 0, 0), bot2line[0])
    if not player1_click and not player2_click:
        pygame.draw.rect(windowSurface,(174, 174, 174), mid1line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), top1line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), bot1line[0])
        pygame.draw.rect(windowSurface,(174, 174, 174), mid2line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), top2line[0])
        pygame.draw.rect(windowSurface,(174, 0, 0), bot2line[0])

def lineboxcollide():
    global lasttime
    global timeboxnumber
    global player1box
    global midline
    global lasttimeupdate
    if player1box[timeboxnumber].bottom > mid1line[0].top + 1:
        lasttime = time.time()
        timeboxnumber += 1
        lasttimeupdate = 1
        #print(timeboxnumber)

def timer():
    global timebox1
    global timebox2
    global player1_click
    global player2_click
    global player1boxnumber
    global player2boxnumber
    global player1box
    global onceclick1
    global onceclick2
    global lastclickupdate1
    global lastclickupdate2
    #print(player1_click, onceclick1)
    if player1_click and player1box[player1boxnumber].bottom < bot1line[0].bottom and player1box[player1boxnumber].bottom > top1line[0].top and onceclick1:
        lastclickupdate1 = 1
        onceclick1 = 0
        #print(1)
    if player2_click and player1box[player2boxnumber].bottom < bot1line[0].bottom and player1box[player2boxnumber].bottom > top1line[0].top and onceclick2:
        lastclickupdate2 = 1
        onceclick2 = 0

def timeboxappend():
    global lastclickupdate1
    global lastclickupdate2
    global lasttimeupdate
    global player1boxnumber
    global player2boxnumber
    global lasttimeupdate
    global timeboxnumber
    global timebox1
    global timebox2
    global player1box
    global player2box
    global firsttime1
    global firsttime2
    global lasttime
    #print(lastclickupdate1, lasttimeupdate)
    if lastclickupdate1 and lasttimeupdate:
        timebox1.append(abs(lasttime-firsttime1))
        lastclickupdate1 = 0
        player1boxnumber += 1
        #print(1, lasttime, firsttime1)
    if lastclickupdate2 and lasttimeupdate:
        timebox2.append(abs(lasttime-firsttime2))
        lastclickupdate2 = 0
        player2boxnumber += 1
        #print(2, lasttime, firsttime2)
    if player1box[timeboxnumber-1].bottom > bot1line[0].bottom and player1boxnumber != player2boxnumber:
        lasttimeupdate = 0
        if player1boxnumber > player2boxnumber:
            timebox2.append('X')
            player2boxnumber += 1
        if player1boxnumber < player2boxnumber:
            timebox1.append('X')
            player1boxnumber += 1
    if player1box[timeboxnumber-1].bottom > bot1line[0].bottom and player1boxnumber < timeboxnumber and player2boxnumber < timeboxnumber:
        player1boxnumber += 1
        player2boxnumber += 1

def drawtimer():
    global timebox1
    global timebox2
    #print(timebox1)
    #print(timebox2)
    
while True:
    windowSurface.fill(BLACK)
    event()
    while Once:
        makebox()
        Once = False
    appendbox()
    drawbox()
    movebox()
    drawline()
    lineboxcollide()
    timer()
    timeboxappend()
    drawtimer()
    pygame.display.update()
    #print(firsttime1, firsttime2)
    #print(timeboxnumber, player1boxnumber, player2boxnumber)
    mainClock.tick(SPEED)
