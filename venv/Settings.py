#game settings
import pygame as pg
from Sprites import *


class Player(object):
    def __init__(self, x, y, Pwidth, Pheight):
        self.x = x
        self.y = y
        self.Pwidth = Pwidth
        self.Pheight = Pheight
        self.vel = 5
        self.left = False
        self.right = False
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


class projectile(object):
    def __init__(self, x, y , radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)


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
