import pygame
import time
import random

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Параметры экрана
WIDTH, HEIGHT = 1280, 720
DIS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Загрузка фона
background = pygame.image.load("background.jpg")

# Параметры змеи
BLOCK_SIZE = 10
SNAKE_SPEED = 15

# Шрифт для вывода сообщений
FONT_STYLE = pygame.font.SysFont(None, 50)

# Функция отображения змеи
def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(DIS, BLUE, [segment[0], segment[1], snake_block, snake_block])

# Функция вывода сообщения на экран
def display_message(message, color):
    message_surface = FONT_STYLE.render(message, True, color)
    DIS.blit(message_surface, [WIDTH / 6, HEIGHT / 3])
    pygame.display.update()

# Основная функция игры
def game_loop():
    game_over = False
    game_close = False

    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:
        while game_close:
            DIS.blit(background, (0, 0))
            display_message("You Lost! Press C-Play Again or Q-Quit", RED)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT:
                    x1_change, y1_change = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP:
                    x1_change, y1_change = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    x1_change, y1_change = 0, BLOCK_SIZE

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        DIS.blit(background, (0, 0))
        pygame.draw.rect(DIS, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            length_of_snake += 1

        pygame.time.Clock().tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()