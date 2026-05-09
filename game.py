"""
Game class - handles main game logic and loop
"""

import pygame
from player import Player

class Game:
    def __init__(self, width, height, fps):
        """Initialize the game"""
        self.screen_width = width
        self.screen_height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Project Nova")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game objects
        self.player = Player(width // 2, height // 2)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
    
    def handle_events(self):
        """Handle user input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        """Update game logic"""
        self.all_sprites.update()
    
    def render(self):
        """Render the game"""
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
