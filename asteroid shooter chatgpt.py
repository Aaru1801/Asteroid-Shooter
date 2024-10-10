import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# Load images
player_image = pygame.image.load("../graphics/ship.png").convert_alpha()
asteroid_image = pygame.image.load("../graphics/meteor.png").convert_alpha()
laser_image = pygame.image.load("../graphics/laser.png").convert_alpha()
bg_surf = pygame.image.load('../graphics/background.png').convert()

# Player setup
player_rect = player_image.get_rect(midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 10))
PLAYER_SPEED = 5

# Laser setup
lasers = []
LASER_SPEED = 8

# Asteroid setup
asteroids = []
SPAWN_RATE = 60  # Spawn asteroid every 1 second

# Fonts
font = pygame.font.Font(None, 36)

def spawn_asteroid():
    x = random.randint(0, WINDOW_WIDTH - asteroid_image.get_width())
    y = -asteroid_image.get_height()
    asteroid_rect = asteroid_image.get_rect(topleft=(x, y))
    asteroids.append(asteroid_rect)

def main():
    global player_rect, lasers, asteroids

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_rect.x += PLAYER_SPEED

        # Shooting lasers
        if keys[pygame.K_SPACE]:
            laser_rect = laser_image.get_rect(midtop=player_rect.midtop)
            lasers.append(laser_rect)

        # Update lasers
        for laser in lasers:
            laser.y -= LASER_SPEED
            if laser.y < 0:
                lasers.remove(laser)

        # Spawn asteroids
        if random.randint(0, SPAWN_RATE) == 0:
            spawn_asteroid()

        # Update asteroids
        for asteroid in asteroids:
            asteroid.y += 2
            if asteroid.colliderect(player_rect):
                pygame.quit()
                sys.exit()

        # Check for laser-asteroid collisions
        for laser in lasers:
            for asteroid in asteroids:
                if laser.colliderect(asteroid):
                    lasers.remove(laser)
                    asteroids.remove(asteroid)

        # Draw Background
        screen.fill((0, 0, 0))
        screen.blit(bg_surf,(0,0))

        # Draw player
        screen.blit(player_image, player_rect)

        # Draw lasers
        for laser in lasers:
            screen.blit(laser_image, laser)

        # Draw asteroids
        for asteroid in asteroids:
            screen.blit(asteroid_image, asteroid)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
