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
        for i in range(0, len(self.actionMemory)-1):
            if i in self.actionMemory:
                return self.actionMemory[i]
            else: return random.randint(0,1)

    def rememberAction(self, target, action):
        actionMemory[target.getUniqueId()] = action
        return