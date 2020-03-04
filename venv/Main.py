import pygame as pg
from Settings import *

pg.init()

screen = pg.display.set_mode((Width, Height))

pg.display.set_caption(Titel)


run = True
while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        x -= vel
    if keys[pg.K_RIGHT]:
        x += vel
    if keys[pg.K_UP]:
        y -= vel
    if keys[pg.K_DOWN]:
        y += vel

    screen.fill(Black)
    pg.draw.rect(screen, Red, (x, y, PWidth, PHeight))
    pg.display.update()

pg.quit()
