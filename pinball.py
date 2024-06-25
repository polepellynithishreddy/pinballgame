import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 15
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_Y = HEIGHT - 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball Game")

# Ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.vx = random.choice([-4, 4])
        self.vy = -4

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.vx = -self.vx

        if self.y <= BALL_RADIUS:
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_RADIUS)

# Paddle class
class Paddle:
    def __init__(self):
        self.x = WIDTH // 2 - PADDLE_WIDTH // 2
        self.y = PADDLE_Y
        self.vx = 0

    def move(self):
        self.x += self.vx
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - PADDLE_WIDTH:
            self.x = WIDTH - PADDLE_WIDTH

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Initialize game objects
ball = Ball()
paddle = Paddle()

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.vx = -8
            elif event.key == pygame.K_RIGHT:
                paddle.vx = 8
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                paddle.vx = 0

    ball.move()
    paddle.move()

    # Ball and paddle collision
    if paddle.y < ball.y + BALL_RADIUS < paddle.y + PADDLE_HEIGHT and paddle.x < ball.x < paddle.x + PADDLE_WIDTH:
        ball.vy = -ball.vy

    # Check if ball hits bottom
    if ball.y > HEIGHT:
        running = False

    # Draw everything
    screen.fill(BLACK)
    ball.draw()
    paddle.draw()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
