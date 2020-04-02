#game settings
import pygame as pg
from Sprites import *

import math

#En klasse for dig altså den person man styrer. Vi har brugt nogle sprites som ikke er vores for at prøve om det virker
#Vi regner med at bruge vores egne sprites i fremtiden
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
        self.hitbox = (self.x + 17, self.y + 11, 31, 57)



    def draw(self, screen):
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
        pg.draw.rect(screen, (255,0,0), self.hitbox, 2)

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






Width = 800
Height = 800
Fps = 60
vel = 10
Titel = ("MWDJ’s BowRain")

#Farver
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)



class Enemy(object):
    def __init__(self, x, y , Ewidth, Eheight):
        self.x = x
        self.y = y
        self.Ewidth = Ewidth
        self.Eheight = Eheight
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 11, 31, 57)
        #self.xspeed = xspeed
        #self.yspeed = yspeed

    def draw(self, screen):
        screen.blit(char, (self.x, self.y))
        #pg.draw.rect(screen, Black, (self.x, self.y, self.Ewidth, self.Eheight))
        self.hitbox = (self.x + 17, self.y + 11, 31, 57)
        pg.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        print("Hit the enemy")
        pass
