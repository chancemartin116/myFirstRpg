import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, window: pygame.surface.Surface):
        super().__init__()
        self.window = window
        self.image = pygame.image.load("Background.png")        
        self.x = 0
        self.y = 0
 
    def render(self):
        self.window.blit(self.image, (self.x, self.y))