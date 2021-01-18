"""
The file for menu items containing the Menu, Button and Slider classes
"""
import pygame

from sudoku.Constants import FONT, SMALL_FONT

class Menu:
    def __init__(self, window, data_manager, bg_img):

        self.win = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.data_manager = data_manager
        self.bg_img = bg_img
        self.clock = pygame.time.Clock()
        self.buttons = []
        self.text_boxes = []

    def run(self):

        run = True

        while run:
            self.clock.tick(20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

            for button in self.buttons:
                button.run()
                if button.done:
                    return

            self.draw()

    def reset(self):
        for button in self.buttons:
            button.done = False

    def add_button(self, text, rect, active_colour, inactive_colour, text_colour):
        """
        Adds a button to the window button

        Arguments:
            text {str} -- Text to be shown in the middle of the button
            rect {tuple} -- (x, y, w, h) Rectangle describing the size and position of the button
            active_colour {tuple} -- (R, G, B) The colour when mouse is over the button
            inactive_colour {tuple} -- (R, G, B) The colour when mouse is not over the button
            text_colour {tuple} -- (R, G, B) The colour of the text
        """

        self.buttons.append(Button(self.data_manager, text, rect, active_colour, inactive_colour, text_colour))

    def add_text_box(self,text, colour, mid_top):
        """
        Add a Text box object to the menu

        Arguments:
            text {string} -- Text you want to display
            colour {tuple} -- (R, G, B) Colour of the text
            mid_top {tuple} -- (x, y) Position of the center top of the text box
        """
        self.text_boxes.append(Text_Box(text, colour, mid_top))

    def draw(self):
        """
        Draw the menu to the screen
        """
        self.win.fill((255,255,255))
        self.bg_img.fill((255, 255, 255))
        self.win.blit(self.bg_img, (0, 0))
        self.draw_buttons()
        self.draw_text_boxes()

        pygame.display.update()

    def draw_buttons(self):
        """
        Loop throough all the buttons and draw them
        """
        for button in self.buttons:
            button.draw(self.win)

    def draw_text_boxes(self):
        """
        Loop through all the buttons and drawm them
        """
        for text_box in self.text_boxes:
            text_box.draw(self.win)


class Button:
    def __init__(self, data_manager, text, rect, active_colour, inactive_colour, text_colour):

        self.data_manager = data_manager
        self.button_text = text
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]
        self.rect = rect
        self.active_colour = active_colour
        self.inactive_colour = inactive_colour
        self.colour = self.inactive_colour
        self.text_colour = text_colour
        self.done = False

    def run(self):
        """
        Function to execute when main menu loop runs. Determines what to do when clicked
        """
        pos = pygame.mouse.get_pos()
        if self.mouse_over(pos):
            self.colour = self.active_colour
            if pygame.mouse.get_pressed()[0] == 1:
                self.data_manager.set_difficulty(self.button_text)
                self.done = True
        else:
            self.colour = self.inactive_colour

    def mouse_over(self, pos):
        """
        Check if the mouse is over the button

        Arguments:
            pos {tuple} -- (x,y) Position of the mouse on the screen

        Returns:
            boolean -- If the mouse is over the button
        """
        return pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height


    def draw(self, screen):
        """
        Draw the button to the screen

        Arguments:
            screen {surface} -- Pygame surface to draw on to
        """
        pygame.draw.rect(screen, self.colour, self.rect)

        text = FONT.render(self.button_text, True, self.text_colour)
        text_rect = text.get_rect(center = ((self.x + self.width // 2), (self.y + self.height // 2)))
        screen.blit(text, text_rect)
        self.is_highlighted = False

class Text_Box:
    def __init__(self, text, colour, mid_top):
        """
        Init method for text box

        Arguments:
            text {string} -- Text to be displayed
            colour {tuple} -- (R, G, B) Colour to display text
            mid_top {tuple} -- (x, y) Mid top point of the text box
        """
        self.text = text
        self.colour = colour
        self.mid_top = mid_top
        self.x = self.mid_top[0]
        self.y = self.mid_top[1]

    def draw(self, screen):
        """
        Draw the text box to the screen

        Arguments:
            screen {surface} -- Pygame surface to draw to
        """
        lines = self.text.splitlines()

        y = self.y

        for line in lines:
            text = SMALL_FONT.render(line, True, self.colour)
            rect = text.get_rect(midtop = (self.x, y))
            screen.blit(text, rect)

            y = y + text.get_height() + 5
