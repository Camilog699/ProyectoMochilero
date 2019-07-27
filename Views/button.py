import pygame

# Class that allows create a button in pygame.


class ButtonP(pygame.sprite.Sprite):

    def __init__(self, up, down, x, y):
        super(ButtonP, ButtonP).__init__(self)
        self.normal = up
        self.selection = down
        self.current = self.normal
        self.rect = self.current.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.x = x
        self.y = y

