"""
Constants for the game of Sudoku
"""

import pygame
import os

pygame.font.init()

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen dimensions
SCREEN_WIDTH = SCREEN_HEIGHT = 542
SQUARE_SIZE = SCREEN_HEIGHT // 9
WIN_WIDTH = SCREEN_WIDTH
WIN_HEIGHT = SCREEN_HEIGHT + 100

# Font
FONT = pygame.font.SysFont("Arial", 35)
SMALL_FONT = pygame.font.SysFont("Arial", 25)
NUMBERS_FONT = pygame.font.SysFont("Chewed Pen BB", 40)

# Paths
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# Imgs
BG_IMG = pygame.image.load(os.path.join(BASE_PATH, "imgs/bg.png"))
