from graphing.xybasic import BasicGraph
from graphing.xycumulative import CumulativeGraph
from environment.game import Game
from config import Config, MetaConfig


def main():

    #TODO:- take input args to toggle debug mode

    #reads file to list so that indexing is easy
    filename = 'config.txt'
    fileList = []
    try:      
        with open(filename) as f_obj:
            for line in f_obj:
                fileList.append(line)
    except FileNotFoundError:
        msg = "Can't find file {0}.".format(filename)
        print(msg)
        exit

    print("\nFile read succesful...")

    try:
        #config is all information a single game requires
        config = Config(fileList)

        #metaConfig is the information required to run several games in a row
        metaconfig = MetaConfig(fileList)
        if(metaconfig.totalGames > 1): cumulative = CumulativeGraph()

    except IndexError:
        print("\nIssue with config file. Exiting program...\n")
        exit
    
    for x in range(1, metaconfig.totalGames+1):
        population = []
        game = Game(config, 0, population)
        game.initialMorphGen(config)
        results = game.run(config)

        if metaconfig.plotIndiv == 1:
            graph = BasicGraph(results)
            graph.plotResults(config, metaconfig.savePlots, metaconfig.plotDirectory)

        if metaconfig.totalGames > 1:
            cumulative.addGame(results, x)
            updateConfig(config, metaconfig)
    
    #cumulative.plotResults()
    if(metaconfig.savePlots == 1): cumulative.saveResults(metaconfig.plotDirectory)
    print("\nExecution succesful. Deallocating memory and exiting program...\n")

#defined as separate function for clarity in case of extension
def updateConfig(config, metaconfig):
    config.totalPopulation += metaconfig.popIncrement
    config.totalTurns += metaconfig.turnIncrement



if __name__ == "__main__":
    main()