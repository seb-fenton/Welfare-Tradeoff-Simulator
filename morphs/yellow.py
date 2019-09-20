from .morph import Morph

class YellowMorph(Morph):
    def makeChoice(self, target, config):
        if(target.getColour() == config.colourMapping['yellow']): return 1
        else: return 0