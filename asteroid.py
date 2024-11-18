import pygame
import circleshape
import constants

class Asteroid(circleshape.CircleShape):
        def __init__(self, x, y, radius):
            super().__init__(x, y, radius) # Initialize parent class properly
            self.position = pygame.Vector2(x, y) # Use a vector for position
            self.velocity = pygame.Vector2(0, 1) # Define an initial velocity

        def draw(self,screen):
            pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

        def update(self,dt):
           self.position += self.velocity * dt
            
