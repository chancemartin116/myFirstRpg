import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    POSITION_INCREMENT_FOR_MOVEMENT = 3
    
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pygame.image.load("Player_Sprite_R.png")
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2((335, 295))
        self.movementImageNumber = 0
        self.attackingImageNumber = 0
        self.direction = 'RIGHT'
        self.isAttacking = False
        self.leftMovementImages = self.getImagesForMovementToTheLeft()
        self.rightMovementImages = self.getImagesForMovementToTheRight()
        self.leftAttackingImages = self.getImagesForAttackingToTheLeft()
        self.rightAttackingImages = self.getImagesForAttackingToTheRight()
        
    def render(self):
        if self.movementImageNumber > 6:
            self.movementImageNumber = 0
        if self.isAttacking:
            self.attack()
        self.move()
        self.window.blit(self.image, self.rect)
        
    def attack(self):   
        if self.attackingImageNumber > 10:
            self.attackingImageNumber = 0
            self.isAttacking = False
        if self.direction == "RIGHT":
            self.image = self.rightAttackingImages[self.attackingImageNumber]
        elif self.direction == "LEFT":
            self.correctLeftFacingAttackImage()
            self.image = self.leftAttackingImages[self.attackingImageNumber] 
        self.attackingImageNumber += 1
        
    def move(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_LEFT]:
            self.moveLeft()
        if pressedKeys[K_RIGHT]:
            self.moveRight()
        self.rect.midbottom = self.position 
        
    def moveLeft(self):
        self.direction = 'LEFT'
        self.position.x -= Player.POSITION_INCREMENT_FOR_MOVEMENT
        self.image = self.leftMovementImages[self.movementImageNumber]
        self.movementImageNumber += 1
        
    def moveRight(self):
        self.direction = 'RIGHT'
        self.position.x += Player.POSITION_INCREMENT_FOR_MOVEMENT 
        self.image = self.rightMovementImages[self.movementImageNumber]
        self.movementImageNumber += 1

    def correctLeftFacingAttackImage(self):
        if self.attackingImageNumber == 1:
            self.position.x -= 20
        if self.attackingImageNumber == 10:
            self.position.x += 20
        
    def getImagesForMovementToTheRight(self):
        return [pygame.image.load("Player_Sprite_R.png"), pygame.image.load("Player_Sprite2_R.png"),
            pygame.image.load("Player_Sprite3_R.png"),pygame.image.load("Player_Sprite4_R.png"),
            pygame.image.load("Player_Sprite5_R.png"),pygame.image.load("Player_Sprite6_R.png"),
            pygame.image.load("Player_Sprite_R.png")]
 
    def getImagesForMovementToTheLeft(self):
        return [pygame.image.load("Player_Sprite_L.png"), pygame.image.load("Player_Sprite2_L.png"),
            pygame.image.load("Player_Sprite3_L.png"),pygame.image.load("Player_Sprite4_L.png"),
            pygame.image.load("Player_Sprite5_L.png"),pygame.image.load("Player_Sprite6_L.png"),
            pygame.image.load("Player_Sprite_L.png")]
        
    def getImagesForAttackingToTheRight(self):
        return [pygame.image.load("Player_Sprite_R.png"), pygame.image.load("Player_Attack_R.png"),
            pygame.image.load("Player_Attack2_R.png"),pygame.image.load("Player_Attack2_R.png"),
            pygame.image.load("Player_Attack3_R.png"),pygame.image.load("Player_Attack3_R.png"),
            pygame.image.load("Player_Attack4_R.png"),pygame.image.load("Player_Attack4_R.png"),
            pygame.image.load("Player_Attack5_R.png"),pygame.image.load("Player_Attack5_R.png"),
            pygame.image.load("Player_Sprite_R.png")]
 
    def getImagesForAttackingToTheLeft(self): 
        return [pygame.image.load("Player_Sprite_L.png"), pygame.image.load("Player_Attack_L.png"),
            pygame.image.load("Player_Attack2_L.png"),pygame.image.load("Player_Attack2_L.png"),
            pygame.image.load("Player_Attack3_L.png"),pygame.image.load("Player_Attack3_L.png"),
            pygame.image.load("Player_Attack4_L.png"),pygame.image.load("Player_Attack4_L.png"),
            pygame.image.load("Player_Attack5_L.png"),pygame.image.load("Player_Attack5_L.png"),
            pygame.image.load("Player_Sprite_L.png")]