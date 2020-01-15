import random

class Config():
    """
    A class used to represent ...

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
    """

    def __init__(self, fileList):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """
        self.totalPopulation = int(fileList[2].rstrip(), 10)
        self.totalTurns = int(fileList[4].rstrip(), 10)
        self.indivEnergy = float(fileList[6].rstrip())
        self.tax = float(fileList[8].rstrip())
        self.formidabilityToggle = int(fileList[10].rstrip(), 10)
        self.redPop = int(fileList[12].rstrip(), 10)
        self.bluePop = int(fileList[14].rstrip(), 10)
        self.greenPop = int(fileList[16].rstrip(), 10)
        self.pinkPop = int(fileList[18].rstrip(), 10)
        self.yellowPop = int(fileList[20].rstrip(), 10)
        self.whitePop = int(fileList[22].rstrip(), 10)
        self.blackPop = int(fileList[24].rstrip(), 10)
        self.repThresh = float(fileList[34].rstrip())
        self.selfishReward = float(fileList[40].rstrip())
        self.selflessReward = float(fileList[42].rstrip())
        self.randomDistrib = int(fileList[44].rstrip())
        self.mutationChance = float(fileList[46].rstrip())
        self.gmrc = float(fileList[50].rstrip())

    def setMappings(self):
        if(self.randomDistrib == 0):
            #NORMAL
            self.colourMapping = {'red': 0, 'blue': 1, 'green': 2, 'pink': 3, 'yellow': 4, 'white': 5, 'black': 6}
            self.indexMapping = {0: 'red', 1: 'blue', 2: 'green', 3: 'pink', 4: 'yellow', 5: 'white', 6: 'black'}
            self.formidMapping = {'red': 0, 'blue': 1, 'green': 2, 'pink': 3, 'yellow': 4, 'white': 5, 'black': 6}
        else:
            #RANDOMISED
            randList = [0, 1, 2, 3, 4, 5, 6]
            random.shuffle(randList)
            self.colourMapping = {'red': randList[0], 'blue': randList[1], 'green': randList[2], 'pink': randList[3], 'yellow': randList[4], 'white': randList[5], 'black': randList[6]}
            self.indexMapping = {randList[0]: 'red', randList[1]: 'blue', randList[2]: 'green', randList[3]: 'pink', randList[4]: 'yellow', randList[5]: 'white', randList[6]: 'black'}
            self.formidMapping = {'red': 0, 'blue': 1, 'green': 2, 'pink': 3, 'yellow': 4, 'white': 5, 'black': 6}


class MetaConfig():
    def __init__(self, fileList):
        self.totalGames = int(fileList[26].rstrip(), 10)
        self.popIncrement = int(fileList[28].rstrip(), 10)
        self.turnIncrement = int(fileList[30].rstrip(), 10)
        self.plotIndiv = int(fileList[32].rstrip(), 10)
        self.savePlots = int(fileList[36].rstrip(), 10)
        self.plotDirectory = fileList[38].rstrip()
        self.mergeCumulative = fileList[48].rstrip()