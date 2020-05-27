import pygame as pg

pg.init()
#De sprites som vi bruger til baggrunden og som laver animationen for charakteren
#Vores karakter har ikke en animation lige nu fordi at vi skulle ændre i koden for at få ham til at skyde
#Forhåbenligt kan vi fikse det senere

WalkRight = [pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png'), pg.image.load('Rightsideside_player.png')]
WalkLeft = [pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png'), pg.image.load('Leftside_player.png')]

bg = pg.image.load('Arena.png')
#Menuq = pg.image.load('BowRain_main_menu.jpg')
char = pg.image.load('standing_player.png')
char_enemy = pg.image.load('standing_enemy.png')
heartSprite = pg.image.load('Heart-health.png')
GameOver = pg.image.load('GameOver.png')


Music = pg.mixer.music.load('SpilMusik.mp3')
#BulletSound = pg.mixer.Sound('bullet.WAV')
#HitSound = pg.mixer.Sound('hit.WAV')


