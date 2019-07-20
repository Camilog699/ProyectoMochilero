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

    def __eq__(self, place):
        return (self.label == place.label and self.name == place.name and
                self.minTimeHere == place.minTimeHere and self.jobs == place.jobs and self.things == place.things)
