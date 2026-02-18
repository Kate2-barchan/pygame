import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600
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

cannon1 = pg.Surface((HEIGHT * 1 / 4, HEIGHT * 1 / 4), pg.SRCALPHA)
cannon_rect = cannon1.get_rect(centerx=WIDTH / 2)
cannon_rect.top = HEIGHT * 3 / 4
cannon1.fill((0, 0, 0, 0))
pg.draw.circle(cannon1, (*RED, 100), (cannon_rect.width / 2, cannon_rect.height / 2), 40)
x1, y1 = 0, 90

cannon2 = pg.Surface((HEIGHT * 1 / 4, HEIGHT * 1 / 4), pg.SRCALPHA)
cannon_rect = cannon2.get_rect(centerx=WIDTH / 2)
cannon_rect.top = HEIGHT * 3 / 4
cannon2.fill((0, 0, 0, 0))
pg.draw.circle(cannon2, (*BLUE, 100), (cannon_rect.width / 2, cannon_rect.height / 2), 20)
x2, y2 = 0, 340

screen.blit(background, (0, 0))
screen.blit(cannon1, (x1, y1))
screen.blit(cannon2, (x2, y2))
pg.display.update()


rect1 = cannon1.get_rect(topleft=(x1, y1))
rect2 = cannon2.get_rect(topleft=(x2, y2))

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

    if rect1.left >= WIDTH:
        flag1 = 'влево'

    if rect1.left <= -220:
        flag1 = 'вправо'

    if flag1 == 'вправо':
        rect1.x += speed1
        rect1.y = 90
    if flag1 == 'влево':
        rect1.x -= speed1
        rect1.y = 340

    if rect2.left >= WIDTH:
        flag2 = 'влево'
    if rect2.left <= -220:
        flag2 = 'вправо'
    if flag2 == 'вправо':
        rect2.x += speed2
        rect2.y = 90
    if flag2 == 'влево':
        rect2.x -= speed2
        rect2.y = 340

    screen.blit(background, (0, 0))
    screen.blit(cannon1, rect1)
    screen.blit(cannon2, rect2)
    pg.display.update()
