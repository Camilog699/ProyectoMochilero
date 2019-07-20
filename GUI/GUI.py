import pygame
import subprocess
import os
import ctypes
from Json.JSON import JSON
pygame.init()


class GUI:
    def __init__(self):
        self.draw()
        self.graph = JSON()

    def screen_size(self):
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]), int(line.split()[9][:-1]))
        return size

    def draw(self):
        screen = pygame.display.set_mode(self.screen_size())
        circle = pygame.draw.circle(screen, (0, 0, 0), (10, 20), 1)

        while True:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
            screen.fill((96, 202, 107))
            for i in range(0, len(self.graph.places)):
                self.graph.places[i] = screen.blit(circle, 100+i, 200+i)

            pygame.display.update()
