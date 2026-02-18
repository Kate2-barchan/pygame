import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
SPACE = (5, 5, 20)

SHIP_SIZE = (120, 120)
ASTEROID_SIZE = (169, 77)
FIREBALL_SIZE = (50, 50)


class Ship(pg.sprite.Sprite):
    speed = 6

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\ship.png").convert_alpha()
        self.image = pg.transform.scale(self.image, SHIP_SIZE)
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.clamp_ip(pg.Rect(0, 0, WIDTH, HEIGHT))


class Asteroid(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\asteroid.png").convert_alpha()
        self.image = pg.transform.scale(self.image, ASTEROID_SIZE)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pg.mask.from_surface(self.image)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


class Fireball(pg.sprite.Sprite):
    speed = 10

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\the fireball.png").convert_alpha()
        self.image = pg.transform.rotate(self.image, 90)
        self.image = pg.transform.scale(self.image, FIREBALL_SIZE)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


def spawn_asteroid():
    x = random.randint(20, WIDTH - 20)
    y = -40
    asteroids.add(Asteroid(x, y))


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Космический шутер")
clock = pg.time.Clock()

pg.mixer.music.load(r"audio\background_music.mp3")
pg.mixer.music.play(-1)

crash_sound = pg.mixer.Sound(r"audio\collision_with_an_asteroid.mp3")
fireball_sound = pg.mixer.Sound(r"audio\fireball_shot.flac")

bg = pg.image.load(r"images\background.jpg").convert()
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))

asteroids = pg.sprite.Group()
fireballs = pg.sprite.Group()

ship = Ship()

spawn_timer = 0
SPAWN_DELAY = 80

game_over = False

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        if event.type == pg.KEYDOWN and not game_over:
            if event.key == pg.K_SPACE:
                fireballs.add(Fireball(ship.rect.centerx, ship.rect.top))
                fireball_sound.play()
    if not flag_play:
        break

    if not game_over:
        keys = pg.key.get_pressed()
        dx = dy = 0
        if keys[pg.K_LEFT]:
            dx = -1
        elif keys[pg.K_RIGHT]:
            dx = 1
        if keys[pg.K_UP]:
            dy = -1
        elif keys[pg.K_DOWN]:
            dy = 1

        ship.update(dx, dy)

        spawn_timer += 1
        if spawn_timer >= SPAWN_DELAY:
            spawn_timer = 0
            spawn_asteroid()

        fireballs.update()
        asteroids.update()

        pg.sprite.groupcollide(fireballs, asteroids, True, True, pg.sprite.collide_mask)

        if pg.sprite.spritecollideany(ship, asteroids, pg.sprite.collide_mask):
            crash_sound.play()  # звук столкновения
            pg.mixer.music.stop()
            game_over = True

    if game_over:
        font = pg.font.SysFont(None, 72)
        text = font.render("GAME OVER", True, (255, 0, 0))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # отрисовка
    if not game_over:
        screen.blit(bg, (0, 0))
        ship.draw(screen)
        fireballs.draw(screen)
        asteroids.draw(screen)
    else:
        screen.blit(text, rect)

    pg.display.update()
