import pygame
import sys

import constants
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # print("Starting asteroids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)

    game_player = player.Player(x = constants.SCREEN_WIDTH / 2, 
        y = constants.SCREEN_HEIGHT / 2)
    
    field = asteroidfield.AsteroidField()

    while True:
        # This makes the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if game_player.collide(item):
                sys.exit('Game Over!')

            for projectile in shots:
                if projectile.collide(item):
                    item.kill()
                    projectile.kill()
                
        
        pygame.Surface.fill(screen, (0,0,0))
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
    
if __name__ == "__main__":
    main()