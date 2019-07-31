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
from Resources.backpacker import Backpacker
pygame.init()


class GUI:
    def __init__(self, graph):
        self.graph = graph
        self.backpacker = None
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
        self.continueB = False
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
        self.walk = False
        self.minimunC = False
        self.minimunT = False
        self.mostrar = False
        self.minimunO = False
        self.destinyin = None
        self.JobsToButton = []
        self.Jobs2ToButton = []
        self.acti1 = ""
        self.job2 = ""
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
        Finish = fontB.render("Resume", True, (0, 0, 0))
        SelecTransport = fontD.render("Select Trasport", True, (0, 0, 0))
        Time = fontD.render("Time: ", True, (0, 0, 0))
        start = fontB.render("Start travel", True, (0, 0, 0))
        continueB = fontB.render("Cont. travel", True, (0, 0, 0))
        obstru = fontB.render(
            "Current route obstructed, recalculating...", True, (255, 0, 0))

        # images
        country = pygame.image.load("Imgs/city.png")
        country = pygame.transform.scale(country, (85, 60))
        image1 = pygame.image.load("Imgs/boton1.png")
        image1 = pygame.transform.scale(image1, (130, 60))
        image2 = pygame.image.load("Imgs/boton2.png")
        image2 = pygame.transform.scale(image2, (130, 60))
        carCrash = pygame.image.load("Imgs/carCrash.png")
        carCrash = pygame.transform.scale(carCrash, (100, 40))
        person = pygame.image.load("Imgs/person.png")
        person = pygame.transform.scale(person, (40, 40))
        bolsita = pygame.image.load("Imgs/money.png")
        bolsita = pygame.transform.scale(bolsita, (40, 40))

        # Buttons
        button1 = ButtonP(image1, image2, 40, 40)
        button2 = ButtonP(image1, image2, 200, 40)
        button3 = ButtonP(image1, image2, 360, 40)
        button4 = ButtonP(image1, image2, 40, 100)
        button5 = ButtonP(image1, image2, 200, 100)
        button6 = ButtonP(image1, image2, 360, 100)

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
        days = 0
        hour = 0
        minutes = 0
        seconds = 0
        cont = 0
        daysR = 0
        hourR = 0
        minutesR = 0
        secondsR = 0
        contR = 0

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
                    if cursor.colliderect(button3.rect):
                        self.ini = True
                        screenTK3 = Tk()
                        size = self.screen_size()
                        screenTK3.geometry(
                            f"430x260+{int(size[0]/2) - 230}+{int(size[1]/2) - 100}")
                        screenTK3.title(
                            "Start travel")
                        self.time = IntVar()
                        self.cost = IntVar()
                        textC = StringVar(
                            value="Write the backpacker budget.")
                        labelC = Label(
                            screenTK3, textvariable=textC).place(x=25, y=10)
                        Cost_field = Entry(
                            screenTK3, textvariable=self.cost, width=25).place(x=25, y=30)
                        textT = StringVar(
                            value="Write the trip time.")
                        labelT = Label(
                            screenTK3, textvariable=textT).place(x=220, y=10)
                        Time_field = Entry(
                            screenTK3, textvariable=self.time, width=25).place(x=220, y=30)
                        Button(screenTK3, text="Way with the minimun cost",
                               command=lambda: self.start(screenTK3, 1)).place(x=25, y=80)
                        Button(screenTK3, text="Way with the minimun time",
                               command=lambda: self.start(screenTK3, 2)).place(x=220, y=80)
                        Button(screenTK3, text="Other",
                               command=lambda: self.start(screenTK3, 3)).place(x=180, y=150)
                        screenTK3.mainloop()
                        self.backpacker = Backpacker(
                            self.cost.get(), self.time.get())
                        self.mostrar = True
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
                    if cursor.colliderect(button4.rect):
                        self.show = True
                    elif self.show:
                        for place in self.graph.places:
                            if cursor.colliderect(place.rect):
                                pos = (place.x, place.y)
                                screenTK5 = Tk()
                                screenTK5.geometry(
                                    f"280x410+{pos[0]}+{pos[1]}")
                                screenTK5.title("Info")
                                self.acti1 = StringVar()
                                self.job1 = StringVar()
                                textC = StringVar(
                                    value="info to Place:")
                                labelC = Label(
                                    screenTK5, textvariable=textC).place(x=5, y=10)
                                text_ = StringVar(
                                    value="__________________________________________________")
                                label_ = Label(
                                    screenTK5, textvariable=text_).place(x=-10, y=30)
                                if self.backpacker.getWork():
                                    texttimeT = StringVar(
                                        value="Time:")
                                    labeltimeT = Label(
                                        screenTK5, textvariable=texttimeT).place(x=5, y=50)
                                    textGainT = StringVar(
                                        value="Gain:")
                                    labelGainT = Label(
                                        screenTK5, textvariable=textGainT).place(x=40, y=50)
                                    textJobs = StringVar(
                                        value="Jobs:")
                                    labelJobs = Label(
                                        screenTK5, textvariable=textJobs).place(x=80, y=50)
                                    text_ = StringVar(
                                        value="__________________________________________________")
                                    label_ = Label(
                                        screenTK5, textvariable=text_).place(x=-10, y=65)
                                    x = 5
                                    y = 50
                                    for job in place.jobs:
                                        y += 30
                                        textJobsTime = StringVar(
                                            value=job.time)
                                        labelJobsTime = Label(
                                            screenTK5, textvariable=textJobsTime).place(x=15, y=y)
                                        textJobsGain = StringVar(
                                            value=job.gain)
                                        labelJobsgain = Label(
                                            screenTK5, textvariable=textJobsGain).place(x=55, y=y)
                                        # Elementos para realizar nuevos "botones"
                                        textJob = StringVar(
                                            value=job.name)
                                        labelJob = Label(
                                            screenTK5, textvariable=textJob).place(x=95, y=y)
                                        # Lista final que agrega los trabajos de cada place
                                        place.jobsFinish.append(job)
                                text_ = StringVar(
                                    value="__________________________________________________")
                                label_ = Label(
                                    screenTK5, textvariable=text_).place(x=-10, y=130)
                                texttimeT = StringVar(
                                    value="Time:")
                                labeltimeT = Label(
                                    screenTK5, textvariable=texttimeT).place(x=5, y=150)
                                textcostT = StringVar(
                                    value="Cost:")
                                labelcostT = Label(
                                    screenTK5, textvariable=textcostT).place(x=40, y=150)
                                textThings = StringVar(
                                    value="Things:")
                                labelThings = Label(
                                    screenTK5, textvariable=textThings).place(x=80, y=150)
                                text_ = StringVar(
                                    value="__________________________________________________")
                                label_ = Label(
                                    screenTK5, textvariable=text_).place(x=-10, y=165)
                                x1 = 90
                                y1 = 155
                                # Evaluar
                                for thing in place.things:
                                    if thing.type == "optional":
                                        y1 += 30
                                        textThingsTime = StringVar(
                                            value=thing.time)
                                        labelThingsTime = Label(
                                            screenTK5, textvariable=textThingsTime).place(x=15, y=y1)
                                        textThingsCost = StringVar(
                                            value=thing.cost)
                                        labelThingsCost = Label(
                                            screenTK5, textvariable=textThingsCost).place(x=55, y=y1)
                                        # Elementos para realizar nuevos "botones"
                                        textActivity = StringVar(
                                            value=thing.name)
                                        labelActivity = Label(
                                            screenTK5, textvariable=textActivity).place(x=95, y=y1)
                                        # Nueva Lista que agrega cada Actividad del place
                                        place.activityFinish.append(thing)
                                        # Evaluar
                                        # Button(screenTK5, text=thing.name, command=lambda: self.getJobs(
                                        # screenTK5, place, id)).place(x=x1, y=y1)
                                # Inputs necesarios
                                text = StringVar(
                                    value="Write the activity that you go to do.")
                                labelActivity = Label(
                                    screenTK5, textvariable=text).place(x=10, y=255)
                                Text1 = Entry(screenTK5,
                                              textvariable=self.acti1, width=40).place(x=10, y=270)
                                Button(screenTK5, text="OK",
                                       command=lambda: self.getJobs(screenTK5, place, self.acti1.get())).place(x=115, y=300)
                                if self.backpacker.getWork():
                                    text_ = StringVar(
                                        value="__________________________________________________")
                                    label_ = Label(
                                        screenTK5, textvariable=text_).place(x=-10, y=325)
                                    text2 = StringVar(
                                        value="If your budget is smaller than 40% write some job")
                                    labelActivity = Label(
                                        screenTK5, textvariable=text2).place(x=10, y=340)
                                    Text2 = Entry(screenTK5,
                                                  textvariable=self.job1, width=30).place(x=10, y=355)
                                    Button(screenTK5, text="OK",
                                           command=lambda: self.getJobs2(screenTK5, place, self.job1.get())).place(x=115, y=385)
                                self.acti1.set('')
                                self.job1.set('')
                                screenTK5.mainloop()
                        self.show = False
                    if cursor.colliderect(button5.rect):
                        self.ini = True
                    # Aqui voy_______________________________________________________
                    if cursor.colliderect(button6.rect):
                        pass
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
                            self.destinyin = self.way[0]
                            self.minimunC = True
                            for node in self.way:
                                if node.status[1] is self.init.label:
                                    self.destiny = node
                                    break
                        if self.mintime:
                            self.MinTime = self.graph.Dijkstra(
                                self.Nodeinit, False, True, int(self.time.get()))
                            self.way = self.MinTime
                            self.destinyin = self.way[0]
                            self.minimunT = True
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
                        if self.other:
                            self.way.clear()
                            self.minimunO = True
                            for place in self.graph.places:
                                if cursor.colliderect(place.rect):
                                    self.way = self.graph.Dijkstra(
                                        self.Nodeinit, False, False, place.label)
                                    self.destinyin = self.way[0]
                                    for node in self.way:
                                        if node.statusD[1] is self.init.label:
                                            self.destiny = node
                                            break
                            self.other = False
                        self.ways = False
                        self.ini = True
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
                                   command=lambda: self.transportF(screenTK4, Tr1, self.graph.Get_Places(self.init, self.destiny))).place(x=20, y=50)
                        if T2:
                            Button(screenTK4, text="Car",
                                   command=lambda: self.transportF(
                                       screenTK4, Tr2, self.graph.Get_Places(self.init, self.destiny))).place(x=20, y=100)
                        if T3:
                            Button(screenTK4, text="Donkey",
                                   command=lambda: self.transportF(
                                       screenTK4, Tr3, self.graph.Get_Places(self.init, self.destiny))).place(x=20, y=150)
                        screenTK4.mainloop()
                        T1 = False
                        T2 = False
                        T3 = False
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw_graph(screen, country, carCrash, fontD, fontP)
            if self.MinMoney:
                self.walk = False
                status = ''
                carSelect = self.orientation(pos, self.init, self.destiny)
                screen.blit(carSelect, pos)
                for place in self.graph.places:
                    if place.x == pos[0] and place.y == pos[1]:
                        self.init = place
                        break
                if self.init == self.destiny:
                    for node in self.way:
                        if self.minimunC:
                            status = node.status[1]
                        elif self.minimunT:
                            status = node.statusT[1]
                        elif self.minimunO:
                            status = node.statusD[1]
                        if status is self.init.label:
                            self.destiny = node
                            break
                    self.MinMoney = False
                if self.MinMoney:
                    pos = self.transportMove(self.init, self.destiny, pos)
                else:
                    self.walk = True
            if self.walk:
                screen.blit(person, (self.init.x, self.init.y))
            if self.begin:
                screen.blit(Select, (10, 650))
            if self.other:
                screen.blit(Select2, (10, 650))
                self.ways = True
            screen.blit(fontP.render("Current Time:",
                                     True, (0, 0, 0)), (1000, 10))
            screen.blit(fontP.render(
                f"{days} days {hour}:{minutes}:{seconds}", True, (0, 0, 0)), (1000, 30))
            if hour == 12 and minutes == 60:
                minutes = 0
                seconds = 0
                hour = 1
            if hour == 11 and minutes == 60:
                hour += 1
                minutes = 0
                seconds = 0
                cont += 1
            elif hour < 13 and minutes == 60:
                hour += 1
                minutes = 0
                seconds = 0
            elif hour < 13 and minutes < 60 and seconds == 60:
                minutes += 1
                seconds = 0
            elif hour < 13 and minutes < 60 and seconds < 60:
                seconds += 1
            if cont == 2:
                days += 1
                cont = 0
            screen.blit(fontP.render("Remaining Time:",
                                     True, (0, 0, 0)), (1170, 10))
            screen.blit(fontP.render(
                f"{daysR} days  {hourR}:{minutesR}:{secondsR}", True, (0, 0, 0)), (1170, 30))
            if self.mostrar:
                screen.blit(bolsita, (1130, 55))
                screen.blit(fontP.render(
                    f"Money: {self.backpacker.money}", True, (0, 0, 0)), (1170, 60))
            cursor.update()
            button1.update(screen, cursor, MinMoneyLabel)
            button2.update(screen, cursor, Obs)
            button3.update(screen, cursor, start)
            button4.update(screen, cursor, Show)
            button5.update(screen, cursor, continueB)
            button6.update(screen, cursor, Finish)
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
                self.graph.Get_Places(
                    edge.vertexB, edge.vertexA).line = edge.line
                if edge.obs:
                    screen.blit(
                        carCrash, (edge.line.centerx, edge.line.centery))
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
        speed = 1
        i = 0
        pas = False
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

    def orientation(self, pos, init, destiny):
        speed = 2
        i = 0
        pas = False
        carSelect = self.form.Der
        # To right
        if init.x < destiny.x and init.y == destiny.y:
            if pos[0] < destiny.x:
                carSelect = self.form.Der
        # To Left
        elif init.x > destiny.x and init.y == destiny.y:
            if pos[0] > destiny.x:
                carSelect = self.form.Izq
        # Equal
            # To Up
        elif init.x == destiny.x and init.y > destiny.y:
            if pos[1] > destiny.y:
                carSelect = self.form.Arr
            # To Down
        elif init.x == destiny.x and init.y < destiny.y:
            if pos[1] < destiny.y:
                carSelect = self.form.Aba
        # To Right-Up
        elif init.x < destiny.x and init.y > destiny.y:
            if pos[0] < destiny.x and pos[1] > destiny.y:
                carSelect = self.form.DerUp
        # To Right-Down
        elif init.x < destiny.x and init.y < destiny.y:
            if pos[0] < destiny.x and pos[1] < destiny.y:
                carSelect = self.form.DerDown
        # To Left-Up
        elif init.x > destiny.x and init.y > destiny.y:
            if pos[0] > destiny.x and pos[1] > destiny.y:
                carSelect = self.form.IzqUp
        # To Left-Down
        elif init.x > destiny.x and init.y < destiny.y:
            if pos[0] > destiny.x and pos[1] < destiny.y:
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
            self.ways = True
        elif id == 2:
            self.mintime = True
            self.ways = True
        else:
            self.other = True
            self.ini = False
        screen.destroy()

    def transportF(self, screen, transport, way):
        self.form = transport
        self.backpacker.money -= (self.form.valueByKm * way.value)
        screen.destroy()

    def getJobs(self, screen, place, thingname):
        for thing in place.things:
            if thing.name == thingname:
                self.JobsToButton.append(thing)
                self.backpacker.money -= thing.cost

    def getJobs2(self, screen, place, jobname):
        for job in place.jobs:
            if job.name == jobname:
                self.JobsToButton.append(job)
                self.backpacker.money += job.gain
