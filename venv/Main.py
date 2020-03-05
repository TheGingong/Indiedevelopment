import pygame as pg
from Settings import *

pg.init()

screen = pg.display.set_mode((Width, Height))

pg.display.set_caption(Titel)

walkRight = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'), pg.image.load('R5.png'), pg.image.load('R6.png'), pg.image.load('R7.png'), pg.image.load('R8.png'), pg.image.load('R9.png')]
walkLeft = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'), pg.image.load('L5.png'), pg.image.load('L6.png'), pg.image.load('L7.png'), pg.image.load('L8.png'), pg.image.load('L9.png')]
bg = pg.image.load('bg.png')
char = pg.image.load('standing.png')

clock = pg.time.Clock()

def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (x, y) )
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount // 3], (x, y) )
        walkCount += 1
    else:
        screen.blit(char, (x, y) )


    pg.display.update()

run = True
while run:
    clock.tick(Fps)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pg.K_RIGHT] and x < Width - PWidth:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if keys[pg.K_UP] and y > vel:
        y -= vel
    if keys[pg.K_DOWN] and y < Height - PHeight - vel:
        y += vel
    if keys[pg.K_ESCAPE]:
        run = False


    redrawGameWindow()

pg.quit()
