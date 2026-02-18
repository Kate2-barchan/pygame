import pygame as pg
import random

FPS = 60
WIN_WIDTH, WIN_HEIGHT = 1000, 600
PINK = (245, 125, 255)
PINK_1 = (243, 82, 255)
WHITE = (255, 255, 255)
GREY_BLUE, DARK_GREY_BLUE = (57, 64, 82), (28, 32, 43)
GRAY = (41, 40, 40)
BLACK = (0, 0, 0)


class Food:
    SIZE = 70

    def __init__(self):
        self.random_size = random.randint(5, 20)
        random_x, random_y = random.randint(self.random_size, WIN_WIDTH - self.random_size), random.randint(
            self.random_size, WIN_HEIGHT - self.random_size)

        self.surf = pg.Surface((Food.SIZE * 2, Food.SIZE * 2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(random_x, random_y))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*PINK, 255), (self.rect.width / 2, self.rect.height / 2), self.random_size)
        pg.draw.circle(self.surf, (*PINK_1, 255), (self.rect.width / 2, self.rect.height / 2), self.random_size, 3)

        self.active = True
        self.mask = pg.mask.from_surface(self.surf)

    def draw(self, screen):
        if self.active:
            screen.blit(self.surf, self.rect)


class Player:
    COLOR = (255, 0, 0)
    COLOR_1 = (166, 7, 7)
    WIDTH, HEIGHT = 150, 150
    SPEED = 3

    def __init__(self):
        self.surf = pg.Surface((Player.WIDTH, Player.HEIGHT), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.surf.fill((0, 0, 0, 0))
        self.r = 30
        self.update_surface()

        self.speed = Player.SPEED
        self.mask = pg.mask.from_surface(self.surf)

    def update_surface(self):
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*Player.COLOR, 255), (self.rect.width / 2, self.rect.height / 2), self.r)
        pg.draw.circle(self.surf, (*Player.COLOR_1, 255), (self.rect.width / 2, self.rect.height / 2), self.r, 3)
        self.mask = pg.mask.from_surface(self.surf)

    def move(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIN_WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < WIN_HEIGHT:
            self.rect.y += dy * self.speed

    def eat(self, r_food):
        if self.r <= 70:
            self.r += r_food
            self.update_surface()

    def reset_radius(self):
        self.r = 30
        self.update_surface()

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


def check_collisions(player, foods):
    for food in foods[:]:
        if food.active:
            offset = (food.rect.x - player.rect.x, food.rect.y - player.rect.y)
            if player.mask.overlap(food.mask, offset) is not None:
                food.active = False
                foods.append(Food())
                r_food = food.random_size
                player.eat(r_food)



class Text:
    def __init__(self, text, text_size, text_color, text_pos):
        self.font = pg.font.SysFont(None, text_size)
        self.suft = self.font.render(text, True, text_color)
        self.rect = self.suft.get_rect(center=text_pos)

    def change_text(self, new_text):
        self.suft = self.font.render(new_text, True, WHITE)
        self.rect = self.suft.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 7))

    def draw(self, screen):
        screen.blit(self.suft, self.rect)


class Button:
    def __init__(self, text, text_size, text_color, button_color, button_cover_color, button_pos):
        self.button_color = button_color
        self.button_cover_color = button_cover_color
        self.font = pg.font.SysFont(None, text_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=button_pos)
        self.button_surf = pg.Surface((self.text_surf.get_width() + 50, self.text_surf.get_height() + 50))
        self.button_rect = self.button_surf.get_rect(center=button_pos)
        self.button_surf.fill(button_color)
        pg.draw.rect(self.button_surf, WHITE, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def redraw(self, state):
        if state:
            self.button_surf.fill(self.button_cover_color)
            pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)
        else:
            self.button_surf.fill(self.button_color)
            pg.draw.rect(self.button_surf, BLACK, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def draw(self, screen):
        screen.blit(self.button_surf, self.button_rect)
        screen.blit(self.text_surf, self.text_rect)


def check_click_on_button(button, player, radius_text):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        player.reset_radius()
        radius_text.change_text(f"Радиус: {player.r}")


def check_mouse_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        button.redraw(state=True)
    else:
        button.redraw(state=False)


pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

foods = [Food() for _ in range(4)]
player = Player()
my_text = Text(f"Радиус: {player.r}", 32, WHITE , (WIN_WIDTH / 2, WIN_HEIGHT / 7))
my_button = Button('сбросить', 45, BLACK, GREY_BLUE, DARK_GREY_BLUE, (WIN_WIDTH / 2, WIN_HEIGHT * 2 / 2.5))

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            check_click_on_button(my_button, player, my_text)
    if not flag_play:
        break

    check_mouse_on_button(my_button)


    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    check_collisions(player, foods)

    if hasattr(my_text, 'suft'):
        my_text.change_text(f"Радиус: {player.r}")

    screen.fill(GRAY)
    my_text.draw(screen)
    my_button.draw(screen)
    for elem in foods:
        elem.draw(screen)
    player.draw(screen)
    pg.display.update()

pg.quit()
