import pygame
from constants import *
import player
import circleshape

def main():
    pygame.init()
    theScreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    theGameClock = pygame.time.Clock()
    dt = 0
    thePlayer = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        theScreen.fill(000000)
        thePlayer.update(dt)
        thePlayer.draw(theScreen)


        pygame.display.flip()
        theGameClock.tick(60)
        dt = theGameClock.tick(60) / 1000
     

if __name__ == "__main__":
    main()
