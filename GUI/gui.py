import PySimpleGUI as sg      
import os

def readToConfig(values):
    print(values)
    fileName = 'config.txt'
    fileList = []

    #TODO:- do we need this?
    if(values[2] != None): fileName = values[2]


    try:      
        with open(fileName) as f_obj:
            for line in f_obj:
                fileList.append(line)
    except FileNotFoundError:
        msg = "Can't find file {0}.".format(fileName)
        print(msg)
        exit

    #If anyone has to work this out in the future I'm so sorry, everything is hardcoded to correspond to a certain line in the config.txt
    #Hopefully the labels help a bit

    ###GENERAL###

    #Turns
    fileList[4] = str(values[0]) + "\n"
    #Starting Energy
    fileList[6] = str(values[4]) + "\n"
    #Tax
    fileList[8] = str(values[6]) + "\n"
    #Selfish reward
    fileList[40] = str(values[3]) + "\n"
    #Selfless reward
    fileList[42] = str(values[5]) + "\n"
    #Mutation probability
    fileList[46] = str(values[7]) + "\n"
    #Reproduction threshold
    fileList[34] = str(values[8]) + "\n"

    #Random Dist
    if(values[12] == True): fileList[44] = "1\n"
    else: fileList[44] = "0\n"
    #Plot indiv
    if(values[14] == True): fileList[32] = "1\n"
    else: fileList[32] = "0\n"
    #Save results
    if(values[16] == True): fileList[36] = "1\n"
    else: fileList[36] = "0\n"

    ###POPS###

    #Selfish Red
    fileList[12] = str(values[20]) + "\n"
    #Random Blue
    fileList[14] = str(values[18]) + "\n"
    #Reciprocal Green
    fileList[16] = str(values[19]) + "\n"
    #Selfless Pink
    fileList[18] = str(values[21]) + "\n"
    #Kin-selective Yellow
    fileList[20] = str(values[22]) + "\n"
    #Reactive White
    fileList[22] = str(values[23]) + "\n"

    with open(fileName, 'w') as file:
        file.writelines(fileList)

    return

def readFromConfig():
    fileName = 'config.txt'
    fileList = []

    try:      
        with open(fileName) as f_obj:
            for line in f_obj:
                fileList.append(line)
    except FileNotFoundError:
        msg = "Can't find file {0}.".format(fileName)
        print(msg)
        exit

    inputs = {}

    ###GENERAL###

    #Turns
    inputs['Turns'] = fileList[4].rstrip()
    #Starting Energy
    inputs['Starting energy'] = fileList[6].rstrip()
    #Tax
    inputs['Tax'] = fileList[8].rstrip()
    #Selfish reward
    inputs['Selfish reward'] = fileList[40].rstrip()
    #Selfless reward
    inputs['Selfless reward'] = fileList[42].rstrip()
    #Mutation probability
    inputs['Mutation probability'] = fileList[46].rstrip()
    #Reproduction threshold
    inputs['Reproduction threshold'] = fileList[34].rstrip()

    #Random Dist
    if(fileList[44].rstrip() == str(1)): inputs['Random distribution'] = True
    else: inputs['Random distribution'] = False
    #Plot individual
    if(fileList[32].rstrip() == str(1)): inputs['Plot individual'] = True
    else: inputs['Plot individual'] = False
    #Save results
    if(fileList[36].rstrip() == str(1)): inputs['Save results'] = True
    else: inputs['Save results'] = False

    ###POPS###

    #Selfish Red
    inputs['Redpop'] = fileList[12].rstrip()
    #Random Blue
    inputs['Bluepop'] = fileList[14].rstrip() 
    #Reciprocal Green
    inputs['Greenpop'] = fileList[16].rstrip() 
    #Selfless Pink
    inputs['Pinkpop'] = fileList[18].rstrip() 
    #Kin-selective Yellow
    inputs['Yellowpop'] = fileList[20].rstrip()
    #Reactive White
    inputs['Whitepop'] = fileList[22].rstrip()

    return inputs

def Gui(inputs):

    #sg.ChangeLookAndFeel('GreenTan')      

    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Exit']],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Help', 'About...'], ]      

    # ------ Column Definition ------ #        

    sg.SetOptions(text_justification='right')      

    layout = [[sg.Text('Welfare Tradeoffs', font=('Helvetica', 16))],      
            [sg.Text('Turns', size=(15, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=inputs['Turns'], size=(6, 1)),      
            sg.Text('Games', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=1, size=(6, 1))],      
            [sg.Text('Input Folder', size=(15, 1)), sg.In(default_text='config.txt', size=(10, 1)), sg.Text('Selfish Reward', size=(15, 1)),      
            sg.In(default_text=inputs['Selfish reward'], size=(10, 1))],      
            [sg.Text('Starting Energy', size=(15, 1)), sg.In(default_text=inputs['Starting energy'], size=(10, 1)), sg.Text('Selfless Reward', size=(15, 1)),      
            sg.In(default_text=inputs['Selfless reward'], size=(10, 1))],      
            [sg.Text('Tax', size=(15, 1)), sg.In(default_text=inputs['Tax'], size=(10, 1)), sg.Text('Mutation Probability', size=(15, 1)),      
            sg.In(default_text=inputs['Mutation probability'], size=(10, 1))],
            [sg.Text('Reproduction threshold', size=(15, 1)), sg.In(default_text=inputs['Reproduction threshold'], size=(10, 1)), sg.Text('Placeholder', size=(15, 1)),      
            sg.In(default_text=0, size=(10, 1))],
            [sg.Text('_'  * 100, size=(65, 1))], 
            [sg.Text('Multi-game options',font=('Helvetica', 15), justification='left')],
            [sg.Text('Pop. Increment', size=(15, 1)), sg.In(default_text='0', size=(10, 1)), sg.Text('Turn Increment', size=(15, 1)),      
            sg.In(default_text='0', size=(10, 1))],          
            [sg.Text('_'  * 100, size=(65, 1))],      
            [sg.Text('Toggles', font=('Helvetica', 15), justification='left')],      
            [sg.Checkbox('Random Distribution', size=(12, 1), default=inputs['Random distribution']), sg.Checkbox('Formidability', size=(20, 1))],      
            [sg.Checkbox('Plot individual games', size=(12, 1), default=inputs['Plot individual']), sg.Checkbox('Placeholder', size=(20, 1), default=True)],      
            [sg.Checkbox('Save results', default=inputs['Save results'], size=(12, 1)), sg.Checkbox('Placeholder', size=(20, 1))],      
            [sg.Text('_'  * 100, size=(65, 1))],      
            [sg.Text('Starting Populations', font=('Helvetica', 15), justification='left')],      
            [sg.Text('Random', size=(15, 1)), sg.In(default_text=inputs['Bluepop'], size=(10, 1)),      
            sg.Text('Reciprocal', size=(15, 1)), sg.In(default_text=inputs['Greenpop'], size=(10, 1))],      
            [sg.Text('Selfish', size=(15, 1)), sg.In(default_text=inputs['Redpop'], size=(10, 1)),
            sg.Text('Selfless', size=(15, 1)), sg.In(default_text=inputs['Pinkpop'], size=(10, 1))],      
            [sg.Text('Kin-selective', size=(15, 1)), sg.In(default_text=inputs['Yellowpop'], size=(10, 1)),      
            sg.Text('Reactionary', size=(15, 1)), sg.In(default_text=inputs['Whitepop'], size=(10, 1))],          
            [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('Welfare Tradeoffs', layout, font=("Helvetica", 12))

    # Event Loop to process "events" and get the "values" of the inputs
    while True:             
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            window.close()
            break
        elif event in ('Submit'):
            readToConfig(values)
            os.system('python3 main.py')


def main():

    inputs = readFromConfig()
    Gui(inputs)

    return



if __name__ == "__main__":
    main()






'''sg.Popup('Title',      
     'The results of the window.',      
     'The button clicked was "{}"'.format(event),      
     'The values are', values) '''