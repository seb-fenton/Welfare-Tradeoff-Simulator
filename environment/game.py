from ..morphs.red import RedMorph
from ..morphs.blue import BlueMorph
from ..morphs.green import GreenMorph
from ..morphs.pink import PinkMorph
from ..morphs.yellow import YellowMorph
from ..morphs.white import WhiteMorph
from ..morphs.black import BlackMorph
from ..config import *

class Game():
    def __init__(self, config):
        self.uniqueId = 0

        #generate morphs
        self.population = []

        #this is probably very inefficient but I'm not a python guru so idk
        for x in range(0, config.redPop):
            newMorph = RedMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['red'], config.formidMapping['red'])
            population.append(newMorph)

        for x in range(0, config.bluePop):
            newMorph = BlueMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['blue'], config.formidMapping['blue'])
            population.append(newMorph)

        for x in range(0, config.greenPop):
            newMorph = GreenMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['green'], config.formidMapping['green'])
            population.append(newMorph)

        for x in range(0, config.pinkPop):
            newMorph = PinkMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['pink'], config.formidMapping['pink'])
            population.append(newMorph)

        for x in range(0, config.yellowPop):
            newMorph = YellowMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['yellow'], config.formidMapping['yellow'])
            population.append(newMorph)

        for x in range(0, config.whitePop):
            newMorph = WhiteMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['white'], config.formidMapping['white'])
            population.append(newMorph)

        for x in range(0, config.blackPop):
            newMorph = BlackMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['black'], config.formidMapping['black'])
            population.append(newMorph)

    def run(self, config):
        results = []
        for x in range(1,config.totalTurns):
            self.popShuffle()
            self.morphChoices()
            results.append(self.generateStats())
        return results

    def morphChoices(self, config):
        #TODO:- make this ternary operator
        #toggle guarantees no issues for odd population, just leaves first morph in list alone
        toggle = 1
        if(config.totalPopulation % 2 == 1): toggle = 2

        reproduction = []
        death = []

        for x in range(toggle, config.totalPopulation):
            population[x].makeChoice(population[x+1])
            #checkChange checks for reproduction/death

            if(population[x].checkChange() == 1): reproduction.append(x)
            elif(population[x].checkChange() == 2): death.append(x)

            if(population[x+1].checkChange() == 1): reproduction.append(x+1)
            elif(population[x+1].checkChange() == 2): death.append(x)
            x+=1
        
        self.consolate(population, reproduction, death)

    def consolate(self, population, reproduction, death):
        return

    def generateStats(self, population):
        return

    def popShuffle(self):
        #TODO:- self.pop.randomshuffle, somehow
        return

    def idGen(self):
        uniqueId += 1
        return uniqueId
        


    