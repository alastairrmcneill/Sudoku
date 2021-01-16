# Sudoku-Solver
## Overview
In this application I have greated a solver for any given partially solved sudoku board using a backtracking algorithm in Python. In tihs alogrithm, rather than burte forcing the full board, you try solving the problem through a recursive method. Firstly try placing a number in an empty square, if it is currently valid then move on to the next empty square and place a number there and so on. If the number is not valid then you try the next number in sudoku, if you have tried 9 and it is not valid then that lets us know that a previous number that got placed was not correct. From there we go back and then increment the last correct number. If was also a 9 then we go back more steps and so on.   

Link explaining the [backtracking alogrithm](https://www.geeksforgeeks.org/backtracking-algorithms/).

To display this to the user I have utilised the module pygame to build a GUI

## Requirements
Python 3.x
pygame

## How to use
Run the Sudoku_solver.py file. When you run the code in Python you'll be met by a partially solved board. Press the spacebar to start the solver.  
In the future I'm going to incorporate this into a sudoku where you can fully play the game, create boards and check solutions
