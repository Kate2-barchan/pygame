import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600
CANNON_WIDTH, CANNON_HEIGHT = WIDTH * 1 / 4, HEIGHT * 1 / 4
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)
BROWN = (87, 20, 8)
GRAY = (186, 184, 182)
RED = (245, 17, 17)
BLUE = (101, 17, 245)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(BROWN)
pg.draw.rect(background, GRAY, (0, 100, WIDTH, 120))
pg.draw.rect(background, GRAY, (0, 350, WIDTH, 120))

cannon1 = pg.Surface((CANNON_WIDTH, CANNON_HEIGHT), pg.SRCALPHA)
cannon1.fill((0, 0, 0, 0))
pg.draw.circle(cannon1, (*RED, 100), (CANNON_WIDTH / 2, CANNON_HEIGHT / 2), 40)
x1, y1 = 0, 90

cannon2 = pg.Surface((CANNON_WIDTH, CANNON_HEIGHT), pg.SRCALPHA)
cannon2.fill((0, 0, 0, 0))
pg.draw.circle(cannon2, (*BLUE, 100), (CANNON_WIDTH / 2, CANNON_HEIGHT / 2), 20)
x2, y2 = 0, 340

screen.blit(background, (0, 0))
screen.blit(cannon1, (x1, y1))
screen.blit(cannon2, (x2, y2))
pg.display.update()

speed1 = 5
speed2 = 7

flag_play = True
flag1 = 'вправо'
flag2 = 'вправо'
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
            break

    if x1 >= WIDTH:
        flag1 = 'влево'
    if x1 <= -220:
        flag1 = 'вправо'

    if flag1 == 'вправо':
        x1 += speed1
        y1 = 90
    if flag1 == 'влево':
        x1 -= speed1
        y1 = 340

    if x2 >= WIDTH:
        flag2 = 'влево'
    if x2 <= -220:
        flag2 = 'вправо'
    if flag2 == 'вправо':
        x2 += speed2
        y2 = 90
    if flag2 == 'влево':
        x2 -= speed2
        y2 = 340

    screen.blit(background, (0, 0))
    screen.blit(cannon1, (x1, y1))
    screen.blit(cannon2, (x2, y2))
    pg.display.update()
