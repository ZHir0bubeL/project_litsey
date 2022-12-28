import pygame, sys

screen_size_menu = width, hieght = 900, 600
screen_size_level = width_level, hieght_level = 300, 700
FPS = 60
current_level = 1


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
                if belongs(325, 263, 575, 337, *(event.pos)):
                    draw_level()
        pygame.display.flip()


def draw_level():
    if current_level == 1:
        draw_level1()


def draw_level1():
    screen = pygame.display.set_mode(screen_size_level)
    going = True

    cell_width = 100
    for i in range(7):
        for j in range(3):
            pygame.draw.rect(screen, (255, 255, 255), (j * cell_width, i * cell_width, cell_width, cell_width), 1)


class Hero1(pygame.sprite.Sprite):
    def __init__(self):
        pass


start_game()
