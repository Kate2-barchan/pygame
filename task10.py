import pygame as pg

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
WHITE = (255, 255, 255)


class Car:
    speed = 5

    def __init__(self):
        self.origin_surf = pg.image.load(r"images\car_orig.png").convert_alpha()  # ОРИГИНАЛ
        self.car_surf = self.origin_surf  # копия оригинала
        self.car_rect = self.car_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
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

    def draw(self, screen):
        screen.blit(self.car_surf, self.car_rect)

    def move(self):
        if self.direction == "up":
                self.car_rect.y -= self.speed
        elif self.direction == "down":
                self.car_rect.y += self.speed
        elif self.direction == "left":
                self.car_rect.x -= self.speed
        elif self.direction == "right":
                self.car_rect.x += self.speed

        # границы экрана
        self.car_rect.clamp_ip(screen.get_rect())

    def draw(self, screen):
        screen.blit(self.car_surf, self.car_rect)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

my_car = Car()

screen.fill(WHITE)
my_car.draw(screen)
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
    if keys[pg.K_UP]:
        my_car.rotate("up")
        my_car.move()
    elif keys[pg.K_DOWN]:
        my_car.rotate("down")
        my_car.move()
    elif keys[pg.K_LEFT]:
        my_car.rotate("left")
        my_car.move()
    elif keys[pg.K_RIGHT]:
        my_car.rotate("right")
        my_car.move()


    screen.fill(WHITE)
    my_car.draw(screen)
    pg.display.update()
