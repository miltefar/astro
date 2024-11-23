import circleshape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SHOT_RADIUS
from shots import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.position = pygame.Vector2(x,y)
        self.direction = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot_position = self.position
        new_shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
        direction_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity = direction_vector * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.timer > 0:
            self.timer -= dt
            print(self.timer)
        if keys[pygame.K_a]:
            self.rotate(dt*(-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*(-1))
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

   


