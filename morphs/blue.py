from .morph import Morph
import random

class BlueMorph(Morph):
    def makeChoice(self, target):
        return random.randint(0,1)
    