import pygame
import time
import random

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake parameters
snake_block = 10
snake_speed = 15

# Initialize snake position and direction
snake_list = []
snake_length = 1
snake_head = [width // 2, height // 2]
snake_direction = "RIGHT"
change_to = snake_direction
speed = snake_speed

# Food parameters
food_position = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]


# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])


# Function to display the message when the game is over
def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])


# Game Loop
game_over = False
game_close = False

while not game_over:

    while game_close:
        window.fill(black)
        message("You Lost! Press C-Play Again or Q-Quit", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    # Reset the game
                    snake_list = []
                    snake_length = 1
                    snake_head = [width // 2, height // 2]
                    snake_direction = "RIGHT"
                    change_to = snake_direction
                    food_position = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
                    game_close = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not snake_direction == "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and not snake_direction == "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_UP and not snake_direction == "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and not snake_direction == "UP":
                change_to = "DOWN"

    # Update the direction
    if change_to == "LEFT":
        snake_head[0] -= snake_block
    elif change_to == "RIGHT":
        snake_head[0] += snake_block
    elif change_to == "UP":
        snake_head[1] -= snake_block
    elif change_to == "DOWN":
        snake_head[1] += snake_block

    # Check for collision with walls or self
    if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
        game_close = True
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_close = True

    # Move the snake
    snake_list.append(list(snake_head))
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with food
    if snake_head == food_position:
        food_position = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        snake_length += 1

    # Update the display
    window.fill(black)
    our_snake(snake_block, snake_list)
    pygame.draw.rect(window, red, [food_position[0], food_position[1], snake_block, snake_block])
    pygame.display.update()

    # Set the game speed
    pygame.time.Clock().tick(speed)

# Quit the game
pygame.quit()
