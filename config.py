class Config():
    def __init__(self, fileList):
        self.colourMapping = {'red': 0, 'blue': 1, 'green': 2, 'pink': 3, 'yellow': 4, 'white': 5, 'black': 6}
        self.indexMapping = {0: 'red', 1: 'blue', 2: 'green', 3: 'pink', 4: 'yellow', 5: 'white', 6: 'black'}
        self.formidMapping = {'red': 0, 'blue': 1, 'green': 2, 'pink': 3, 'yellow': 4, 'white': 5, 'black': 6}
        
        #TODO:- rework to use split so it's less cancer
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


class MetaConfig():
    def __init__(self, fileList):

        #TODO:- strip whitespace & convert all these strings to numericals
        self.totalGames = int(fileList[26].rstrip(), 10)

        self.popIncrement = int(fileList[28].rstrip(), 10)

        self.turnIncrement = int(fileList[30].rstrip(), 10)

        self.plotIndiv = int(fileList[32].rstrip(), 10)
        
        self.savePlots = int(fileList[36].rstrip(), 10)

        self.plotDirectory = fileList[38].rstrip()