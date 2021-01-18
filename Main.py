"""
This is a visualiser of a backtracking algorithm that is used to solve a sudoku board.
Author: Alastair McNeill
Started:13th January 2021
Ended: 16th January 2021
"""
import pygame

from sudoku.Constants import WIN_HEIGHT, WIN_WIDTH, BLACK, WHITE, GREY, BG_IMG
from sudoku.Sudoku import Sudoku
from sudoku.Data_Manager import Data_Manager
from sudoku.Menu import Menu


WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sudoku Sovler")
data_manager = Data_Manager()

def setup_menu():
    menu = Menu(WIN, data_manager, BG_IMG)
    menu.add_button("Hard", (WIN_WIDTH // 2 - 75, WIN_HEIGHT - 75, 150, 50), GREY, BLACK, WHITE)
    menu.add_button("Medium", (WIN_WIDTH // 2 - 75, WIN_HEIGHT - 150, 150, 50), GREY, BLACK, WHITE)
    menu.add_button("Easy", (WIN_WIDTH // 2 - 75, WIN_HEIGHT - 225, 150, 50), GREY, BLACK, WHITE)
    menu.add_text_box("<ESC> for main menu \n <ENTER> to check board \n <SPACE> to solve board for you", BLACK, (WIN_WIDTH // 2 , 275))
    return menu


def main():
    """
    Run this function to open the pygame winodw and then use sapcebar to solve the sudoku
    """

    menu = setup_menu()
    menu.run()

    sudoku = Sudoku(WIN,data_manager)
    run = True
    clock = pygame.time.Clock()


    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                sudoku.select(pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            main()
        if keys[pygame.K_SPACE]:
            sudoku.solve()
        if keys[pygame.K_DELETE]:
            sudoku.delete()
        if keys[pygame.K_RETURN]:
            if not sudoku.ended:
                sudoku.check_board()
            else:
                sudoku.reset()
        if keys[pygame.K_1]:
            sudoku.play(1)
        if keys[pygame.K_2]:
            sudoku.play(2)
        if keys[pygame.K_3]:
            sudoku.play(3)
        if keys[pygame.K_4]:
            sudoku.play(4)
        if keys[pygame.K_5]:
            sudoku.play(5)
        if keys[pygame.K_6]:
            sudoku.play(6)
        if keys[pygame.K_7]:
            sudoku.play(7)
        if keys[pygame.K_8]:
            sudoku.play(8)
        if keys[pygame.K_9]:
            sudoku.play(9)


        sudoku.draw()

if __name__ == '__main__':
    main()



