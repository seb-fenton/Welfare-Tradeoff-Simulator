from .morph import Morph
import random

class BlackMorph(Morph):
    def makeChoice(self, target, config):
        return random.randint(0,1)