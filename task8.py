import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
RED = (194, 0, 0)


class Food:
    SIZE = 70

    def __init__(self):
        self.random_size = random.randint(5, 20)
        random_x, random_y = random.randint(self.random_size, WIN_WIDTH - self.random_size), random.randint(
            self.random_size, WIN_HEIGHT - self.random_size)

        self.surf = pg.Surface((Food.SIZE * 2, Food.SIZE * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(random_x, random_y))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*RED, 255), (self.rect.width / 2, self.rect.height / 2), self.random_size)

        self.active = True
        self.mask = pg.mask.from_surface(self.surf)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


class Player:
    COLOR = (27, 4, 143)
    WIDTH, HEIGHT = 150, 150
    SPEED = 3

    def __init__(self):
        self.surf = pg.Surface((Player.WIDTH, Player.HEIGHT), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.surf.fill((0, 0, 0, 0))
        self.r = 30
        pg.draw.circle(self.surf, (*Player.COLOR, 255), (self.rect.width / 2, self.rect.height / 2), self.r)

        self.speed = Player.SPEED
        self.mask = pg.mask.from_surface(self.surf)

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIN_WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < WIN_HEIGHT:
            self.rect.y += dy * self.speed

    def eat(self, r_food):
        if self.r <= 70:
            self.r += r_food
            self.surf.fill((0, 0, 0, 0))
            pg.draw.circle(self.surf, (*Player.COLOR, 255), (self.rect.width / 2, self.rect.height / 2), self.r)


    def draw(self, screen):
        screen.blit(self.surf, self.rect)


    def check_collisions(player, foods):
        for food in foods:
            if food.active == True:
                offset = (food.rect.x - player.rect.x, food.rect.y - player.rect.y)
                if player.mask.overlap(food.mask, offset) is not None:
                    food.active = False
                    foods.append(Food())
                    r_food = food.random_size
                    player.eat(r_food)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

foods = [Food(), Food(), Food(), Food()]
player = Player()

screen.fill((255, 255, 255))
for elem in foods:
    elem.draw(screen)
player.draw(screen)
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

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    player.check_collisions(foods)

    screen.fill((255, 255, 255))
    for elem in foods:
        if elem.active == True:
            elem.draw(screen)
    player.draw(screen)
    pg.display.update()
