"""
Player class - represents the player character
"""

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initialize the player"""
        super().__init__()
        
        # Create a simple colored rectangle as the player
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # Movement variables
        self.speed = 5
        self.vel_x = 0
        self.vel_y = 0
    
    def handle_input(self):
        """Handle player input"""
        keys = pygame.key.get_pressed()
        
        self.vel_x = 0
        self.vel_y = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel_y = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel_y = self.speed
    
    def update(self):
        """Update player position"""
        self.handle_input()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Keep player on screen (basic boundary check)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
