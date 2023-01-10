import pygame
import sys


pygame.init()

COVER = pygame.image.load('PongCover.png')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 1000

font_end_game = pygame.font.SysFont('Arial', 98, True)
font_score = pygame.font.SysFont('Arial', 28, True)
speed = 4
score = 0
fps = 60
position_block = 200
y_ball = 250
x_ball = 200
ball_up = True
ball_right = True

window = pygame.display.set_caption('PygamePong')
window = pygame.display.set_icon(COVER)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


def close_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


while True:
    close_window()
    clock.tick(fps)
    window.fill(BLACK)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if position_block > 0:
            position_block -= 5

    elif keys[pygame.K_DOWN]:
        if position_block + 100 < 500:
            position_block += 5

    if x_ball - 20 <= 0:
        ball_right = True

    if y_ball + 20 >= 500:
        ball_up = True
    elif y_ball - 20 <= 0:
        ball_up = False

    if ball_right:
        x_ball += speed
    else:
        x_ball -= speed

    if ball_up:
        y_ball -= speed
    else:
        y_ball += 5

    if position_block <= y_ball <= position_block + 100 and 1000 - 20 <= x_ball + 20 <= 1000:
        ball_right = False
        score += 1
        speed += 1
    elif x_ball + 20 > 1000:
        render_end = font_end_game.render('GAME OVER', True, RED)
        window.blit(render_end, (200, 200))

    pygame.draw.line(window, WHITE, (500, 0), (500, 500), 5)
    pygame.draw.circle(window, WHITE, (500, 250), 75, 5)
    pygame.draw.rect(window, WHITE, (0, 0, 1000, 500), 10)
    pygame.draw.circle(window, WHITE, (x_ball, y_ball), 20)
    pygame.draw.rect(window, WHITE, (965, position_block, 20, 100))
    render_score = font_score.render(f'SCORE: {score}', True, WHITE)
    window.blit(render_score, (30, 10))
    pygame.display.update()
