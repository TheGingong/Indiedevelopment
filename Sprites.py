import pygame as pg

pg.init()

WalkRight = [pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png')]
WalkLeft = [pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png')]

bg = pg.image.load('Arena.png')
char = pg.image.load('standing_player.png')
char_enemy = pg.image.load('standing_enemy.png')
heartSprite = pg.image.load('Heart-health.png')
GameOver = pg.image.load('GameOver.png')
Music = pg.mixer.music.load('SpilMusik.mp3')
#BulletSound = pg.mixer.Sound('bullet.mp3')
#HitSound = pg.mixer.Sound('hit.mp3')



