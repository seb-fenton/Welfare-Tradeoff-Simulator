import matplotlib.pyplot as plt

class BasicGraph():
    def __init__(self, results):
        self.results = results
        return
    
    def plotResults(self, config, savePlots, plotDirectory):

        ###START TO BREAKDOWN STATS FROM RESULTS###

        xVals = []

        yValsEnergyRed = []
        yValsPopRed = [] 

        yValsEnergyBlue = []
        yValsPopBlue = []

        yValsEnergyGreen = []
        yValsPopGreen = []

        yValsEnergyPink = []
        yValsPopPink = []

        yValsEnergyYellow = []
        yValsPopYellow = []

        yValsEnergyWhite = []
        yValsPopWhite = []

        yValsEnergyBlack = []
        yValsPopBlack = []

        for x in range(0, len(self.results)):
            xVals.append(x)

            yValsEnergyRed.append(self.results[x][0][config.colourMapping['red']])
            yValsPopRed.append(self.results[x][1][config.colourMapping['red']])

            yValsEnergyBlue.append(self.results[x][0][config.colourMapping['blue']])
            yValsPopBlue.append(self.results[x][1][config.colourMapping['blue']])

            yValsEnergyGreen.append(self.results[x][0][config.colourMapping['green']])
            yValsPopGreen.append(self.results[x][1][config.colourMapping['green']])

            yValsEnergyYellow.append(self.results[x][0][config.colourMapping['yellow']])
            yValsPopYellow.append(self.results[x][1][config.colourMapping['yellow']])

            yValsEnergyPink.append(self.results[x][0][config.colourMapping['pink']])
            yValsPopPink.append(self.results[x][1][config.colourMapping['pink']])

            yValsEnergyWhite.append(self.results[x][0][config.colourMapping['white']])
            yValsPopWhite.append(self.results[x][1][config.colourMapping['white']])

            yValsEnergyBlack.append(self.results[x][0][config.colourMapping['black']])
            yValsPopBlack.append(self.results[x][1][config.colourMapping['black']])



        ###ENERGY###

        red, = plt.plot(xVals, yValsEnergyRed, color = 'r')
        red.set_label('Selfish')

        blue, = plt.plot(xVals, yValsEnergyBlue, color = 'b')
        blue.set_label('Random')

        green, = plt.plot(xVals, yValsEnergyGreen, color = 'g')
        green.set_label('Reciprocal')

        pink, = plt.plot(xVals, yValsEnergyPink, color = 'm')
        pink.set_label('Selfless')
        
        yellow, = plt.plot(xVals, yValsEnergyYellow, color = 'y')
        yellow.set_label('Kin-selective')

        white, = plt.plot(xVals, yValsEnergyWhite, color = 'gray')
        white.set_label('Previous action')

        black, = plt.plot(xVals, yValsEnergyBlack, color = 'k')

        plt.title("Energy of Morphs by turn", fontsize=12)
        plt.xlabel("Turns", fontsize=12)
        plt.ylabel("Energy", fontsize=12)
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.grid(True)
        if(config.randomDistrib == 0): plt.legend()

        #Save and show
        if(savePlots == 1): plt.savefig('plots/energy')
        plt.show()



        ###POPULATION###

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

        plt.title("Population of Morphs by turn", fontsize=12)
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
