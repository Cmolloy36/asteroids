import circleshape
import constants
import pygame
import shot

class Player(circleshape.CircleShape):
    # containers = (updatable,drawable)
    # could add containers here, but would need to create group instances here too... I think

    def __init__(self,x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = constants.PLAYER_SHOOT_COOLDOWN

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += dt*constants.PLAYER_TURN_SPEED


    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer < 0:
            self.shoot()
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
        

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        projectile = shot.Shot(self.position.x, self.position.y)
        projectile.velocity = pygame.math.Vector2(0,1)
        projectile.velocity = projectile.velocity.rotate(self.rotation)
        projectile.velocity *= constants.PLAYER_SHOOT_SPEED
        # print(f'player script velo: {projectile.velocity}')