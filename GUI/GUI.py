import pygame
import subprocess
import os
import sys
import ctypes
from Json.JSON import JSON
from random import randint
from Views.cursor import Cursor
from Views.button import ButtonP
pygame.init()


class GUI:
    def __init__(self, graph):
        self.graph = graph
        self.cursor = Cursor()
        self.MinMoney = False
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
        # Places position
        self.position()

        # screen
        screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption('Backpacker')

        # fontDs
        fontD = pygame.font.SysFont("Times new Roman", 11)
        fontP = pygame.font.SysFont("Times new Roman", 20)

        # labels to use
        MinMoneyLabel = fontD.render("Way whit minMoney", True, (0, 0, 0))

        # images
        country = pygame.image.load("Imgs/city.png")
        country = pygame.transform.scale(country, (85, 60))
        image1 = pygame.image.load("Imgs/boton1.png")
        image1 = pygame.transform.scale(image1, (130, 60))

        # Buttons
        button1 = ButtonP(image1, image1, 40, 40)

        # main elements
        cursor = Cursor()

        # elements by animation
        car = pygame.image.load("Imgs/car.png")
        car = pygame.transform.scale(car, (50, 30))
        posx = 0
        posy = 0
        speed = 1
        right = True

        while True:
            screen.fill((0, 105, 155))
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    for place in self.graph.places:
                        if cursor.colliderect(place.rect):
                            right = True
                            posx = place.x
                            posy = place.y
                            self.MinMoney = True
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_graph(screen, country, fontD, fontP)
            if self.MinMoney:
                screen.blit(car, (posx, posy - 15))
                if right:
                    if posx < 1300:
                        posx += speed
                    else:
                        right = False
                else:
                    if posx > 1:
                        posx -= speed
                    else:
                        right = True
            cursor.update()
            button1.update(screen, cursor, MinMoneyLabel)
            pygame.display.update()

    def position(self):
        for place in self.graph.places:
            if place.label is 'A':
                place.x = 200
                place.y = 240
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'B':
                place.x = 800
                place.y = 40
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'C':
                place.x = 800
                place.y = 240
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'D':
                place.x = 1150
                place.y = 140
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'E':
                place.x = 500
                place.y = 390
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'F':
                place.x = 200
                place.y = 540
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'G':
                place.x = 800
                place.y = 540
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'H':
                place.x = 1150
                place.y = 390
            if place.label is 'I':
                place.x = 1150
                place.y = 690
                place.rect.x = place.x
                place.rect.y = place.y
            if place.label is 'J':
                place.x = 500
                place.y = 690
                place.rect.x = place.x
                place.rect.y = place.y

    def draw_graph(self, screen, country, fontD, fontP):
        showedge = []
        posfontD = ()
        for edge in self.graph.edges:
            if edge not in showedge:
                showedge.append(edge)
                pygame.draw.line(screen, (0, 0, 0), (edge.vertexA.x,
                                                     edge.vertexA.y), (edge.vertexB.x, edge.vertexB.y), 10)
                if edge.vertexA.y == edge.vertexB.y:
                    posfontD = (
                        (((edge.vertexA.x + edge.vertexB.x) / 2) - 10, edge.vertexA.y - 20))
                elif edge.vertexA.x == edge.vertexB.x:
                    posfontD = (edge.vertexA.x + 10,
                                (((edge.vertexA.y + edge.vertexB.y) / 2) - 10))
                else:
                    posfontD = ((((edge.vertexA.x + edge.vertexB.x) / 2) - 5),
                                (((edge.vertexA.y + edge.vertexB.y) / 2)) - 20)
                screen.blit(fontD.render(
                    f"{edge.value}", True, (0, 0, 0)), posfontD)
        for place in self.graph.places:
            screen.blit(country, (place.x - 40, place.y - 50))
            place.rect.x = place.x - 40
            place.rect.y = place.y - 50
            screen.blit(fontP.render(
                f"{place.name}", True, (255, 255, 255)), (place.x - 30, place.y + 12))
