import pygame
import constants

from player import Player 

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
print("Starting asteroids!")





if __name__ == "__main__":
    main() 




    # source venv/bin/activate --> to activate virtual machine for pygame

