import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, window, center: tuple):
        super().__init__()
        self.window = window
        self.image = pygame.image.load("Ground.png")
        self.rect = self.image.get_rect(center=center)
 
    def render(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y)) 