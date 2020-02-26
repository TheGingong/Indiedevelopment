# Sprite klasser

import pygame as pg
from Settings import *



class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((PWidth,PHeight))
        self.image.fill(Red)
        self.rect = self.image.get_rect()
        self.rect.center = (Width / 2, Height / 2)
        # Easy variabler lol
        self.x = 0
        self.y = 0
        self.IsJump = False
        self.Jumpcount = 10
        self.left = False
        self.right = False
        self.walkCount = 0


    def update(self):
        self.x = 0
        self.y = 0
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.x = -vel
        if self.rect.x < 0 : self.rect.x = 0

        if keys[pg.K_RIGHT]:
            self.x = vel
        if self.rect.x > Width-PWidth : self.rect.x = Width - PWidth

        if not(self.IsJump):
            #if keys[pg.K_DOWN]:
                #self.y = vel
            #if self.rect.y > Height - PWidth: self.rect.y = Height - PHeight

            if keys[pg.K_UP] or keys[pg.K_SPACE]:
                self.IsJump = True
        else:
            if self.Jumpcount >= -10:
                self.neg = 0.6
                if self.Jumpcount < 0:
                    self.neg = -0.6
                self.y -= (self.Jumpcount ** 2) * 0.4 * self.neg
                self.Jumpcount -= 1
            else:
                self.IsJump = False
                self.Jumpcount = 10

        self.rect.x += self.x
        self.rect.y += self.y

