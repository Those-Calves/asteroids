import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = True

    while game == True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return









    pygame.display.flip(screen)

if __name__ == "__main__":
    main()