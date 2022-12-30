import pygame, sys
from random import randint

screen_size_menu = width, hieght = 900, 600
screen_size_level = width_level, hieght_level = 300, 700
FPS = 60
current_level = 1
enemy_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
heroes = pygame.sprite.Group()
screen = None


def start_game():
    draw_main_menu()


def end_session():
    pygame.quit()
    sys.exit()


def download_image(name):
    name = 'data/' + name
    im = pygame.image.load(name)
    return im


def belongs(toX1, toY1, toX2, toY2, X, Y):
    if toX1 <= X <= toX2 and toY1 <= Y <= toY2:
        return True
    return False


def draw_main_menu():
    pygame.init()
    global screen
    screen = pygame.display.set_mode(screen_size_menu)
    going = True

    background = download_image('forest_fon.png')
    background = pygame.transform.scale(background, (900, 600))
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (325, 263, 250, 74), 1)
    font = pygame.font.Font(None, 90)
    font_render = font.render('НАЧАТЬ', 1, pygame.Color('white'))
    font_rect = (327, 273, 250, 74)
    screen.blit(font_render, font_rect)

    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_session()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if belongs(325, 263, 575, 337, *event.pos):
                    draw_level()
        pygame.display.flip()


def draw_level():
    if current_level == 1:
        draw_level1()


def draw_level1():
    global screen
    screen = pygame.display.set_mode(screen_size_level)
    going = True
    clock = pygame.time.Clock()

    cell_width = 100
    for i in range(7):
        for j in range(3):
            pygame.draw.rect(screen, (255, 255, 255), (j * cell_width, i * cell_width, cell_width, cell_width), 1)

    enemy1, enemy2, enemy3 = Enemy(0, enemy_sprites), Enemy(1, enemy_sprites), Enemy(2, enemy_sprites)
    hero = Hero1(heroes)
    heroes.draw(screen)
    enemy_sprites.draw(screen)
    while going:
        # c = choice(enemy_sprites)
        # c.shoot()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    hero.move(0)
                elif event.key == pygame.K_LEFT:
                    hero.move(-1)
                elif event.key == pygame.K_RIGHT:
                    hero.move(1)
                heroes.draw(screen)
            elif event.type == pygame.QUIT:
                end_session()
        clock.tick(FPS)
        pygame.display.update()


class Enemy(pygame.sprite.Sprite):
    image = download_image('enemy.png')

    def __init__(self, n, *group):
        super().__init__(*group)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.rect.x = 100 * n
        self.rect.y = 0
        self.n = n
        self.clock = pygame.time.Clock()

    def shoot(self):
        global screen
        bullet = Shot(self.n, bullets)
        while bullet.rect.y <= 700:
            bullets.draw(screen)
            bullet.move()
            pygame.display.flip()
            self.clock.tick(1)


class Shot(pygame.sprite.Sprite):
    image = download_image('bullet.png')

    def __init__(self, n, *group):
        super().__init__(*group)
        self.image = Shot.image
        self.rect = Shot.image.get_rect()
        self.rect.x = 100 * n
        self.rect.y = 100

    def move(self):
        if self.rect.y != 100:
            pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 1, self.rect.y + 1 - 100, 98, 98), 0)
        self.rect = self.rect.move(0, 100)


def choice(group):
    n = randint(1, len(group))
    i = 1
    for spr in enemy_sprites:
        if i == n:
            return spr
        i += 1


class Hero1(pygame.sprite.Sprite):
    image = download_image('hero1.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero1.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 600

    def move(self, direction):
        pygame.draw.rect(screen, (0, 0, 0), (self.rect.x + 1, self.rect.y + 1, 98, 98), 0)
        self.rect.y -= 100
        self.rect.x += (100 * direction)
        self.rect.x %= 300


start_game()
