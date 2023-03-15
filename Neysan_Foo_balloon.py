import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (135, 206, 250)
CANNON_COLOR = (139, 69, 19)
BALLOON_COLOR = (255, 0, 0)
BULLET_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)

# Initialize the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Shooting Game")

# Initialize game clock
clock = pygame.time.Clock()

# Load font for countdown and score display
font = pygame.font.Font(None, 36)

# Cannon class
class Cannon:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, CANNON_COLOR, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, CANNON_COLOR, (self.x - self.width // 2, self.y + self.height // 4, self.width // 2, self.height // 2))

# Balloon class
class Balloon:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 1
        self.direction = random.choice([-1, 1])

    def move(self):
        if random.random() < 0.01:  # 1% chance to change direction
            self.direction *= -1

        self.y += self.direction * self.speed

        # Keep the balloon within the screen boundaries
        if self.y <= self.radius:
            self.y = self.radius
            self.direction = 1
        elif self.y >= HEIGHT - self.radius * 2:
            self.y = HEIGHT - self.radius * 2
            self.direction = -1

    def draw(self, screen):
        pygame.draw.circle(screen, BALLOON_COLOR, (self.x, self.y), self.radius)
        pygame.draw.aaline(screen, (0, 0, 0), (self.x, self.y + self.radius), (self.x, self.y + self.radius * 2))

# Bullet class
class Bullet:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.speed = -10

    def move(self):
        self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BULLET_COLOR, (self.x, self.y, self.height, self.height))

# Game loop
cannon = Cannon(WIDTH - 150, 250, 60, 30)  # Updated cannon height to match bullet height
balloon = Balloon(100, 200, 25)
bullets = []

missed_shots = 0
game_over = False

while not game_over:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(cannon.x - cannon.width // 2, cannon.y + cannon.height // 4, cannon.height // 2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and cannon.y > 0:
        cannon.y -= 5
    if keys[pygame.K_DOWN] and cannon.y < HEIGHT - cannon.height:
        cannon.y += 5

    screen.fill(BG_COLOR)

    cannon.draw(screen)
    balloon.move()
    balloon.draw(screen)

    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(screen)
        if bullet.x < 0:
            bullets.remove(bullet)
            missed_shots += 1

        if (balloon.x - balloon.radius < bullet.x < balloon.x + balloon.radius) and (balloon.y - balloon.radius < bullet.y < balloon.y + balloon.radius):
            game_over = True
            break

    pygame.display.flip()

# Prepare Game Over text and final score
game_over_text = font.render("Game Over!", True, FONT_COLOR)
final_score_text = font.render(f"Missed shots: {missed_shots}", True, FONT_COLOR)

# Display Game Over text and final score
screen.fill(BG_COLOR)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height()))
pygame.display.flip()

# Wait for 2 seconds
pygame.time.delay(2000)

pygame.quit()