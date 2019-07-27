
import pygame


# Class that create a rect that allows meet the mouse position.
class Cursor(pygame.Rect):
    def __init__(self):
        super(Cursor, Cursor).__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()