import matplotlib.pyplot as plt


class CumulativeGraph():
    
    def __init__(self):
        self.results = []
        return

    def addGame(self, game):
        self.results.append(game)
        return

    def plotUnMergedResults(self, savePlots, plotDirectory, config):
        return
    
    def plotMergedResults(self, savePlots, plotDirectory, config):

        xVals = []
        yValsPopRed = [] 
        yValsPopBlue = []
        yValsPopGreen = []
        yValsPopPink = []
        yValsPopYellow = []
        yValsPopWhite = []
        yValsPopBlack = []

        for y in range(0, len(self.results)): 
            for x in range(0, len(self.results[y])):
                if(y==0): 
                    xVals.append(x)
                    yValsPopRed.append(self.results[y][x][1][config.colourMapping['red']])
                    yValsPopBlue.append(self.results[y][x][1][config.colourMapping['blue']])
                    yValsPopGreen.append(self.results[y][x][1][config.colourMapping['green']])
                    yValsPopYellow.append(self.results[y][x][1][config.colourMapping['yellow']])
                    yValsPopPink.append(self.results[y][x][1][config.colourMapping['pink']])
                    yValsPopWhite.append(self.results[y][x][1][config.colourMapping['white']])
                    yValsPopBlack.append(self.results[y][x][1][config.colourMapping['black']])
                else:
                    yValsPopRed[x] += (self.results[y][x][1][config.colourMapping['red']])
                    yValsPopBlue[x] += (self.results[y][x][1][config.colourMapping['blue']])
                    yValsPopGreen[x] += (self.results[y][x][1][config.colourMapping['green']])
                    yValsPopYellow[x] += (self.results[y][x][1][config.colourMapping['yellow']])
                    yValsPopPink[x] += (self.results[y][x][1][config.colourMapping['pink']])
                    yValsPopWhite[x] += (self.results[y][x][1][config.colourMapping['white']])
                    yValsPopBlack[x] += (self.results[y][x][1][config.colourMapping['black']])

        red, = plt.plot(xVals, yValsPopRed, color = 'r')
        red.set_label('Selfish')
        blue, = plt.plot(xVals, yValsPopBlue, color = 'b')
        blue.set_label('Random')
        green, = plt.plot(xVals, yValsPopGreen, color = 'g')
        green.set_label('Reciprocal')
        pink, = plt.plot(xVals, yValsPopPink, color = 'm')
        pink.set_label('Selfless')
        yellow, = plt.plot(xVals, yValsPopYellow, color = 'y')
        yellow.set_label('Kin-selective')
        white, = plt.plot(xVals, yValsPopWhite, color = 'gray')
        white.set_label('Previous action')
        black, = plt.plot(xVals, yValsPopBlack, color = 'k')
        plt.title("Cumulative Population of Morphs by turn", fontsize=12)
        plt.xlabel("Turns", fontsize=12)
        plt.ylabel("Population", fontsize=12)
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.grid(True)
        if(config.randomDistrib == 0): plt.legend()

        #print("###CONFIG###")
        #config.prettyPrint()

        #Logarithmic check
        startingPop = config.redPop + config.bluePop + config.greenPop + config.yellowPop + config.pinkPop + config.whitePop + config.blackPop
        totalPop = yValsPopBlue[-1] + yValsPopGreen[-1] + yValsPopRed[-1] + yValsPopYellow[-1] + yValsPopPink[-1] + yValsPopWhite[-1]
        if(totalPop >= 100*startingPop): plt.yscale('log')
        if(savePlots == 1): plt.savefig('plots/pop')
        plt.show()
        
        return
