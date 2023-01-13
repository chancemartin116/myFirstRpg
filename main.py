import pygame
from game import Game
        
pygame.init()

screenWidth = 700
screenHeight = 350
window = pygame.display.set_mode((screenWidth, screenHeight))

game = Game(
    window=window,
    framesPerSecond=60
)

game.run()