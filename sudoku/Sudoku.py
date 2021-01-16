"""
The sudoku class, holds the baord, and solving method
"""

import pygame

from sudoku.Constants import (BLACK, GREEN, RED, SQUARE_SIZE, WHITE,
                              WIN_HEIGHT, WIN_WIDTH)
from sudoku.Square import Square


class Sudoku:
    def __init__(self, win, starting_board):
        """
        Init method for Sudoku class

        Arguments:
            win {surface} -- Pygame surface to draw to
            starting_board {list[list[int]]} -- 2D list of numbers representing the board
        """
        self.win = win
        self.rows = len(starting_board)
        self.cols = len(starting_board[0])
        self.board = [[Square(self.win, starting_board[i][j], i, j) for j in range(self.cols)] for i in range(self.rows)]
        self.selected = None


    def print_board(self):
        """
        Prints the board in a readable format to the command line. Used for testing
        """
        for i in range(self.rows):
            if i % 3 == 0 and i != 0:
                print('----------------------')
            for j in range(self.cols):
                if j % 3 == 0 and j != 0:
                    print('| ', end='')
                print(str(self.board[i][j].value) + ' ', end='')
                if j == self.cols - 1:
                    print('\n', end ='')


    def solve(self):
        """
        Backtracking method to solve the baord

        Returns:
            Boolean -- Returns True if reached the end of the board and false if none of the numbers were valid in this square
        """
        pos = self.first_empty_square()

        if pos == None:
            return True

        i, j = pos

        for num in range(1,10):
            if self.isValid(num, i, j):
                self.board[i][j].set_value(num)
                self.board[i][j].draw_change(GREEN)

                if self.solve():
                    return True

                self.board[i][j].set_value(0)
                self.board[i][j].draw_change(RED)
        return False


    def isValid(self, num, row, col):
        """
        Checks the board to see if the given number is valid in the given square per normal sudoku rules

        Arguments:
            num {int} -- Value that you are testing against
            row {int} -- Row to check
            col {int} -- Coloumn to check

        Returns:
            Boolean -- True if valid, False if not
        """
        # Check row
        for j in range(self.cols):
            if self.board[row][j].value == num:
                return False

        # Check col
        for i in range(self.rows):
            if self.board[i][col].value == num:
                return False

        # Check 3x3 square
        box_x = row // 3
        box_y = col // 3

        for i in range(3):
            for j in range(3):
                if self.board[3 * box_x + i][3 * box_y + j].value == num:
                    return False

        return True

    def first_empty_square(self):
        """
        Finds the first empty square on the board

        Returns:
            tuple -- (row, col) Gives the position of the first empty square
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].value == 0:
                    return (i,j)
        return None

    def select(self, mouse):
        pos = self.get_row_col_from_mouse(mouse)

        if pos != None:
            if not self.board[pos[0]][pos[1]].original:
                if self.selected == pos:
                    self.board[pos[0]][pos[1]].deselect()
                    self.selected = None
                else:
                    self.board[pos[0]][pos[1]].select()
                    if self.selected != None:
                        self.board[self.selected[0]][self.selected[1]].deselect()
                    self.selected = pos
            else:
                pos = self.selected
                if pos != None:
                    self.board[pos[0]][pos[1]].deselect()
                    self.selected = None


    def get_row_col_from_mouse(self, mouse):
        if mouse[0] < self.win.get_width() and mouse[1] < self.win.get_height():
            row = mouse[1] // SQUARE_SIZE
            col = mouse[0] // SQUARE_SIZE

            return (row, col)
        return None

    def play(self, num):
        if self.selected != None:
            if num > 0 and num < 10:
                row, col = self.selected
                self.board[row][col].set_value(num)
                self.board[row][col].deselect()
                self.selected = None


    def delete(self):
        if self.selected != None:
            row, col = self.selected
            self.board[row][col].set_value(0)
            self.board[row][col].deselect()
            self.selected = None

    def check_board(self):
        board = self.get_board_values()
        for row in board:
            if len(row) != len(set(row)):
                return False

        for col in board:
            if len(col) != len(set(col)):
                return False

        for x in range(3):
            for y in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[3 * x + i][3 * y + j])
                if len(box) != len(set(box)):
                    return False

        return True

    def get_board_values(self):
        board = []
        for row in self.board:
            r = []
            for elem in row:
                r.append(elem.value)
            board.append(r)
        return board

    def draw(self):
        """
        Draw this board to the screen
        """
        self.win.fill(WHITE)
        self.draw_lines()
        self.draw_squares()
        pygame.display.update()

    def draw_lines(self):
        """
        Draw the lines to the screen
        """
        for i in range(len(self.board) + 1):
            if i == 0 or i % 3 == 0:
                thickness = 6
            else:
                thickness = 1
            pygame.draw.line(self.win, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIN_HEIGHT), thickness)
            pygame.draw.line(self.win, BLACK, (0, i * SQUARE_SIZE), (WIN_WIDTH, i * SQUARE_SIZE), thickness)

    def draw_squares(self):
        """
        Draw the numbers to the screen
        """
        for row in self.board:
            for square in row:
                square.draw()
