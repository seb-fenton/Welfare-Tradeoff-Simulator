from .morph import Morph
import random

class GreenMorph(Morph):
    def __init__(self, energy, repThresh, uniqueId, colourId, formidabilityIndex):
        self.energy = energy
        self.repThresh = repThresh
        self.uniqueId = uniqueId
        self.colourId = colourId
        self.formidabilityIndex = formidabilityIndex
        self.actionMemory = {}

    def makeChoice(self, target, config):
        if(len(self.actionMemory) == 0): 
            return 1
        for i in range(0, len(self.actionMemory)-1):
            if target in self.actionMemory:
                return self.actionMemory[target]
        return 1

    def rememberAction(self, target, action):
        self.actionMemory[target] = action
        return