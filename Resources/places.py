from math import inf
from pygame import Rect


class Place:
    def __init__(self, label, name, minTimeHere, jobs, things):
        self.label = label
        self.name = name
        self.minTimeHere = minTimeHere
        self.jobs = jobs
        self.things = things
        self.goings = []
        self.x = 0
        self.y = 0
        self.statusD = [inf, None]
        self.status = [inf, None]
        self.statusT = [inf, None]
        self.jobsFinish = []
        self.activityFinish = []
        self.rect = Rect(0, 0, 110, 90)

    def __eq__(self, place):
        return (self.label == place.label and self.name == place.name and
                self.minTimeHere == place.minTimeHere and self.jobs == place.jobs and self.things == place.things)
