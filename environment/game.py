from morphs.red import RedMorph
from morphs.blue import BlueMorph
from morphs.green import GreenMorph
from morphs.pink import PinkMorph
from morphs.yellow import YellowMorph
from morphs.white import WhiteMorph
from morphs.black import BlackMorph
from morphs.morph import Morph
from config import Config, MetaConfig
import random

class Game():
    def __init__(self, config, uniqueId, population):
        self.uniqueId = uniqueId
        self.population = population
        self.deadList = []
        self.greenPopulation = []
        self.tempGreenPopulation = []

    #this is a separate function because it was shitting itself & I'm not a good enough python coder to bother working out what was going wrong
    def initialMorphGen(self, config):
        for x in range(0, config.redPop):
            config.setMappings()
            newMorph = RedMorph(config.indivEnergy, config.repThresh, self.uniqueId, config.colourMapping['red'], config.formidMapping['red'])
            self.population.append(newMorph)
            self.uniqueId += 1

        for x in range(0, config.bluePop):
            config.setMappings()
            newMorph = BlueMorph(config.indivEnergy, config.repThresh, self.uniqueId, config.colourMapping['blue'], config.formidMapping['blue'])
            self.population.append(newMorph)
            self.uniqueId += 1

        for x in range(0, config.greenPop):
            config.setMappings()
            newMorph = GreenMorph(config.indivEnergy, config.repThresh, self.uniqueId, config.colourMapping['green'], config.formidMapping['green'])
            self.population.append(newMorph)
            self.uniqueId += 1

        for x in range(0, config.pinkPop):
            config.setMappings()
            newMorph = PinkMorph(config.indivEnergy, config.repThresh, self.uniqueId, config.colourMapping['pink'], config.formidMapping['pink'])
            self.population.append(newMorph)
            self.uniqueId += 1

        for x in range(0, config.yellowPop):
            config.setMappings()
            newMorph = YellowMorph(config.indivEnergy, config.repThresh, self.uniqueId, config.colourMapping['yellow'], config.formidMapping['yellow'])
            self.population.append(newMorph)
            self.uniqueId += 1

        for x in range(0, config.whitePop):
            config.setMappings()
            newMorph = WhiteMorph(config.indivEnergy, config.repThresh, self.uniqueId, config.colourMapping['white'], config.formidMapping['white'])
            self.population.append(newMorph)
            self.uniqueId += 1

        for x in range(0, config.blackPop):
            config.setMappings()
            newMorph = BlackMorph(config.indivEnergy, config.repThresh, self.uniqueId, config.colourMapping['black'], config.formidMapping['black'])
            self.population.append(newMorph)
            self.uniqueId += 1

    def run(self, config):
        results = []
        for x in range(1,config.totalTurns):
            print("Turn: ", x)
            random.shuffle(self.population)
            self.handleGreens(config)
            self.morphModification(config)
            results.append(self.generateStats(config))
            self.greenPopulation = []
            self.tempGreenPopulation = []
        return results

    def morphModification(self, config):
        #toggle guarantees no issues for odd population, just leaves last morph in list alone
        toggle = 0
        if(len(self.population) % 2 == 1): toggle = 1

        reproduction = []
        death = []

        #TODO ISSUE HERE FOR ODD NUMBERS - MAKE THEM ALWAYS SELFISH
        for x in range(0, len(self.population)-toggle-1, 2):
            #choice
            #print("Start of Turn: \nActor: ", self.population[x].getColour(), "C ", self.population[x].getEnergy(), "H\n")
            #print("Actee: ", self.population[x+1].getColour(), "C ", self.population[x+1].getEnergy(), "\n")

            choice = self.population[x].makeChoice(self.population[x+1], config)
            if(choice == 0): self.population[x].addEnergy(config.selfishReward)
            elif(choice == 1): self.population[x+1].addEnergy(config.selflessReward)

            if(isinstance(self.population[x+1], GreenMorph) | isinstance(self.population[x+1], WhiteMorph)): 
                self.population[x+1].rememberAction(self.population[x].getUniqueId(), choice)

            #print("Choice: ", choice, " | Actor: ", self.population[x].getColour(), " | Actee: ", self.population[x+1].getColour())

            #tax
            self.population[x].removeEnergy(config.tax)
            self.population[x+1].removeEnergy(config.tax)

            #print("End of turn: \nActor: ", self.population[x].getColour(), "C ", self.population[x].getEnergy(), "\n")
            #print("Actee: ", self.population[x+1].getColour(), "C ", self.population[x+1].getEnergy(), "\n")

            #checkChange checks for reproduction/death
            if(self.population[x].checkChange() == 1): reproduction.append(x)
            elif(self.population[x].checkChange() == 2): death.append(x)

            #print("Actor checkchange: ", self.population[x].checkChange(), "\n")

            if(self.population[x+1].checkChange() == 1): reproduction.append(x+1)
            elif(self.population[x+1].checkChange() == 2): death.append(x)

            #print("Actee checkchange: ", self.population[x+1].checkChange(), "\n")

        if(len(self.population)==1):
            self.population[0].addEnergy(config.selfishReward)
            self.population[0].removeEnergy(config.tax)
            if(self.population[0].checkChange() == 1): reproduction.append(0)
            elif(self.population[0].checkChange() == 2): death.append(0)
        elif(toggle==1):
            self.population[len(self.population)-1].addEnergy(config.selfishReward)
            self.population[len(self.population)-1].addEnergy(config.selfishReward)
            if(self.population[len(self.population)-1].checkChange() == 1): reproduction.append(0)
            elif(self.population[len(self.population)-1].checkChange() == 2): death.append(0)


        
        self.consolate(reproduction, death, config)

    def consolate(self, reproduction, death, config):
        #done before death so that indices don't screw up
        for x in reproduction:
            self.population[x].removeEnergy(config.tax)
            newMorph = self.genMorph(self.population[x].getColour(), config)
            self.population.append(newMorph)

        #goes backwards so that indices don't screw up
        for x in sorted(death, reverse=True):
            self.deadList.append(self.population[x].uniqueId)
            del self.population[x]

        return

    def genMorph(self, colour, config):

        mutationCheck = random.randint(1,100)
        colourName = ''

        #initial check for 0 technically redundant but optimises code
        if(config.mutationChance == 0): colourName = config.indexMapping[colour]
        elif(mutationCheck < config.mutationChance):
            randIndex = random.randint(0, len(config.indexMapping) - 1)
            colourName = config.indexMapping[randIndex]
        else: colourName = config.indexMapping[colour]


        if(colourName == 'red'): 
            newMorph = RedMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['red'], config.formidMapping['red'])
            return newMorph
        elif(colourName == 'blue'): 
            newMorph = BlueMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['blue'], config.formidMapping['blue'])
            return newMorph
        elif(colourName == 'green'): 
            newMorph = GreenMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['green'], config.formidMapping['green'])
            return newMorph
        elif(colourName == 'pink'): 
            newMorph = PinkMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['pink'], config.formidMapping['pink'])
            return newMorph
        elif(colourName == 'yellow'): 
            newMorph = YellowMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['yellow'], config.formidMapping['yellow'])
            return newMorph
        elif(colourName == 'white'): 
            newMorph = WhiteMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['white'], config.formidMapping['white'])
            return newMorph
        elif(colourName == 'black'): 
            newMorph = BlackMorph(config.indivEnergy, config.repThresh, self.idGen(), config.colourMapping['black'], config.formidMapping['black'])
            return newMorph

    def generateStats(self, config):
        energyStats = [0] * len(config.colourMapping)
        popStats = [0] * len(config.colourMapping)

        for x in range(0, len(self.population)): 
            colour = self.population[x].getColour()
            energyStats[colour] += self.population[x].getEnergy()
            popStats[colour] += 1
        results = [energyStats, popStats]
        return results

    def idGen(self):
        self.uniqueId += 1
        return self.uniqueId

    def isAlive(self, uniqueId):
        for morph in self.deadList:
            if morph == uniqueId: return False
        return True
        



    def handleGreens(self, config):
        #generate pairs
        lockList = [] #reserves morphs so that they don't get selected multiple times
        for morph in self.population:
            if(morph.colourId == config.colourMapping['green']):
                #TODO(seb): let gui modify gmrc
                if (random.random() < config.gmrc): continue
                for pair in morph.actionMemory:
                    if self.isAlive(pair) and pair not in lockList: 
                        self.greenPopulation.append([morph.uniqueId, pair])
                        lockList.append(pair)
                        lockList.append(morph.uniqueId)
        
        #generate list of morphs to delete and create a temp list of saved greens
        deleteList = []
        for morph in self.population: 
            for uniqueIdPair in self.greenPopulation:
                if(morph.uniqueId == (uniqueIdPair[0] or uniqueIdPair[1])):
                    self.tempGreenPopulation.append(morph)
                    deleteList.append(morph.uniqueId)
        #remove paired morphs from main list
        for morph in self.population:
            if morph.uniqueId in deleteList: del morph
        
        tempTempMorphHolder = []
        #sort the temp green list into its pairs
        for morph in self.tempGreenPopulation:
            for pair in self.greenPopulation:
                if morph.uniqueId == pair[0]:
                    for pairmorph in self.tempGreenPopulation:
                        if pairmorph.uniqueId == pair[1]:
                            tempTempMorphHolder.append(morph)
                            tempTempMorphHolder.append(pairmorph)
                elif morph.uniqueId == pair[1]:
                    for pairmorph in self.tempGreenPopulation:
                        if pairmorph.uniqueId == pair[0]:
                            tempTempMorphHolder.append(pairmorph)
                            tempTempMorphHolder.append(morph) 
        print(self.greenPopulation)
        print(tempTempMorphHolder)

        #append the pairs to the original population list
        for morph in tempTempMorphHolder:
            self.population.append(morph)