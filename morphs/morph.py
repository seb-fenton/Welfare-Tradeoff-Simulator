class Morph():
    def __init__(self, energy, repThresh, uniqueId, colourId, formidabilityIndex):
        self.energy = energy
        self.repThresh = repThresh
        self.uniqueId = uniqueId
        self.colourId = colourId
        self.formidabilityIndex = formidabilityIndex

    def getAttributes(self):
        return [self.energy, self.repThresh, self.uniqueId, self.colourId, self.formidabilityIndex]

    def getColour(self):
        return self.colourId
    
    def getUniqueId(self):
        return self.uniqueId

    def getEnergy(self):
        return self.energy

    def makeChoice(self, target, config):
        return 0

    def checkChange(self):
        if(self.energy <= 0): return 2
        elif(self.energy >= self.repThresh): return 1
        else: return 0
        return

    def removeEnergy(self, modifier):
        self.energy = self.energy - modifier
        return

    def addEnergy(self, modifier):
        self.energy += modifier
        return
    