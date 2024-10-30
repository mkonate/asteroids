import pygame
import sys
from asteroidfield import AsteroidField
from asteroids import Asteroid
from constants import *
from player import Player
from shot import Shot


def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers =(updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over")
                sys.exit(0)

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

if __name__ == '__main__':
    main()
