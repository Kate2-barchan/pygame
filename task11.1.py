import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 800
GRAY = (80, 80, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LANE_WIDTH = WIDTH // 3

CAR_SIZE = (60, 120)

class Car(pg.sprite.Sprite):
    speed = 5


    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r"images\car1.png").convert_alpha()
        self.image = pg.transform.scale(self.image, CAR_SIZE)
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < HEIGHT:
            self.rect.y += dy * self.speed

class EnemyCar(pg.sprite.Sprite):

    def __init__(self, lane_x, y):
        pg.sprite.Sprite.__init__(self)
        images = [r"images\car2.png", r"images\car3.png", r"images\car4.png"]
        selected_image = random.choice(images)
        self.image = pg.image.load(selected_image).convert_alpha()
        self.image = pg.transform.scale(self.image, CAR_SIZE)
        self.rect = self.image.get_rect(center=(lane_x, y))
        self.mask = pg.mask.from_surface(self.image)
        self.speed = random.randint(6, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

def draw_road(screen):
    screen.fill(BLACK)
    pg.draw.rect(screen, GRAY, (0, 0, WIDTH, HEIGHT))

    x1 = 1 * LANE_WIDTH
    x2 = 2 * LANE_WIDTH

    pg.draw.line(screen, WHITE, (x1, 0), (x1, HEIGHT), 8)
    pg.draw.line(screen, WHITE, (x2, 0), (x2, HEIGHT), 8)




pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

lane_x1 = LANE_WIDTH // 2
lane_x2 = LANE_WIDTH // 2 + LANE_WIDTH
lane_x3 = LANE_WIDTH // 2 + 2 * LANE_WIDTH

player = Car()
sprites.add(player)

spawn_timer = 0
SPAWN_DELAY = 60
game_over = False

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

    if not game_over:
        # управление игроком через dx, dy
        dx = dy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            dx = -1
        elif keys[pg.K_RIGHT]:
            dx = 1
        if keys[pg.K_UP]:
            dy = -1
        elif keys[pg.K_DOWN]:
            dy = 1

        player.update(dx, dy)

        spawn_timer += 1
        if spawn_timer >= SPAWN_DELAY:
            spawn_timer = 0
            lane_x = random.choice((lane_x1, lane_x2, lane_x3))
            enemy = EnemyCar(lane_x, -80)
            sprites.add(enemy)
            enemies.add(enemy)

        enemies.update()

        if pg.sprite.spritecollideany(player, enemies, pg.sprite.collide_mask):
            game_over = True

            
    draw_road(screen)
    sprites.draw(screen)



    pg.display.update()
