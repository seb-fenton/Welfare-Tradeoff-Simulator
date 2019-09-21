import matplotlib.pyplot as plt

class BasicGraph():
    def __init__(self, results):
        self.results = results
        return
    
    def plotResults(self, config, savePlots, plotDirectory):
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

            yValsEnergyYellow.append(self.results[x][0][config.colourMapping['pink']])
            yValsPopYellow.append(self.results[x][1][config.colourMapping['pink']])

            yValsEnergyPink.append(self.results[x][0][config.colourMapping['yellow']])
            yValsPopPink.append(self.results[x][1][config.colourMapping['yellow']])

            yValsEnergyWhite.append(self.results[x][0][config.colourMapping['white']])
            yValsPopWhite.append(self.results[x][1][config.colourMapping['white']])

            yValsEnergyBlack.append(self.results[x][0][config.colourMapping['black']])
            yValsPopBlack.append(self.results[x][1][config.colourMapping['black']])


        plt.plot(xVals, yValsEnergyRed, color = 'r')
        plt.plot(xVals, yValsEnergyBlue, color = 'b')
        plt.plot(xVals, yValsEnergyGreen, color = 'g')
        plt.plot(xVals, yValsEnergyPink, color = 'm')
        plt.plot(xVals, yValsEnergyYellow, color = 'y')
        plt.plot(xVals, yValsEnergyWhite, color = 'w')
        plt.plot(xVals, yValsEnergyBlack, color = 'k')

        plt.show()
        if(savePlots == 1): plt.save(plotDirectory)

        plt.plot(xVals, yValsPopRed, color = 'r')
        plt.plot(xVals, yValsPopBlue, color = 'b')
        plt.plot(xVals, yValsPopGreen, color = 'g')
        plt.plot(xVals, yValsPopPink, color = 'm')
        plt.plot(xVals, yValsPopYellow, color = 'y')
        plt.plot(xVals, yValsPopWhite, color = 'w')
        plt.plot(xVals, yValsPopBlack, color = 'k')

        plt.show()
        if(savePlots == 1): plt.save(plotDirectory)

        return
