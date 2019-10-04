from .morph import Morph

class YellowMorph(Morph):
    def makeChoice(self, target, config):
        if(isinstance(target, YellowMorph)): return 1
        else: return 0