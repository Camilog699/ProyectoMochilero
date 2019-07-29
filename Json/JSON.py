from Resources.graph import Graph
from Resources.transport import Transport
from Resources.jobs import Jobs
from Resources.things import Things
from Resources.places import Place
import pygame
import json
import os


class JSON:
    def __init__(self):
        self.file = ""
        self.graph = Graph()
        self.transports = []
        self.places = []

    def Read(self):
        if os.name is "posix":
            file = "Json/format.json"
            self.slash = "/"
        else:
            file = "Json\\format.json"
            self.slash = "\\"
        with open(file) as jfile:
            data = json.load(jfile)

        Arr = None
        Aba = None
        Der = None
        Izq = None
        DerDown = None
        DerUp = None
        IzqDown = None
        IzqUp = None

        for trans in data["transportForm"]:
            id = trans["id"]
            name = trans["id"]
            valueByKm = trans["valueByKm"]
            timeByKm = trans["timeByKm"]
            if id == 1:
                Arr = pygame.image.load("Imgs/airUp.png")
                Arr = pygame.transform.scale(Arr, (30, 50))
                Aba = pygame.transform.rotate(Arr, 180)
                Der = pygame.transform.rotate(Arr, -90)
                Izq = pygame.transform.rotate(Arr, 90)
                DerDown = pygame.transform.rotate(Der, -40)
                DerUp = pygame.transform.rotate(Der, 40)
                IzqDown = pygame.transform.rotate(Izq, 45)
                IzqUp = pygame.transform.rotate(Izq, -45)
            if id == 2:
                Der = pygame.image.load("Imgs/carDer.png")
                Der = pygame.transform.scale(Der, (50, 30))
                Izq = pygame.image.load("Imgs/carIzq.png")
                Izq = pygame.transform.scale(Izq, (50, 30))
                Arr = pygame.image.load("Imgs/carArr.png")
                Arr = pygame.transform.scale(Arr, (30, 50))
                Aba = pygame.image.load("Imgs/carAba.png")
                Aba = pygame.transform.scale(Aba, (30, 50))
                DerDown = pygame.transform.rotate(Der, -40)
                DerUp = pygame.transform.rotate(Der, 40)
                IzqDown = pygame.transform.rotate(Izq, 45)
                IzqUp = pygame.transform.rotate(Izq, -45)
            if id == 3:
                Arr = pygame.image.load("Imgs/donkeyUp.png")
                Arr = pygame.transform.scale(Arr, (30, 50))
                Aba = pygame.transform.rotate(Arr, 180)
                Der = pygame.transform.rotate(Arr, -90)
                Izq = pygame.transform.rotate(Arr, 90)
                DerDown = pygame.transform.rotate(Der, -40)
                DerUp = pygame.transform.rotate(Der, 40)
                IzqDown = pygame.transform.rotate(Izq, 45)
                IzqUp = pygame.transform.rotate(Izq, -45)
            newTransport = Transport(
                id, name, valueByKm, timeByKm, Der, Izq, Arr, Aba, DerUp, DerDown, IzqUp, IzqDown)
            self.transports.append(newTransport)

        for place in data["places"]:
            jobs = []
            things = []
            label = place["label"]
            name = place["name"]
            minTimeHere = place["minTimeHere"]
            for job in place["jobs"]:
                namej = job["name"]
                gain = job["gain"]
                timej = job["time"]
                newJob = Jobs(namej, gain, timej)
                jobs.append(newJob)
            for thing in place["things_to_do"]:
                namet = thing["name"]
                cost = thing["cost"]
                timet = thing["time"]
                type = thing["type"]
                newThing = Things(namet, cost, timet, type)
                things.append(newThing)
            self.graph.add_place(label, name, minTimeHere, jobs, things)

        for node in data['places']:
            for goingto in node['goingTo']:
                forms = []
                for transport in self.transports:
                    for t in goingto['transportForms']:
                        if transport.id == t:
                            forms.append(transport)
                self.graph.add_edge(goingto['travelDistance'], self.graph.Get_Vertex(
                    node['label']), self.graph.Get_Vertex(goingto['label']), forms)

        return self.graph
