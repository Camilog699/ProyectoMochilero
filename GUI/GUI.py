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
        self.show = False
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
        self.JobsToButton = []
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
        fontM = pygame.font.SysFont("Times new Roman", 40)
        fontH = pygame.font.SysFont("Times new Roman", 30)
        fontB = pygame.font.SysFont("Times new Roman", 15)

        # labels to use
        MinMoneyLabel = fontB.render("Min. roads", True, (0, 0, 0))
        Select = fontM.render("Select the arrival city", True, (255, 0, 0))
        Select2 = fontM.render("Select the destiny city", True, (255, 0, 0))
        Obs = fontB.render("Obstruction", True, (0, 0, 0))
        Show = fontB.render("Show info.", True, (0, 0, 0))
        SelecTransport = fontD.render("Select Trasport", True, (0, 0, 0))
        Time = fontD.render("Time: ", True, (0, 0, 0))
        start = fontB.render("Start travel", True, (0, 0, 0))

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
        button3 = ButtonP(image1, image1, 420, 40)
        button4 = ButtonP(image1, image1, 40, 140)

        # main elements
        cursor = Cursor()

        # elements by animation

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
        hour = 0
        minutes = 0
        seconds = 0

        while True:
            screen.fill((0, 105, 155))
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    if cursor.colliderect(button2.rect):
                        self.obs = True
                    elif self.obs:
                        for edge in self.graph.edges:
                            if (edge.line.x < pygame.mouse.get_pos()[0] < edge.line.right and edge.line.y < pygame.mouse.get_pos()[1] < edge.line.bottom):
                                edge.obs = True
                    """if cursor.colliderect(button4.rect):
                        self.transport = True
                    elif self.transport:
                        for place in self.graph.places:
                            if cursor.colliderect(place.rect):
                                pos = (place.x, place.y)
                                init = place
                                self.MinMoney = True
                        self.transport = False"""
                    if cursor.colliderect(button3.rect):
                        self.ini = True
                        screenTK3 = Tk()
                        size = self.screen_size()
                        screenTK3.geometry(
                            f"430x260+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK3.title(
                            "Travel way")
                        Button(screenTK3, text="Way with the minimun cost",
                               command=lambda: self.start(screenTK3, 1)).place(x=20, y=50)
                        Button(screenTK3, text="Way with the minimun time",
                               command=lambda: self.start(screenTK3, 2)).place(x=20, y=100)
                        Button(screenTK3, text="Other",
                               command=lambda: self.start(screenTK3, 3)).place(x=20, y=150)
                        screenTK3.mainloop()
                    if cursor.colliderect(button1.rect):
                        screenTK = Tk()
                        size = self.screen_size()
                        screenTK.geometry(
                            f"430x160+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK.title(
                            "Select way to show")
                        Button(screenTK, text="Way with the minimun cost",
                               command=lambda: self.selway(screenTK, 1)).place(x=20, y=50)
                        Button(screenTK, text="Way with the minimun time",
                               command=lambda: self.selway(screenTK, 2)).place(x=20, y=100)
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
                    if cursor.colliderect(button4.rect):
                        self.show = True
                    elif self.show:
                        for place in self.graph.places:
                            if cursor.colliderect(place.rect):
                                pos = (place.x, place.y)
                                screenTK5 = Tk()
                                screenTK5.geometry(
                                    f"200x280+{pos[0]}+{pos[1]}")
                                screenTK5.title("Info")
                                textC = StringVar(
                                    value="info to Place:")
                                labelC = Label(
                                    screenTK5, textvariable=textC).place(x=5, y=10)
                                text_ = StringVar(
                                    value="_______________________________________")
                                label_ = Label(
                                    screenTK5, textvariable=text_).place(x=-10, y=30)
                                textJobs = StringVar(
                                    value="Jobs:")
                                labelJobs = Label(
                                    screenTK5, textvariable=textJobs).place(x=5, y=50)
                                x = 5
                                y = 40
                                for job in place.jobs:
                                    y += 30
                                    Button(screenTK5, text=job.name, command=lambda: self.getJobs(
                                        screenTK5, job)).place(x=x, y=y)
                                text_ = StringVar(
                                    value="_______________________________________")
                                label_ = Label(
                                    screenTK5, textvariable=text_).place(x=-10, y=130)
                                textThings = StringVar(
                                    value="Things:")
                                labelThings = Label(
                                    screenTK5, textvariable=textThings).place(x=5, y=150)
                                x1 = 5
                                y1 = 140
                                for thing in place.things:
                                    if thing.type == "optional":
                                        y1 += 30
                                        Button(screenTK5, text=thing.name, command=lambda: self.getJobs(
                                            screenTK5, thing)).place(x=x1, y=y1)
                                screenTK5.mainloop()
                        self.show = False
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
                    if self.ini:
                        self.way.clear()
                        for place in self.graph.places:
                            if cursor.colliderect(place.rect):
                                self.way = self.graph.Dijkstra(
                                    self.Nodeinit, False, False, place.label)
                                for node in self.way:
                                    if node.statusD[1] is self.init.label:
                                        self.destiny = node
                                        break

                        self.other = False
                    if self.ini:
                        self.MinMoney = True
                        self.ini = False
                        pos = (self.init.x, self.init.y)
                        screenTK4 = Tk()
                        size = self.screen_size()
                        screenTK4.geometry(
                            f"430x260+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK4.title("Travel form")
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
                                   command=lambda: self.transportF(screenTK4, Tr1)).place(x=20, y=50)
                        if T2:
                            Button(screenTK4, text="Car",
                                   command=lambda: self.transportF(
                                       screenTK4, Tr2)).place(x=20, y=100)
                        if T3:
                            Button(screenTK4, text="Donkey",
                                   command=lambda: self.transportF(
                                       screenTK4, Tr3)).place(x=20, y=150)
                        screenTK4.mainloop()
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_graph(screen, country, carCrash, fontD, fontP)

            if self.MinMoney:
                carSelect = self.orientation(pos, self.init)
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
                screen.blit(Select, (10, 650))
            if self.other:
                screen.blit(Select2, (10, 650))
                self.ini = True
            screen.blit(fontH.render(f"{hour}:{minutes}:{seconds}", True, (0, 0, 0)), (1000, 20))
            if hour == 12 and minutes == 60 and seconds == 60:
                hour = 1
                minutes = 0
                seconds = 0
            elif seconds < 60:
                seconds += 1
            elif seconds == 60:
                seconds = 0
                minutes += 1
            elif minutes == 60:
                minutes = 0
                hour += 1
             
            cursor.update()
            button1.update(screen, cursor, MinMoneyLabel)
            button2.update(screen, cursor, Obs)
            button3.update(screen, cursor, start)
            button4.update(screen, cursor, Show)
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
                edge.line = pygame.draw.line(screen, edge.color, (edge.vertexA.x,
                                                      edge.vertexA.y), (edge.vertexB.x, edge.vertexB.y), 10)
                self.graph.Get_Places(edge.vertexB, edge.vertexA).line = edge.line
                if edge.obs:
                    screen.blit(carCrash, (edge.line.centerx, edge.line.centery))
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

    def orientation(self, pos, init):
        if init not in self.visited:
            self.visited.append(init)
        speed = 2
        i = 0
        pas = False
        carSelect = self.form.Der
        if len(self.visited) is len(self.graph.places):
            self.visited.clear()
        for j in range(len(init.goings)):
            if init.goings[j] not in self.visited:
                i = j
                break
        # To right
        if init.x < init.goings[i].x and init.y == init.goings[i].y:
            if pos[0] < init.goings[i].x:
                carSelect = self.form.Der
        # To Left
        elif init.x > init.goings[i].x and init.y == init.goings[i].y:
            if pos[0] > init.goings[i].x:
                carSelect = self.form.Izq
        # Equal
            # To Up
        elif init.x == init.goings[i].x and init.y > init.goings[i].y:
            if pos[1] > init.goings[i].y:
                carSelect = self.form.Arr
            # To Down
        elif init.x == init.goings[i].x and init.y < init.goings[i].y:
            if pos[1] < init.goings[i].y:
                carSelect = self.form.Aba
        # To Right-Up
        elif init.x < init.goings[i].x and init.y > init.goings[i].y:
            if pos[0] < init.goings[i].x and pos[1] > init.goings[i].y:
                carSelect = self.form.DerUp
        # To Right-Down
        elif init.x < init.goings[i].x and init.y < init.goings[i].y:
            if pos[0] < init.goings[i].x and pos[1] < init.goings[i].y:
                carSelect = self.form.DerDown
        # To Left-Up
        elif init.x > init.goings[i].x and init.y > init.goings[i].y:
            if pos[0] > init.goings[i].x and pos[1] > init.goings[i].y:
                carSelect = self.form.IzqUp
        # To Left-Down
        elif init.x > init.goings[i].x and init.y < init.goings[i].y:
            if pos[0] > init.goings[i].x and pos[1] < init.goings[i].y:
                carSelect = self.form.IzqDown
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
            self.begin = False
            self.ini = False
        screen.destroy()

    def transportF(self, screen, transport):
        self.form = transport
        screen.destroy()

    def getJobs(self, screen, t):
        self.JobsToButton.append(t)
