import pygame
import sys
from pygame.locals import *
import random, time
from background import Background
from ground import Ground
from player import Player
from enemy import Enemy

class Game:
    
    def __init__(self, window: pygame.surface.Surface, framesPerSecond):
        self.background = Background(window)
        self.ground = Ground(window, center=(350, 350))
        self.enemy = Enemy(window)
        self.player = Player(window)
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(self.player)
        self.framesPerSecond = framesPerSecond
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            self.runGame()
    
    def runGame(self):
        self.handleEvents()
        self.render()
        pygame.display.update()
        self.clock.tick(self.framesPerSecond)
        
    def handleEvents(self):
        for event in pygame.event.get():  
            self.handleEvent(event)
                
    def render(self):
        self.background.render()
        self.ground.render()
        self.player.render()
        self.enemy.render()
        
    def handleEvent(self, event: pygame.event.Event):
        if event.type == QUIT:
            self.quit()
        if self.isPlayerAttackEvent(event):
            self.executePlayerAttack()
                                  
    def quit(self):
        pygame.quit()
        sys.exit()
        
    def isPlayerAttackEvent(self, event):
        return event.type == KEYDOWN and event.key == K_RETURN
    
    def executePlayerAttack(self):
        if not self.player.isAttacking:
            self.player.attack()
            self.player.isAttacking = True 
        if self.didCollisionOccur():
            self.enemy.isAlive = False
                
    def didCollisionOccur(self):
        if self.player.direction == 'RIGHT':
            diff = self.enemy.rect.left - self.player.rect.right 
            return diff > -20 and diff < 11
        else:
            diff = self.player.rect.left - self.enemy.rect.right 
            return diff > 15 and diff < 31

        
        
