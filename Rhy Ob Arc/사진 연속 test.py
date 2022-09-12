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
num = 1
n = 0
mousexinput = []
mouseyinput = []
ok = False
mousex = 0
mousey = 0
mouseevent = False
what = 6
number = 0
ImageRect = []
ImageStreched = []
for i in range(4):
    Image.append(pygame.image.load('6.%d.png'%(i)))
    jumping=(pygame.image.load('jumping.jpg'))
    ImageStreched.append(pygame.transform.scale(Image[i], (300, 300)))
    ImageRect.append(ImageStreched[i].get_rect())
    ImageRect[i].centerx = 450
    ImageRect[i].centery = 300

SPEED = 500
while True:
    windowSurface.fill(BLACK)
    windowSurface.blit(jumping,(0,0))
    windowSurface.blit(ImageStreched[number], ImageRect[number])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == ord('r'):
                if len(mousexinput) > 0:
                    mousexinput.remove(mousexinput[len(mousexinput)-1])
                    mouseyinput.remove(mouseyinput[len(mouseyinput)-1])
                    ok = False
            if event.key == ord('f'):
                ok = True
                print(mousexinput)
                print(mouseyinput)
            if event.key == ord('n'):
                outfile=open("%d.%d.txt"%(what,number), "a")
                for num in mousexinput:
                    outfile.write("%d\n"%(num))
                for num in mouseyinput:
                    outfile.write("%d\n"%(num))
                outfile.close()
                number += 1
                mousexinput = []
                mouseyinput = []
                ok = False
        if event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            mousexinput.append(mousex)
            mouseyinput.append(mousey)

    for i in range(len(mousexinput)):
        pygame.draw.circle(windowSurface, YELLOW, (mousexinput[i], mouseyinput[i]), 2, 0)
        if i == len(mousexinput)-1 and ok:
            pygame.draw.line(windowSurface, GREEN, (mousexinput[i], mouseyinput[i]), (mousexinput[0], mouseyinput[0]), 2)
        if i > 0:
            pygame.draw.line(windowSurface, GREEN, (mousexinput[i], mouseyinput[i]), (mousexinput[i-1], mouseyinput[i-1]), 2)
    #windowSurface.blit(Image[num],(0,0))
    pygame.display.update()
    mainClock.tick(SPEED)
    
''' 박자 맞춰서 애들 색깔 바뀌게'''
