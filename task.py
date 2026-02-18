import pygame as pg
FPS = 60
WIDTH, HEIGHT = 1000, 600

SKY_BLUE = (227, 231, 255)
GREY = (189, 191, 199)
GREY_2 = (189, 191, 199)


pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
sc.fill(SKY_BLUE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

pg.draw.rect(sc, GREY, (WIDTH / 2, HEIGHT / 2 - 60, 150, 290))
pg.draw.polygon(sc, GREY_2, [[WIDTH / 2, HEIGHT / 2 - 60], [WIDTH / 2 + 75, HEIGHT / 2 - 60 - 60], [WIDTH / 2 + 150, HEIGHT / 2 - 60]])
pg.display.update()


flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    # изменение объектов
    # ...

    # обновление экрана
    pg.display.update()
