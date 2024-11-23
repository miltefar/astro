import circleshape
from constants import SHOT_RADIUS
import pygame


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x,y)
        self.position = pygame.Vector2(x, y) # Use a vector for position
        self.velocity = pygame.Vector2(0, 1) # Define an initial velocity
        self.radius = SHOT_RADIUS

    def draw(self,screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 3)

    def update(self,dt):
        self.position += self.velocity * dt
