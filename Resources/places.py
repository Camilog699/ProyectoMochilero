from math import inf
from pygame import Rect

class Place:
    def __init__(self, label, name, minTimeHere, jobs, things):
        self.label = label
        self.name = name
        self.minTimeHere = minTimeHere
        self.jobs = []
        self.things = []
        self.goings = []
        self.x = 0
        self.y = 0
        self.status= [inf, None]
        self.rect = Rect(0, 0, 85, 60)

    def __eq__(self, place):
        return (self.label == place.label and self.name == place.name and
                self.minTimeHere == place.minTimeHere and self.jobs == place.jobs and self.things == place.things)
