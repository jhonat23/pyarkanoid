import pygame
import random
import sys

# Inicializa Pygame y establece algunas variables para el tamaño de la pantalla y los colores que se utilizarán:

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arkanoid")
bg_color = (0, 0, 0)
paddle_color = (255, 255, 255)
ball_color = (255, 255, 255)
brick_color = (255, 0, 0)

# Crea la plataforma móvil del jugador y la pelota:

paddle_width = 100
paddle_height = 10
paddle_x = (width // 2) - (paddle_width // 2)
paddle_y = height - 50
paddle_speed = 5
paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

ball_size = 10
ball_x = random.randint(ball_size, width - ball_size)
ball_y = height // 2
ball_speed_x = 2
ball_speed_y = -2
ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

#Crea los ladrillos y guárdalos en una lista:

brick_width = 70
brick_height = 20
brick_margin = 10
brick_rows = 5
brick_cols = 10
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = (col * (brick_width + brick_margin)) + brick_margin
        brick_y = (row * (brick_height + brick_margin)) + brick_margin
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick_rect)

# Crea una función para actualizar la posición de la pelota y manejar las colisiones con la plataforma móvil del jugador y los ladrillos:

def update_ball():
    global ball_speed_x, ball_speed_y

    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed_x *= -1

    if ball_rect.top < 0:
        ball_speed_y *= -1

    if ball_rect.bottom > height:
        pygame.quit()
        sys.exit()

    if ball_rect.colliderect(paddle_rect):
        ball_speed_y *= -1
        ball_rect.top = paddle_rect.bottom

    for brick in bricks:
        if ball_rect.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            break

# Crea una función para manejar la entrada del jugador y mover la plataforma móvil:

def handle_input():
    global paddle_rect

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_rect.x -= paddle_speed
    elif keys[pygame.K_RIGHT]:
        paddle_rect.x += paddle_speed

    if paddle_rect.left < 0:
        paddle_rect.left = 0
    elif paddle_rect.right > width:
        paddle_rect.right = width

#Crea un bucle principal para el juego que actualice la posición de la pelota, maneje la entrada del jugador y dibuje los elementos del juego en la pantalla:

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    handle_input()
    update_ball()

    screen.fill(bg_color)
    pygame.draw.rect(screen, paddle_color, paddle_rect)
    pygame.draw.circle(screen, ball_color, ball_rect.center, ball_rect.width // 2)

    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)

    pygame.display.update()

# Ejecuta el juego

if __name__ == '__main__':
    main()