import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 800

GRAY = (80, 80, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

STRIPES_WIDTH = WIDTH // 3

class Car:
    speed = 7

    def __init__(self, x, y, image_path):
        self.origin_surf = pg.image.load(image_path).convert_alpha()
        self.car_surf = self.origin_surf
        self.car_rect = self.car_surf.get_rect(center=(x, y))
        self.direction = "up"

    def rotate(self, new_direction):
        if new_direction == "up":
            self.angle = 0
        elif new_direction == "right":
            self.angle = -90
        elif new_direction == "down":
            self.angle = -180
        elif new_direction == "left":
            self.angle = -270

        origin_surf = self.origin_surf
        new_surf = pg.transform.rotate(origin_surf, self.angle)
        center = self.car_rect.center
        self.car_surf = new_surf
        self.car_rect = self.car_surf.get_rect(center=center)
        self.direction = new_direction

    def move_forward(self):
        if self.direction == "up":
            self.car_rect.y -= self.speed
        elif self.direction == "down":
            self.car_rect.y += self.speed
        elif self.direction == "left":
            self.car_rect.x -= self.speed
        elif self.direction == "right":
            self.car_rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.car_surf, self.car_rect)

class EnemyCar(Car):
    def __init__(self, lane_x, y, image_path, speed):
        Car.__init__(self, lane_x, y, image_path)
        self.speed = speed
        self.rotate("down")

    def update(self):
        self.car_rect.y += self.speed

def road(screen):
    screen.fill(BLACK)
    pg.draw.rect(screen, GRAY, (0, 0, WIDTH, HEIGHT))
    for i in range(1, 3):
        x = i * STRIPES_WIDTH
        pg.draw.line(screen, WHITE, (x, 0), (x, HEIGHT), 8)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

middle_lane_x = STRIPES_WIDTH // 2 + STRIPES_WIDTH
player_car = Car(middle_lane_x, HEIGHT - 120, r"images\car_orig.png")
player_car.rotate("up")

road(screen)
player_car.draw(screen)
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

    road(screen)
    player_car.draw(screen)

    pg.display.update()
