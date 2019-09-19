class Morph():
    def __init__(self, energy, repThresh, uniqueId, colourId, formidabilityIndex):
        self.energy = energy
        self.repThresh = repThresh
        self.uniqueId = uniqueId
        self.colourId = colourId
        self.formidabilityIndex = formidabilityIndex

    def getAttributes(self):
        return [self.energy, self.repThresh, self.uniqueId, self.colourId, self.formidabilityIndex]

    def makeChoice(self, target):
        return 
    