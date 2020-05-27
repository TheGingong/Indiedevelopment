import pygame as pg
from Classes import *
import math
import random
from os import path

pg.init()

pg.display.set_caption(Titel)

clock = pg.time.Clock()

# Først kører vi denne kode for at vi kan bruge variablen Highscore og vi updatere den hele tiden men når vi dør ændre den sig
Readhighscore = open("highscore.txt", "r")
Highscore = Readhighscore.read()

#Der hvor vi opdatere vores draw funktioner
def redrawGameWindow():
    Readhighscore = open("highscore.txt", "r")
    Highscore = Readhighscore.read()
    if dead == False:
        screen.blit(bg, (0,0))
    else:
        screen.blit(GameOver, (0,0))
    text = font.render('Score: ' + str(score), 1, (Black))
    HStext = font.render('Highscore: ' + str(Highscore), 1, (Dark_green))
    #Tegner vores score på skærmen(ret på x eller y hvis den ser dum ud)
    screen.blit(text, (551, 50))
    screen.blit(HStext, (500, 20))
    man.draw(screen)
    enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pg.display.update()

#MainLoop
font = pg.font.SysFont('comicsans', 30, True)
man = Player(390, 290, 64, 64)
enemy = Enemy(100, 100, 40, 40)
bullets = []



pg.mixer.music.play(-1, 0)
dead = False
run = True
while run:
    clock.tick(Fps)
    keys = pg.key.get_pressed()

    if enemy.visible == True:
        if man.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and man.hitbox[1] + man.hitbox[3] > enemy.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > enemy.hitbox[0] and man.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                man.hit()
                enemy.x = random.randint(10, 1100)
                enemy.y = random.randint(10, 800)
                if score >= 2:
                    score -= 2

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if dead:
        man.visible = False
        enemy.visible = False

        if str(score) > str(Highscore):
            with open ("highscore.txt", "w") as f:
                f.write(str(score))

        if event.type == pg.MOUSEBUTTONDOWN:
            man.visible = True
            enemy.visible = True
            dead = False
            enemy.x = 100
            enemy.y = 100
            man.x = 390
            man.y = 290
            man.health = 3
            enemy.health = 3
            score = 0
            enemy.ekstra = 1.0

    if man.health == 0:
        dead = True

    for bullet in bullets:
        if enemy.visible == True:
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                    #HitSound.play()
                    enemy.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
        # Dette har vi så skuddene forsvinder når de kommer ud af banen så der ikke er 15 milliarder skud der bare flyver omkring
        if bullet.x < Width and bullet.x > 0 and bullet.y < Height and bullet.y > 0:
            bullet.update()

        else:
            bullets.pop(bullets.index(bullet))

    #Karakterens gå funktion
    if keys[pg.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.Left = True
        man.Right = False

    elif keys[pg.K_RIGHT] and man.x < Width - man.Pwidth - man.vel:
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
        #BulletSound.play()
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
        print("Bullet: ",xspeeed, yspeeed)
        print("Enemy: ", xspeed, yspeed)


        if len(bullets) < 1  :
            bullets.append(projectile(round(man.x + man.Pwidth //2), round(man.y + man.Pheight//2), 6, Black, xspeeed, yspeeed))

    #rnd1 = random.randint(10, 1100)
    #rnd2 = random.randint(10, 400)

    epos = [enemy.x, enemy.y]
    ex = epos[0]
    ey = epos[1]
    ppos = [man.x, man.y]
    px = ppos[0]
    py = ppos[1]
    evecx = px - ex
    evecy = py - ey
    evecc = math.sqrt((evecx * evecx) + (evecy * evecy))
    xspeed = evecx / evecc
    yspeed = evecy / evecc

    enemy.x += xspeed * enemy.ekstra
    enemy.y += yspeed * enemy.ekstra
    redrawGameWindow()

pg.quit()