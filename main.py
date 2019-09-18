#imports
from .graphing.xybasic import BasicGraph

if __name__ == "__main__":

    #reads file to list so that indexing is easy
    filename = 'config.txt'
    fileList = []
    with open(filename) as f_obj:
        for line in f_obj:
            fileList.append(line)

    #initialise config variables
    config = []

    totalEnergy = fileList[2]
    config.append(totalEnergy)

    totalTurns = fileList[4]
    config.append(totalTurns)

    indivEnergy = fileList[6]
    config.append(indivEnergy)

    tax = fileList[8]
    config.append(tax)

    
    