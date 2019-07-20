import pygame
import subprocess
import os
import sys
import ctypes
from Json.JSON import JSON
from random import randint
pygame.init()


class GUI:
    def __init__(self, graph):
        self.graph = graph
        self.draw()

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
        country = pygame.image.load("Imgs/city.png")
        country = pygame.transform.scale(country, (85, 60))
        self.positions()
        while True:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((96, 202, 107))

            for edge in self.graph.edges:
                initX = edge.vertexA.x
                initY = edge.vertexA.y
                desX = edge.vertexB.x
                desY = edge.vertexB.y
                pygame.draw.line(screen, (0, 0, 0),
                                 (initX+20, initY+40), (desX+20, desY+40), 5)

            for place in self.graph.places:
                name = place.name
                screen.blit(
                    country, (place.x, place.y))
                screen.blit(name, (place.x+20, place.y+40))

            pygame.display.update()

    def positions(self):
        size = self.screen_size()
        i = 0
        while i < len(self.graph.places):
            place = self.graph.places[i]
            posx = randint(0, size[0]-100)
            posy = randint(0, size[1]-100)
            if place is self.graph.places[0]:
                place.x = posx
                place.y = posy
            elif self.dont_hover(posx, posy):
                place.x = posx
                place.y = posy
            else:
                i = i - 1
            i = i+1

    def dont_hover(self, x, y):
        pas = True
        for place in self.graph.places:
            if x == place.x and y == place.y:
                pas = False
                break
            elif x + 50 == place.x and y + 50 == place.y:
                pas = False
                break
            elif x + 50 == place.x and y - 50 == place.y:
                pas = False
                break
            elif x - 50 == place.x and y + 50 == place.y:
                pas = False
                break
            elif x - 50 == place.x and y - 50 == place.y:
                pas = False
                break

        return pas
