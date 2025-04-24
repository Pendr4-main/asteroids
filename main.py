# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField




def main():


    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")

                time.sleep(2)

                sys.exit()
        pygame.display.flip()
        
       
    pygame.quit()

if __name__ == "__main__":
    main()