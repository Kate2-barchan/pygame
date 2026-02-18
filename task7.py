import time
from math import radians

import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 1000, 600
MINT = (230, 254, 212)
ORANGE = (255, 150, 100)
BROWN = (87, 20, 8)
GRAY = (186, 184, 182)
RED = (245, 17, 17)
BLUE = (101, 17, 245)


class Ball:
    SIZE = HEIGHT * 1 / 4

    def __init__(self):
        self.speed = random.randint(5, 20)
        number1, number2, number3 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.random_color = (number1, number2, number3)
        self.radius = random.randint(5, 30)

        self.surf = pg.Surface((Ball.SIZE, Ball.SIZE), pg.SRCALPHA)
        self.rect = self.surf.get_rect(centerx=WIDTH * 1 / 8)
        self.rect.top = round(HEIGHT / 7)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*self.random_color, 100), (self.rect.width / 2, self.rect.height / 2), self.radius)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def move(self):
        top_y = round(HEIGHT * 1 / 7)
        bottom_y = top_y + 250

        if self.rect.top == top_y:
            if self.rect.left <= WIDTH:
                self.rect.left += self.speed
            else:
                self.rect.top = bottom_y
        else:
            if self.rect.top == bottom_y:
                if self.rect.right >= 0:
                    self.rect.right -= self.speed
                else:
                    self.rect.top = top_y


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(BROWN)
pg.draw.rect(background, GRAY, (0, 100, WIDTH, 120))
pg.draw.rect(background, GRAY, (0, 350, WIDTH, 120))

fireworks = [Ball(), Ball()]

screen.blit(background, (0, 0))
for elem in fireworks:
    elem.draw(screen)
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break

    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        new_ball = Ball()
        new_ball.rect.left = 0
        new_ball.rect.top = random.choice([int(round(HEIGHT * 1 / 7)), int(round(HEIGHT * 1 / 7))])
        new_ball.surf.fill((0, 0, 0, 0))
        pg.draw.circle(new_ball.surf, (*new_ball.random_color, 100), (int(new_ball.rect.width / 2), int(new_ball.rect.height / 2)), new_ball.radius)
        fireworks.append(new_ball)



    for elem in fireworks:
        elem.move()

    screen.blit(background, (0, 0))
    for elem in fireworks:
        elem.draw(screen)

    pg.display.update()
