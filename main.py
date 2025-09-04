from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
import pygame

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    updatable_group.add(player)
    drawable_group.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        screen.fill("black")

        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()

        # Cap the frame rate at 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
