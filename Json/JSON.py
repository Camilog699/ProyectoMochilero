from Resources.graph import Graph
from Resources.transport import Transport
from Resources.jobs import Jobs
from Resources.things import Things
from Resources.places import Place
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

        for trans in data["transportForm"]:
            id = trans["id"]
            name = trans["id"]
            valueByKm = trans["valueByKm"]
            timeByKm = trans["timeByKm"]
            newTransport = Transport(id, name, valueByKm, timeByKm)
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
                self.jobs.append(newJob)
            for thing in place["things_to_do"]:
                namet = thing["name"]
                cost = thing["cost"]
                timet = thing["time"]
                type = thing["type"]
                newThing = Things(namet, cost, timet, type)
                self.things.append(newThing)

        for node in data['places']:
            for goingto in node['goingTo']:
                forms = []
                for transport in self.transports:
                    for t in goingto['transportForm']:
                        if transport.id == t:
                            forms.append(transport)
                self.graph.add_edge(goingto['travelDistance'], self.graph.Get_Vertex(
                    node['label']),  self.graph.Get_Vertex(goingto['label']), forms)
