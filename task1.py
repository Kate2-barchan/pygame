import pygame as pg
FPS = 60
WIDTH, HEIGHT = 1000, 600

BEIGE = (235, 210, 155)
DARK_BEIGE = (230, 202, 145)
BLUE = (166, 200, 237)
BROWN = (110, 34, 2)
YELLOW = (247, 181, 49)
BROWN_2 = (102, 34, 2)
DARK_BROWN = (79, 23, 0)
DARK_DARK_BROWN =  (64, 22, 0)
CHARCOAL = (79, 23, 0)
WHITE = (245, 241, 233)
GREEN = (8, 161, 18)
FOREST_GREEN = (4, 140, 12)


pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
sc.fill(BLUE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

pg.draw.rect(sc, BEIGE, (WIDTH / 2, HEIGHT / 2, 200, 250))
pg.draw.rect(sc, DARK_BEIGE, (WIDTH / 2, HEIGHT / 2, 200, 250), 8)
pg.draw.polygon(sc, BROWN, [[WIDTH / 2, HEIGHT / 2], [WIDTH / 2 + 200, HEIGHT / 2], [WIDTH / 2 + 100, HEIGHT / 2 - 100]])
pg.draw.polygon(sc, CHARCOAL, [[WIDTH / 2, HEIGHT / 2], [WIDTH / 2 + 200, HEIGHT / 2], [WIDTH / 2 + 100, HEIGHT / 2 - 100]], 5)
pg.draw.circle(sc, YELLOW, (100, 100), 70)
pg.draw.circle(sc,WHITE, (490, 100), 50)
pg.draw.circle(sc,WHITE, (540, 55), 40)
pg.draw.circle(sc,WHITE, (585, 100), 50)
pg.draw.circle(sc,WHITE, (540, 130), 40)
pg.draw.circle(sc,WHITE, (800, 100), 50)
pg.draw.circle(sc,WHITE, (840, 55), 40)
pg.draw.circle(sc,WHITE, (885, 100), 50)
pg.draw.circle(sc,WHITE, (840, 130), 40)
pg.draw.rect(sc, BROWN_2, (550, 400, 100, 150))
pg.draw.circle(sc, DARK_BROWN, (603, 450), 5)
pg.draw.circle(sc, DARK_BROWN, (635, 480), 7)
pg.draw.circle(sc, GREEN, (750, 480), 50)
pg.draw.circle(sc, FOREST_GREEN, (710, 530), 50)
pg.draw.circle(sc, FOREST_GREEN, (780, 530), 50)
pg.draw.circle(sc, GREEN, (450, 480), 50)
pg.draw.circle(sc, FOREST_GREEN, (410, 530), 50)
pg.draw.circle(sc, FOREST_GREEN, (480, 530), 50)
pg.draw.rect(sc, DARK_DARK_BROWN, (550, 400, 100, 150), 8)
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
