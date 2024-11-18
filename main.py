import pygame
from constants import *
import player
import circleshape
import asteroid
import asteroidfields
import sys

def main():
    pygame.init()
    theScreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    theGameClock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()   
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    dt = 0
    asteroidfields.AsteroidField.containers = (updatable,)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    theAsteroidField = asteroidfields.AsteroidField()

    thePlayer = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        theScreen.fill(000000)
       
        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            if thing.collisionCheck(thePlayer):  
                sys.exit("Game Over!")
        for thing in drawable:
            thing.draw(theScreen)


        pygame.display.flip()
        theGameClock.tick(60)
        dt = theGameClock.tick(60) / 1000.0
     

if __name__ == "__main__":
    main()
