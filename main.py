import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
import pygame

from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    shots_groups = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()

    Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
    AsteroidField.containers = (updatable_group)
    Player.containers = (updatable_group, drawable_group)
    Shot.containers = (updatable_group, drawable_group, shots_groups)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects
        updatable_group.update(dt)

        screen.fill("black")

        # Draw all drawables
        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()

        # Check for collisions
        for asteroid in asteroids_group:
            if asteroid.has_overlap(player):
                print("Game over!")
                sys.exit()

        # Cap the frame rate at 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
