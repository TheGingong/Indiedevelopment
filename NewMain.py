import pygame as pg
from Settings import *
import math



pg.init()

screen = pg.display.set_mode((Width, Height))

pg.display.set_caption(Titel)

clock = pg.time.Clock()




#Der hvor vi opdatere vores draw funktioner
def redrawGameWindow():
    screen.blit(bg, (0,0))
    man.draw(screen)
    enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pg.display.update()




#MainLoop
man = Player(390, 290, 64, 64)
enemy = Enemy(0,0, 40, 40)

pg.mixer.music.load('Spildemo3.mp3')
pg.mixer.music.play(-1, 0, 0)
bullets = []
run = True
while run:
    clock.tick(Fps)



    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    #Dette har vi så skuddene forsvinder når de kommer ud af banen så der ikke er 15 milliarder skud der bare flyver omkring
    for bullet in bullets:
        if bullet.x < Width and bullet.x > 0 and bullet.y < Height and bullet.y > 0:
            bullet.update()

        else:
            bullets.pop(bullets.index(bullet))


    keys = pg.key.get_pressed()


    #Karakterens gå funktion
    if keys[pg.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.Left = True
        man.Right = False

    if keys[pg.K_RIGHT] and man.x < Width - man.Pwidth - man.vel:
        man.x += man.vel
        man.Right = True
        man.Left = False

    else:
        man.Right = False
        man.Left = False
        man.walkCount = 0


    if keys[pg.K_DOWN] and man.y < Height - man.Pheight - man.vel:
        man.y += man.vel
    if keys[pg.K_UP] and man.y > man.vel:
        man.y -= man.vel


    if keys[pg.K_ESCAPE]:
        run = False






    #Vores skyde funktion, som tager brug af nogle vektorer til at se hvor musen er og beregner hvor den skal skyde hen
    if event.type == pg.MOUSEBUTTONDOWN:
        mpos = pg.mouse.get_pos()
        mx, my = pg.mouse.get_pos()
        ppos = [man.x, man.y]
        px = ppos[0]
        py = ppos[1]
        vecx = mx - px
        vecy = my - py
        vecc = math.sqrt((vecx * vecx) + (vecy * vecy))
        xspeeed = vecx / vecc
        yspeeed = vecy / vecc
        print(xspeeed, yspeeed)


        if len(bullets) < 1  :
            bullets.append(projectile(round(man.x + man.Pwidth //2), round(man.y + man.Pheight//2), 6, Black, xspeeed, yspeeed))


    redrawGameWindow()





pg.quit()
