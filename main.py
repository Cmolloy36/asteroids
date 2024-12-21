import pygame
import constants

def main():
    pygame.init()
    # print("Starting asteroids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    
    while True:
        # This makes the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
    
if __name__ == "__main__":
    main()