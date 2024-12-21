import circleshape
import constants
import pygame

class Shot(circleshape.CircleShape):
    def __init__(self,x,y,radius=constants.SHOT_RADIUS):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255, 255, 255),self.position,self.radius,width=2)
    
    def update(self, dt):
        self.position += self.velocity * (1 + dt)
        # print(f'pos: {self.position}, velo: {self.velocity}')