"""
Basic Game Setup - Project Nova
Main game loop and entry point
"""

import pygame
import sys
from game import Game

def main():
    """Initialize and run the game"""
    pygame.init()
    
    # Game configuration
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    
    # Create game instance
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
    
    # Run the game loop
    game.run()
    
    # Cleanup
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
