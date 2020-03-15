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
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True


    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):

            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x, self.y) )
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount // 3], (self.x, self.y) )
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))

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
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.xspeeed * 10
        self.y += self.yspeeed * 10

#Vi er i gang med at lave en enemy class som så vil følge efter dig
class Enemy(object):
    def __init__(self, x, y , Ewidth, Eheight):
        self.x = x
        self.y = y
        self. Ewidth = Ewidth
        self.Eheight = Eheight
        self.vel = 3
        #self.xspeed = xspeed
        #self.yspeed = yspeed

    def draw(self, screen):
        pg.draw.rect(screen, Black, (self.x, self.y, self.Ewidth, self.Eheight))

    def update(self):
        #self.x += self.xspeed
        #self.y += self.yspeed
        pass


Width = 1200
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





# Ikke slet please :)
# greater than >
# less than <
