import pygame as pg
pg.init()
#De sprites som vi bruger til baggrunden og som laver animationen for charakteren
#Vores karakter har ikke en animation lige nu fordi at vi skulle ændre i koden for at få ham til at skyde
#Forhåbenligt kan vi fikse det senere
WalkRight = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'), pg.image.load('R5.png'), pg.image.load('R6.png'), pg.image.load('R7.png'), pg.image.load('R8.png'), pg.image.load('R9.png')]
WalkLeft = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'), pg.image.load('L5.png'), pg.image.load('L6.png'), pg.image.load('L7.png'), pg.image.load('L8.png'), pg.image.load('L9.png')]
#walkUp
#walkDown
bg = pg.image.load('Bg.png')
char_enemy = pg.image.load('standing_enemy.png')
char = pg.image.load('standing.png')

Music = pg.mixer.music.load('Spildemo3.mp3')
#BulletSound = pg.mixer.Sound('bullet.mp3')
#HitSound = pg.mixer.Sound('hit.mp3')