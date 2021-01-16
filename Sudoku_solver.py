"""
This is a visualiser of a backtracking algorithm that is used to solve a sudoku board.
Author: Alastair McNeill
Started:13th January 2021
Ended: 16th January 2021
"""
import pygame

from sudoku.Constants import WIN_HEIGHT, WIN_WIDTH
from sudoku.Sudoku import Sudoku

BOARD = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sudoku Sovler")

def main():
    """
    Run this function to open the pygame winodw and then use sapcebar to solve the sudoku
    """

    sudoku = Sudoku(WIN, BOARD)
    run = True
    clock = pygame.time.Clock()


    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            sudoku.solve()

        sudoku.draw()

if __name__ == '__main__':
    main()



