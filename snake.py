import pygame
import random
import time

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(68, 182, 227)

pygame.init()

pygame.display.set_caption('SNAKE')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

snake_speed = 5
snake_position = [100, 50]
tail_size = 10
score = 0

# drfine first 4 blocks of snake body
snake_body = [
    [100, 50],
    [(100 - tail_size), 50],
    [(100 - (2 * tail_size)), 50],
    [(100 - (3 * tail_size)), 50]
]

# fruit position
fruit_position = [random.randrange(1, (SCREEN_WIDTH // tail_size)) * tail_size,
                  random.randrange(1, (SCREEN_HEIGHT // tail_size)) * tail_size]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

def show_score(score, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= tail_size
    if direction == 'DOWN':
        snake_position[1] += tail_size
    if direction == 'LEFT':
        snake_position[0] -= tail_size
    if direction == 'RIGHT':
        snake_position[0] += tail_size
    
    screen.fill(black)
    
    snake_body.insert(0, list(snake_position))
    for pos in snake_body:
        pygame.draw.rect(screen, green,
                         pygame.Rect(pos[0], pos[1], tail_size, tail_size))
    
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (SCREEN_WIDTH // tail_size)) * tail_size, 
                          random.randrange(1, (SCREEN_HEIGHT // tail_size)) * tail_size]
    fruit_spawn = True
    
    pygame.draw.rect(screen, white, pygame.Rect(
        fruit_position[0], fruit_position[1], tail_size, tail_size))
    
    # Game Over contition
    if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH - tail_size:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT - tail_size:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(score, white,'times new roman', 20)
    pygame.display.update()
    clock.tick(snake_speed)
pygame.quit()
