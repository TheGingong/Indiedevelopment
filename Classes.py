#Globale variabler
Width = 1200
Height = 840
Fps = 60
vel = 10
ShootLoop = 0
Titel = ("MWDJ’s BowRain")


#Farver
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Dark_green = (0,100,0)
Blue = (0,0,255)

#game settings implementation
import time
import pygame as pg
import random
from Sprites import *
pg.init()
import math
screen = pg.display.set_mode((Width, Height))

#En klasse for spilleren hvor vi definere x, y, velocity, health, walkcount, hitbox, mm.
class Player(object):
    def __init__(self, x, y, Pwidth, Pheight):
        self.x = x
        self.y = y
        self.Pwidth = Pwidth
        self.Pheight = Pheight
        self.vel = 5
        self.Left = False
        self.Right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.health = 3
        self.visible = True
        self.hitbox = (self.x + 17, self.y + 11, 31, 57)

#Draw funktion for player hvilket sætter standard værdier for spilleren som health, og movement.
    def draw(self, screen):
        if self.visible == True:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.Left:
                screen.blit(WalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.Right:
                screen.blit(WalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(char, (self.x,self.y))
            #Så vi kan se vores hitbox
            self.hitbox = (self.x + 17, self.y + 11, 31, 57)

            if self.health == 3:
                screen.blit(heartSprite, (50, 20))
                screen.blit(heartSprite, (110, 20))
                screen.blit(heartSprite, (170, 20))

            if self.health == 2:
                screen.blit(heartSprite, (50, 20))
                screen.blit(heartSprite, (110, 20))

            if self.health == 1:
                screen.blit(heartSprite, (50, 20))

            if self.health == 0:
                self.visible = False

    def hit(self):
        self.x = 390
        self.y = 290
        self.walkCount = 0
        if self.health >= 0:
            self.health -= 1
        pg.display.update()


#En klasse for dine skud
class projectile(object):
    def __init__(self, x, y , radius, color, xspeeed, yspeeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.xspeeed = xspeeed
        self.yspeeed = yspeeed

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.x += self.xspeeed * 10
        self.y += self.yspeeed * 10

#Vi er i gang med at lave en enemy class som så vil følge efter dig
class Enemy(object):
    def __init__(self, x, y , Ewidth, Eheight):
        self.x = x
        self.y = y
        self.Ewidth = Ewidth
        self.Eheight = Eheight
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 11, 31, 57)
        self.health = 1
        self.visible = True
        self.ekstra = 1.0
        self.score = 0
        self.hpbar = 1

    def draw(self, screen):
        if self.visible:
            screen.blit(char_enemy, (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 6, 31, 57)
            #Healthbar
            pg.draw.rect(screen, (255,0,0), (self.hitbox[0] - 10, self.hitbox[1] - 20, 50, 10))
            pg.draw.rect(screen, (0, 128, 0), (self.hitbox[0] - 10, self.hitbox[1] - 20, 50 / self.hpbar, 10))

    def hit(self):
        self.ekstra += 0.1
        if self.health > 0:
            self.health -= 1
            self.hpbar += 1
        else:
            self.visible = False
            self.visible = True
            self.x = random.randint(10, 1100)
            self.y = random.randint(10, 800)
            self.health = 1
            self.score += 1
            self.hpbar = 1
        #print("Hit the enemy")
        pass
