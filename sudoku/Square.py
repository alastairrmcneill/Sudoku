"""
Square class holds the numbers and positon for the sudoku game
"""

import pygame

from sudoku.Constants import (BLACK, FONT, SQUARE_SIZE, WHITE, WIN_HEIGHT,
                              WIN_WIDTH)


class Square:
    def __init__(self, win, value, row, col):
        """
        Init method for Square class

        Arguments:
            win {Surface} -- Pygame surface to draw to
            value {int} -- Number associated with this square
            row {int} -- Row that this is place on the sudoku board
            col {int} -- Column that this is placed to on the sudoku board
        """
        self.win = win
        self.value = value
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.get_top_left_pos()
        self.x_c = 0
        self.y_c = 0
        self.get_center_pos()

    def get_top_left_pos(self):
        """
        Method to find the top left corner of the square
        """
        self.x = self.col * SQUARE_SIZE
        self.y = self.row * SQUARE_SIZE

    def get_center_pos(self):
        """
        Method to find the center of the square
        """
        self.x_c = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y_c = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def set_value(self,value):
        """
        Method to change the value from its initial value

        Arguments:
            value {int} -- Number to chagne it to
        """
        self.value = value

    def draw(self):
        """
        Draws the number to the center of the square
        """
        text = FONT.render(str(self.value), True, BLACK)
        rect = text.get_rect(center = (self.x_c, self.y_c))
        self.win.blit(text, rect)

    def draw_change(self, colour):
        """
        Draws the number to the square as well as the outline to show if the algorithm is progressing or not

        Arguments:
            colour {tuple} -- (R, G, B) Colour for the outline of the box
        """

        pygame.draw.rect(self.win, WHITE, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

        if self.value != 0:
            self.draw()

        pygame.draw.rect(self.win, colour, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE), 2)
        pygame.display.update()
        pygame.time.delay(100)


