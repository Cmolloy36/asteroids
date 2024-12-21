import pygame
import player

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen,(255, 255, 255),player.Player.triangle(self),width=2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self,other):
        # distance_coords = (self.position - other.position)
        # distance = (distance_coords.x**2 + distance_coords.y**2)**1/2
        distance= pygame.math.Vector2.distance_to(self.position,other.position)
        if self.radius + other.radius >= distance:
            return True
        else:
            return False