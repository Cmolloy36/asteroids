import pygame
import constants
import player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # print("Starting asteroids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))

    game_player = player.Player(x = constants.SCREEN_WIDTH / 2, 
        y = constants.SCREEN_HEIGHT / 2)

    while True:
        # This makes the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        game_player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000
    
if __name__ == "__main__":
    main()