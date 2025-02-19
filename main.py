import pygame
import constants

def main():
    pygame.init
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()


print("Starting asteroids!")



if __name__ == "__main__":
    main() 



