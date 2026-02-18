import random
import pygame as pg

FPS = 60
WIDTH, HEIGHT = 600, 500
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()


r = 30
x, y = random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r)
pg.draw.circle(screen, ORANGE, (x, y), r)
pg.display.update()


flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 4:
            pos = pg.mouse.get_pos()
            dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
            if dist <= r and r <= 100:
                r += 1
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 5:
            dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
            if dist <= r and r >= 10:
                r -= 1

    pressed = pg.mouse.get_pressed()
    if pressed[1]:
        pos = pg.mouse.get_pos()
        dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
        if dist <= r:
            x, y = random.randint(r, WIDTH - r), random.randint(r, HEIGHT - r)
    if pressed[0]:
        pos = pg.mouse.get_pos()
        dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
        if dist <= r and r <= 100:
            r += 1

    if pressed[2]:
        pos = pg.mouse.get_pos()
        dist = ((pos[0] - x) ** 2 + (pos[1] - y) ** 2) ** 0.5
        if dist <= r and r >= 10:
            r -= 1
