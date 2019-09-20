from .morph import Morph

class GreenMorph(Morph):
    def __init__(self, energy, repThresh, uniqueId, colourId, formidabilityIndex):
        self.energy = energy
        self.repThresh = repThresh
        self.uniqueId = uniqueId
        self.colourId = colourId
        self.formidabilityIndex = formidabilityIndex
        self.actionMemory = {}

    def makeChoice(self, target):
        return 0

    def rememberAction(self, target, action):
        actionMemory[target.getUniqueId()] = action
        return
        #use a dictionary for this?