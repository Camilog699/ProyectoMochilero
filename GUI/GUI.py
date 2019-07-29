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
        self.ini = False
        self.MinCost = []
        self.MinTime = []
        self.other = False
        self.begin = True
        self.Nodeinit = None
        self.form = None
        self.destiny = None
        self.init = None
        self.way = []
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
        Select2 = fontM.render("Select the destiny city", True, (255, 0, 0))
        Obs = fontD.render("Obstruction", True, (0, 0, 0))
        start = fontD.render("Start travel", True, (0, 0, 0))

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
        button3 = ButtonP(image1, image1, 440, 40)

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
        arrival = None
        T1 = False
        T2 = False
        T3 = False
        Tr1 = None
        Tr2 = None
        Tr3 = None

        while True:
            screen.fill((0, 105, 155))
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    if cursor.colliderect(button3.rect):
                        self.ini = True
                        screenTK3 = Tk()
                        size = self.screen_size()
                        screenTK3.geometry(
                            f"430x110+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK3.title(
                            "Travel way")
                        Button(screenTK3, text="Way with the minimun cost",
                               command=lambda: self.start(screenTK3, 1)).place(x=20, y=50)
                        Button(screenTK3, text="Way with the minimun time",
                               command=lambda: self.start(screenTK3, 2)).place(x=100, y=50)
                        Button(screenTK3, text="Other",
                               command=lambda: self.start(screenTK3, 3)).place(x=200, y=50)
                        screenTK3.mainloop()
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
                    if self.mintime:
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
                    if self.mincost:
                        self.ways = True
                        screenTK2 = Tk()
                        size = self.screen_size()
                        screenTK2.geometry(
                            f"430x110+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK2.title(
                            "Way whit the minimun cost")
                        self.cost = IntVar()
                        textC = StringVar(
                            value="Write the backpacker budget.")
                        labelC = Label(
                            screenTK2, textvariable=textC).place(x=5, y=10)
                        Cost_field = Entry(
                            screenTK2, textvariable=self.cost, width=25).place(x=10, y=30)
                        Button(screenTK2, text="OK",
                               command=lambda: screenTK2.destroy()).place(x=170, y=70)
                        screenTK2.mainloop()
                    if self.begin:
                        for place in self.graph.places:
                            if cursor.colliderect(place.rect):
                                self.Nodeinit = place
                                self.init = place
                        self.begin = False
                    if self.ways:
                        self.way.clear()
                        if self.mincost:
                            self.MinCost = self.graph.Dijkstra(
                                self.Nodeinit, True, False, int(self.cost.get()))
                            self.way = self.MinCost
                            for node in self.way:
                                if node.status[1] is self.init.label:
                                    self.destiny = node
                                    break
                        if self.mintime:
                            self.MinTime = self.graph.Dijkstra(
                                self.Nodeinit, False, True, int(self.time.get()))
                            self.way = self.MinTime
                            for node in self.way:
                                    if node.statusT[1] is self.init.label:
                                        self.destiny = node
                                        break
                        if self.mincost:
                            for edge in self.graph.edges:
                                for node in self.MinCost:
                                    if edge.vertexA is self.graph.Get_Vertex(node.status[1]) and edge.vertexB is node:
                                        edge.color = (0, 255, 0)
                                    if edge.vertexA is node and edge.vertexB is self.graph.Get_Vertex(node.status[1]):
                                        edge.color = (0, 255, 0)
                            self.mincost = False
                        if self.mintime:
                            for edge in self.graph.edges:
                                for node in self.MinTime:
                                    if edge.vertexA is self.graph.Get_Vertex(node.statusT[1]) and edge.vertexB is node:
                                        edge.color = (0, 0, 255)
                                    if edge.vertexA is node and edge.vertexB is self.graph.Get_Vertex(node.statusT[1]):
                                        edge.color = (0, 0, 255)
                            self.mintime = False
                        self.ways = False
                    if self.other:
                        self.way.clear()
                        for place in self.graph.places:
                            if cursor.colliderect(place.rect):
                                self.way = self.graph.Dijkstra(
                                    self.Nodeinit, False, False, 0)
                                for node in self.way:
                                    if node.status[1] is self.init.label:
                                        self.destiny = node
                                        break
                        self.other = False
                        
                    if self.ini:
                        self.MinMoney = True
                        pos = (self.init.x, self.init.y)
                        screenTK4 = Tk()
                        size = self.screen_size()
                        screenTK4.geometry(
                            f"430x110+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK4.title(
                            "Travel form")
                        edge = self.graph.Get_Places(self.init, self.destiny)
                        for transport in edge.forms:
                            if transport.id == 1:
                                T1 = True
                                Tr1 = transport
                            if transport.id == 2:
                                T2 = True
                                Tr2 = transport
                            if transport.id == 3:
                                T3 = True
                                Tr3 = transport
                        if T1:
                            Button(screenTK4, text="Airplane",
                                   command=lambda: self.transport(screenTK4, Tr1)).place(x=20, y=50)
                        if T2:
                            Button(screenTK4, text="Car",
                                   command=lambda: self.transport(screenTK4, Tr2)).place(x=100, y=50)
                        if T3:
                            Button(screenTK4, text="Donkey",
                                   command=lambda: self.transport(screenTK4, Tr3)).place(x=200, y=50)
                        screenTK4.mainloop()
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_graph(screen, country, carCrash, fontD, fontP)

            if self.MinMoney:
                carSelect = self.orientation(
                    pos, self.init, self.destiny, carDer, carIzq, carArr, carAba)
                screen.blit(carSelect, pos)
                for place in self.graph.places:
                    if place.x == pos[0] and place.y == pos[1]:
                        self.init = place
                if self.init == self.destiny:
                    for node in self.way:
                        if node.status[1] is self.init.label:
                            self.destiny = node
                            break
                    self.MinMoney = False
                if self.MinMoney:
                    pos = self.transportMove(self.init, self.destiny, pos)
            if self.begin:
                screen.blit(Select, (self.screen_size()[
                    0]/2, 10))
            if self.other:
                screen.blit(Select2, (self.screen_size()[
                    0]/2, 10))
            cursor.update()
            button1.update(screen, cursor, MinMoneyLabel)
            button2.update(screen, cursor, Obs)
            button3.update(screen, cursor, start)
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

    def transportMove(self, init, destiny, pos):
        X1 = pos[0]
        Y1 = pos[1]
        # if init not in self.visited:
          #  self.visited.append(init)
        speed = 1
        i = 0
        pas = False
        # if len(self.visited) is len(self.graph.places):
          #  self.visited.clear()
        # for j in range(len(init.goings)):
          #  if init.goings[j] not in self.visited:
           #     i = j
            #    break
        # X2 = destiny.x
        # Y2 = destiny.y
        # Y = (Y2-Y1)*((X-X1)/(X2-X1))
        X2 = destiny.x
        Y2 = destiny.y
        # To right
        if init.x < destiny.x and init.y == destiny.y:
            if pos[0] < destiny.x:
                pos = (pos[0] + speed, pos[1])
        # To Left
        elif init.x > destiny.x and init.y == destiny.y:
            if pos[0] > destiny.x:
                pos = (pos[0] - speed, pos[1])
        # Equal
            # To Up
        elif init.x == destiny.x and init.y > destiny.y:
            if pos[1] > destiny.y:
                pos = (pos[0], pos[1] - speed)
            # To Down
        elif init.x == destiny.x and init.y < destiny.y:
            if pos[1] < destiny.y:
                pos = (pos[0], pos[1] + speed)
        # To Right-Up
        elif init.x < destiny.x and init.y > destiny.y:
            if pos[0] < destiny.x and pos[1] > destiny.y:
                pos = (pos[0] + speed,
                       ((Y2-Y1)*(((pos[0] + speed)-X1)/(X2-X1))) + Y1)
        # To Right-Down
        elif init.x < destiny.x and init.y < destiny.y:
            if pos[0] < destiny.x and pos[1] < destiny.y:
                pos = (pos[0] + speed,
                       ((Y2-Y1)*(((pos[0] + speed)-X1)/(X2-X1))) + Y1)
        # To Left-Up
        elif init.x > destiny.x and init.y > destiny.y:
            if pos[0] > destiny.x and pos[1] > destiny.y:
                pos = (pos[0] - speed,
                       ((Y2-Y1)*(((pos[0] - speed)-X1)/(X2-X1))) + Y1)
        # To Left-Down
        elif init.x > destiny.x and init.y < destiny.y:
            if pos[0] > destiny.x and pos[1] < destiny.y:
                pos = (pos[0] - speed,
                       ((Y2-Y1)*(((pos[0] - speed)-X1)/(X2-X1))) + Y1)
        return pos

    def orientation(self, pos, init, destiny, carDer, carIzq, carArr, carAba):
        #if init not in self.visited:
         #   self.visited.append(init)
        speed = 2
        i = 0
        pas = False
        carSelect = carDer
        # if len(self.visited) is len(self.graph.places):
          #  self.visited.clear()
        #for j in range(len(init.goings)):
         #   if init.goings[j] not in self.visited:
          #      i = j
           #     break
        if pos[0] < destiny.x:
            carSelect = carDer
        if pos[0] > destiny.x:
            carSelect = carIzq
        if pos[0] == destiny.x:
            if pos[1] > destiny.y:
                carSelect = carArr
            if pos[1] < destiny.y:
                carSelect = carAba
        return carSelect

    def selway(self, screenTK, id):
        if id == 1:
            self.mincost = True
        else:
            self.mintime = True
        screenTK.destroy()

    def start(self, screen, id):
        if id == 1:
            self.mincost = True
        elif id == 2:
            self.mintime = True
        else:
            self.other = True
        screen.destroy()
    
    def transport(self, screen, transport):
        self.form = transport
        screen.destroy()
