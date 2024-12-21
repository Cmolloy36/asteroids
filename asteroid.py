import pygame
import random
import constants
import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255, 255, 255),self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * (1 + dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20,50)
            dir1 = self.velocity.rotate(rand_angle)
            # 2*rand_angle if rotate method changes self attribute
            dir2 = self.velocity.rotate(-2*rand_angle)

            as1 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
            as1.velocity = 1.2 * dir1

            as2 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
            as2.velocity = 1.2 * dir2
