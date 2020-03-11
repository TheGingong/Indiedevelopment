import pygame as pg
from Settings import *


pg.init()

screen = pg.display.set_mode((Width, Height))

pg.display.set_caption(Titel)

clock = pg.time.Clock()

def redrawGameWindow():
    screen.blit(bg, (0,0))
    man.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pg.display.update()


#MainLoop
man = Player(300, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(Fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < Width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 4  :
            bullets.append(projectile(round(man.x + man.Pwidth //2), round(man.y + man.Pheight//2), 6, Black, facing))

    if keys[pg.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pg.K_RIGHT] and man.x < Width - man.Pwidth - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if keys[pg.K_UP] and man.y > man.vel:
        man.y -= man.vel
    if keys[pg.K_DOWN] and man.y < Height - man.Pheight - man.vel:
        man.y += man.vel
    if keys[pg.K_ESCAPE]:
        run = False


    redrawGameWindow()

pg.quit()
