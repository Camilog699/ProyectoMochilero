import pygame
import subprocess
import os
import sys
import ctypes
from tkinter import*
from Json.JSON import JSON
from random import randint
from Views.cursor import Cursor
from Views.button import ButtonP
pygame.init()


class GUI:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.cursor = Cursor()
        self.mincost = False
        self.mintime = False
        self.cost = None
        self.time = None
        self.MinMoney = False
        self.ways = False
        self.obs = False
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
        fontM = pygame.font.SysFont("Times new Roman", 50)

        # labels to use
        MinMoneyLabel = fontD.render("Minimun roads", True, (0, 0, 0))
        Select = fontM.render("Select the arrival city", True, (255, 0, 0))
        Obs = fontD.render("Obstruction", True, (0, 0, 0))

        # images
        country = pygame.image.load("Imgs/city.png")
        country = pygame.transform.scale(country, (85, 60))
        image1 = pygame.image.load("Imgs/boton1.png")
        image1 = pygame.transform.scale(image1, (130, 60))
        carCrash = pygame.image.load("Imgs/carCrash.png")
        carCrash = pygame.transform.scale(carCrash, (100, 40))

        # Buttons
        button1 = ButtonP(image1, image1, 40, 40)
        button2 = ButtonP(image1, image1, 220, 40)

        # main elements
        cursor = Cursor()

        # elements by animation
        carDer = pygame.image.load("Imgs/carDer.png")
        carDer = pygame.transform.scale(carDer, (50, 30))
        carIzq = pygame.image.load("Imgs/carIzq.png")
        carIzq = pygame.transform.scale(carIzq, (50, 30))
        carArr = pygame.image.load("Imgs/carArr.png")
        carArr = pygame.transform.scale(carArr, (30, 50))
        carAba = pygame.image.load("Imgs/carAba.png")
        carAba = pygame.transform.scale(carAba, (30, 50))
        pos = (0, 0)
        speed = 2
        right = True
        up = True
        MinCost = []
        MinTime = []
        arrival = None
        init = None

        while True:
            screen.fill((0, 105, 155))
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    """for place in self.graph.places:
                        if cursor.colliderect(place.rect):
                            pos = (place.x, place.y)
                            init = place
                            self.MinMoney = True"""
                    if cursor.colliderect(button1.rect):
                        screenTK = Tk()
                        size = self.screen_size()
                        screenTK.geometry(
                            f"430x110+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK.title(
                            "Select way to show")
                        Button(screenTK, text="Way with the minimun cost",
                               command=lambda: self.selway(screenTK, 1)).place(x=20, y=50)
                        Button(screenTK, text="Way with the minimun time",
                               command=lambda: self.selway(screenTK, 2)).place(x=100, y=50)
                        screenTK.mainloop()
                    elif self.mintime:
                        self.ways = True
                        screenTK1 = Tk()
                        size = self.screen_size()
                        screenTK1.geometry(
                            f"430x110+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK1.title(
                            "Way whit the minimun time")
                        self.time = IntVar()
                        textT = StringVar(
                            value="Write the trip time.")
                        labelT = Label(
                            screenTK1, textvariable=textT).place(x=200, y=10)
                        Time_field = Entry(
                            screenTK1, textvariable=self.time, width=25).place(x=210, y=30)
                        Button(screenTK1, text="OK",
                               command=lambda: self.selway(screenTK1, 2)).place(x=170, y=70)
                        screenTK1.mainloop()
                    elif self.mincost:
                        self.ways = True
                        screenTK2 = Tk()
                        size = self.screen_size()
                        screenTK2.geometry(
                            f"430x110+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK2.title(
                            "Way whit the minimun cost")
                        self.cost = IntVar()
                        textC = StringVar(
                            value="Writhe the backpacker budget.")
                        labelC = Label(
                            screenTK2, textvariable=textC).place(x=5, y=10)
                        Cost_field = Entry(
                            screenTK2, textvariable=self.cost, width=25).place(x=10, y=30)
                        Button(screenTK2, text="OK",
                               command=lambda: screenTK2.destroy()).place(x=170, y=70)
                        screenTK2.mainloop()
                    if self.ways:
                        for place in self.graph.places:
                            if cursor.colliderect(place.rect):
                                if self.mincost:
                                    MinCost = self.graph.Dijkstra(
                                        place, True, False, int(self.cost.get()))
                                if self.mintime:
                                    MinTime = self.graph.Dijkstra(
                                        place, False, True, int(self.time.get()))
                        if self.mincost:
                            for edge in self.graph.edges:
                                for node in MinCost:
                                    if edge.vertexA is self.graph.Get_Vertex(node.status[1]) and edge.vertexB is node:
                                        edge.color = (0, 255, 0)
                                    elif edge.vertexA is node and edge.vertexB is self.graph.Get_Vertex(node.status[1]):
                                        edge.color = (0, 255, 0)
                            self.mincost = False
                        if self.mintime:
                            for edge in self.graph.edges:
                                for node in MinTime:
                                    if edge.vertexA is self.graph.Get_Vertex(node.statusT[1]) and edge.vertexB is node:
                                        edge.color = (0, 0, 255)
                                    elif edge.vertexA is node and edge.vertexB is self.graph.Get_Vertex(node.status[1]):
                                        edge.color = (0, 0, 255)
                            self.mintime = False
                        self.ways = False
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_graph(screen, country, carCrash, fontD, fontP)

            if self.MinMoney:
                carSelect = self.orientation(
                    pos, init, carDer, carIzq, carArr, carAba)
                screen.blit(carSelect, pos)
                for place in self.graph.places:
                    if place.x == pos[0] and place.y == pos[1]:
                        init = place
                pos = self.transportMove(init, pos)
            if self.mincost or self.mintime:
                screen.blit(Select, (self.screen_size()[
                    0]/2, 10))

            cursor.update()
            button1.update(screen, cursor, MinMoneyLabel)
            button2.update(screen, cursor, Obs)
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

    def draw_graph(self, screen, country, carCrash, fontD, fontP):
        showedge = []
        posfontD = ()
        for edge in self.graph.edges:

            if edge not in showedge:
                showedge.append(edge)
                showedge.append(self.graph.Get_Places(
                    edge.vertexB, edge.vertexA))
                pygame.draw.line(screen, edge.color, (edge.vertexA.x,
                                                      edge.vertexA.y), (edge.vertexB.x, edge.vertexB.y), 10)
                if edge.vertexA.y == edge.vertexB.y:
                    posfontD = (
                        (((edge.vertexA.x + edge.vertexB.x) / 2) - 10, edge.vertexA.y - 20))
                elif edge.vertexA.x == edge.vertexB.x:
                    posfontD = (edge.vertexA.x+10,
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

    # Modificar

    def transportMove(self, init, pos):
        X1 = pos[0]
        Y1 = pos[1]
        if init not in self.visited:
            self.visited.append(init)
        speed = 1
        i = 0
        pas = False
        if len(self.visited) is len(self.graph.places):
            self.visited.clear()
        for j in range(len(init.goings)):
            if init.goings[j] not in self.visited:
                i = j
                break
        X2 = init.goings[i].x
        Y2 = init.goings[i].y
        #Y = (Y2-Y1)*((X-X1)/(X2-X1))

        # To right
        if init.x < init.goings[i].x and init.y == init.goings[i].y:
            if pos[0] < init.goings[i].x:
                pos = (pos[0] + speed, pos[1])
        # To Left
        elif init.x > init.goings[i].x and init.y == init.goings[i].y:
            if pos[0] > init.goings[i].x:
                pos = (pos[0] - speed, pos[1])
        # Equal
            # To Up
        elif init.x == init.goings[i].x and init.y > init.goings[i].y:
            if pos[1] > init.goings[i].y:
                pos = (pos[0], pos[1] - speed)
            # To Down
        elif init.x == init.goings[i].x and init.y < init.goings[i].y:
            if pos[1] < init.goings[i].y:
                pos = (pos[0], pos[1] + speed)
        # To Right-Up
        elif init.x < init.goings[i].x and init.y > init.goings[i].y:
            if pos[0] < init.goings[i].x and pos[1] > init.goings[i].y:
                pos = (pos[0] + speed,
                       ((Y2-Y1)*(((pos[0] + speed)-X1)/(X2-X1))) + Y1)
        # To Right-Down
        elif init.x < init.goings[i].x and init.y < init.goings[i].y:
            if pos[0] < init.goings[i].x and pos[1] < init.goings[i].y:
                pos = (pos[0] + speed,
                       ((Y2-Y1)*(((pos[0] + speed)-X1)/(X2-X1))) + Y1)
        # To Left-Up
        elif init.x > init.goings[i].x and init.y > init.goings[i].y:
            if pos[0] > init.goings[i].x and pos[1] > init.goings[i].y:
                pos = (pos[0] - speed,
                       ((Y2-Y1)*(((pos[0] - speed)-X1)/(X2-X1))) + Y1)
        # To Left-Down
        elif init.x > init.goings[i].x and init.y < init.goings[i].y:
            if pos[0] > init.goings[i].x and pos[1] < init.goings[i].y:
                pos = (pos[0] - speed,
                       ((Y2-Y1)*(((pos[0] - speed)-X1)/(X2-X1))) + Y1)
        return pos

    def orientation(self, pos, init, carDer, carIzq, carArr, carAba):
        if init not in self.visited:
            self.visited.append(init)
        speed = 2
        i = 0
        pas = False
        carSelect = carDer
        if len(self.visited) is len(self.graph.places):
            self.visited.clear()
        for j in range(len(init.goings)):
            if init.goings[j] not in self.visited:
                i = j
                break
        if pos[0] < init.goings[i].x:
            carSelect = carDer
        if pos[0] > init.goings[i].x:
            carSelect = carIzq
        if pos[0] == init.goings[i].x:
            if pos[1] > init.goings[i].y:
                carSelect = carArr
            if pos[1] < init.goings[i].y:
                pos = (pos[0], pos[1] + speed)
        return pos

    def selway(self, screenTK, id):
        if id == 1:
            self.mincost = True
        else:
            self.mintime = True
        screenTK.destroy()
