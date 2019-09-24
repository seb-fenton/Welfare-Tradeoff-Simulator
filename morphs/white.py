from .morph import Morph

class WhiteMorph(Morph):
    def __init__(self, energy, repThresh, uniqueId, colourId, formidabilityIndex):
        self.energy = energy
        self.repThresh = repThresh
        self.uniqueId = uniqueId
        self.colourId = colourId
        self.formidabilityIndex = formidabilityIndex
        self.actionMemory = 0

    def makeChoice(self, target, config):
        if(self.actionMemory == 0): return 0 
        else: return 1

    def rememberAction(self, target, action):
        #taking target is redundant but it makes the code neater in game
        #optimise area in future if needed
        actionMemory = action
        return