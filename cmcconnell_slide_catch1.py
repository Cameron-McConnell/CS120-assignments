import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PLAYER_SPEED = 5
OBSTACLE_SPEED_RANGE = (3, 8)
GAME_DURATION = 10000  # 10 seconds in milliseconds

# Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slide and Dodge")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Load assets
try:
    background_img = pygame.image.load("castle2.png").convert()
except:
    background_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_img.fill((100, 100, 100))

try:
    player_img = pygame.image.load("black_knight.png").convert_alpha()
except:
    player_img = pygame.Surface((50, 50))
    player_img.fill((255, 0, 0))

try:
    obstacle_img = pygame.image.load("flame.png").convert_alpha()
except:
    obstacle_img = pygame.Surface((30, 30))
    obstacle_img.fill((0, 0, 255))

try:
    crash_sound = pygame.mixer.Sound("click.wav")
except:
    crash_sound = None

# Sprite classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 50))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Keep within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_img
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(*OBSTACLE_SPEED_RANGE)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

# Instruction screen
def show_instructions(last_score):
    while True:
        screen.blit(background_img, (0, 0))
        draw_text_center("Use arrow keys to move and avoid obstacles.", 240)
        draw_text_center(f"Last Score: {last_score}", 280)
        draw_button("Play", 200, 400, 100, 50)
        draw_button("Quit", 350, 400, 100, 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 200 <= x <= 300 and 400 <= y <= 450:
                    return "Play"
                if 350 <= x <= 450 and 400 <= y <= 450:
                    return "Quit"

# Draw text centered
def draw_text_center(text, y):
    label = font.render(text, True, (255, 255, 255))
    rect = label.get_rect(center=(SCREEN_WIDTH//2, y))
    screen.blit(label, rect)

# Draw button
def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, (0, 128, 0), (x, y, w, h))
    label = font.render(text, True, (255, 255, 255))
    label_rect = label.get_rect(center=(x + w//2, y + h//2))
    screen.blit(label, label_rect)

# Game scene
def play_game():
    player = Player()
    obstacles = pygame.sprite.Group()
    for _ in range(10):
        obstacles.add(Obstacle())

    all_sprites = pygame.sprite.Group(player, *obstacles)

    score = 0
    start_time = pygame.time.get_ticks()

    running = True
    while running:
        dt = clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update
        player.update(keys)
        obstacles.update()

        # Check collisions
        hits = pygame.sprite.spritecollide(player, obstacles, False)
        for hit in hits:
            if crash_sound:
                crash_sound.play()
            hit.reset()
            score -= 1

        # Draw
        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)

        # Draw score and time
        elapsed_time = pygame.time.get_ticks() - start_time
        time_left = max(0, (GAME_DURATION - elapsed_time) // 1000)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        time_text = font.render(f"Time Left: {time_left}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        screen.blit(time_text, (500, 20))

        pygame.display.flip()

        if elapsed_time >= GAME_DURATION:
            print(f"Final Score: {score}")
            running = False

    return score

# Main loop
def main():
    last_score = 0
    while True:
        response = show_instructions(last_score)
        if response == "Play":
            last_score = play_game()
        else:
            break

    pygame.quit()

if __name__ == "__main__":
    main()
