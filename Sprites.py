import pygame as pg

pg.init()

#Her bliver der spillet vores karakter animationer. Læse synopsis for tydeligere beskrivelse
WalkRight = [pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png')]
WalkLeft = [pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png')]

#Her bliver vores billeder, lyde, baggrunde, osv lagt ind i variabler så vi kan benytte os af dem senere
bg = pg.image.load('Arena.png')
char = pg.image.load('standing_player.png')
char_enemy = pg.image.load('standing_enemy.png')
heartSprite = pg.image.load('Heart-health.png')
GameOver = pg.image.load('GameOver.png')
Music = pg.mixer.music.load('SpilMusik.mp3')
BulletSound = pg.mixer.Sound('bullet.ogg')
HitSound = pg.mixer.Sound('hit.ogg')