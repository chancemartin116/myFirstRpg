import pygame
import random

class Enemy(pygame.sprite.Sprite):
    RIGHT = 0
    LEFT = 1
    
    def __init__(self, window: pygame.surface.Surface):
        super().__init__()
        self.window = window
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()     
        self.position = pygame.math.Vector2(237, 237)
        self.rect.midbottom = self.position
        self.isAlive = True
            
    def render(self):
        if self.isAlive:
            self.window.blit(self.image, (self.position.x, self.position.y))
            