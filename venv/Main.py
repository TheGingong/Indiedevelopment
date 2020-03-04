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

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
    if keys[pg.K_RIGHT] and x < Width - PWidth:
        x += vel
    if keys[pg.K_UP] and y > vel:
        y -= vel
    if keys[pg.K_DOWN] and y < Height - PHeight - vel:
        y += vel
    if keys[pg.K_ESCAPE]:
        run = False

    screen.fill(Black)
    pg.draw.rect(screen, Red, (x, y, PWidth, PHeight))
    pg.display.update()

pg.quit()