import pygame

class FightMenu:
    def __init__(self, window):
        self.font = pygame.font.SysFont('Arial', 20)
        self.menu = pygame.draw.rect(window, 'white',
                   (40, 80, 200, 80), width=0, border_radius=20) 
        window.blit(self.font.render('Attack', True, 'black'), (40, 80))
        