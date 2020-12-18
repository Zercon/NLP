import pandas
import numpy
from ipymarkup.palette import palette
from ipymarkup.palette import Color
from ipymarkup.palette import material
from yargy import Parser
from ipymarkup import show_span_box_markup as show_markup
from yargy.interpretation import fact

from PlacesRules import ADDRESS
from NamesRules import FULLNAME

class PersonNERHypothesis:

    def __init__(self):
        self.finder = Parser(FULLNAME)

    def find(self, data):
        founds = list(self.finder.findall(data))
        if (len(founds)):
            return founds[0].fact
        else:
            return None
            
    def getFullName(self, data):
        found = self.find(data)
        if (found):
            return (found.name, found.patr, found.surn)
        else:
            return (None, None, None)

# test = PersonNERHypothesis()
# print('result= ', test.getFullName('Иванов Петр Васильевич'))

class AddressNERHypothesis:
    def __init__(self):
        self.finder = Parser(ADDRESS)

    def find(self, data):
        founds = list(self.finder.findall(data))
        if (len(founds)):
            return founds[0].fact
        else:
            return None

    def getCity(self, data):
        found = self.find(data)
        if (found and found.city):
            return (found.city.title, found.city.type)
        else:
            return (None, None)

    def getStreet(self, data):
        found = self.find(data)
        if (found and found.street):
            return (found.street.title, found.street.type)
        else:
            return (None, None)

    def getBuilding(self, data):
        found = self.find(data)
        if (found and found.building):
            return (found.building.house, found.building.corpus, found.building.structure)
        else:
            return (None, None, None)

    def getAppartment(self, data):
        found = self.find(data)
        if (found and found.appartment):
            return found.appartment
        else:
            return None

    def getSPb(self, data):
        spb = []
        spb.append(self.getCity(data))
        spb.append(self.getStreet(data))
        spb.append(self.getBuilding(data))
        return spb

    def getTotalAddress(self, data):
        ta = []
        ta.append(self.getCity(data))
        ta.append(self.getStreet(data))
        ta.append(self.getBuilding(data))
        ta.append(self.getAppartment(data))
        return ta