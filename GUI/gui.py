import PySimpleGUI as sg      
import os

def readToConfig(values):
    print(values)
    fileName = 'config.txt'
    fileList = []

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

    #Random Dist
    if(values[10] == True): fileList[44] = "1\n"
    else: fileList[44] = "0\n"
    #Plot indiv
    if(values[12] == True): fileList[32] = "1\n"
    else: fileList[32] = "0\n"
    #Save results
    if(values[14] == True): fileList[36] = "1\n"
    else: fileList[36] = "0\n"

    ###POPS###

    #Selfish Red
    fileList[12] = str(values[18]) + "\n"
    #Random Blue
    fileList[14] = str(values[16]) + "\n"
    #Reciprocal Green
    fileList[16] = str(values[17]) + "\n"
    #Selfless Pink
    fileList[18] = str(values[19]) + "\n"
    #Kin-selective Yellow
    fileList[20] = str(values[20]) + "\n"
    #Reactive White
    fileList[22] = str(values[21]) + "\n"

    with open(fileName, 'w') as file:
        file.writelines(fileList)

    return

#sg.ChangeLookAndFeel('GreenTan')      

# ------ Menu Definition ------ #      
menu_def = [['File', ['Exit']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Help', 'About...'], ]      

# ------ Column Definition ------ #        

sg.SetOptions(text_justification='right')      

layout = [[sg.Text('Welfare Tradeoffs', font=('Helvetica', 16))],      
          [sg.Text('Turns', size=(15, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1)),      
           sg.Text('Games', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=1, size=(6, 1))],      
          [sg.Text('Input Folder', size=(15, 1)), sg.In(default_text='config.txt', size=(10, 1)), sg.Text('Selfish Reward', size=(15, 1)),      
           sg.In(default_text='4', size=(10, 1))],      
          [sg.Text('Starting Energy', size=(15, 1)), sg.In(default_text='8', size=(10, 1)), sg.Text('Selfless Reward', size=(15, 1)),      
           sg.In(default_text='6', size=(10, 1))],      
          [sg.Text('Tax', size=(15, 1)), sg.In(default_text='4', size=(10, 1)), sg.Text('Mutation Probability', size=(15, 1)),      
           sg.In(default_text='0', size=(10, 1))],
          [sg.Text('_'  * 100, size=(65, 1))], 
          [sg.Text('Multi-game options',font=('Helvetica', 15), justification='left')],
          [sg.Text('Pop. Increment', size=(15, 1)), sg.In(default_text='0', size=(10, 1)), sg.Text('Turn Increment', size=(15, 1)),      
           sg.In(default_text='0', size=(10, 1))],          
          [sg.Text('_'  * 100, size=(65, 1))],      
          [sg.Text('Toggles', font=('Helvetica', 15), justification='left')],      
          [sg.Checkbox('Random Distribution', size=(12, 1), default=False), sg.Checkbox('Formidability', size=(20, 1))],      
          [sg.Checkbox('Plot individual games', size=(12, 1), default=True), sg.Checkbox('N/A', size=(20, 1), default=True)],      
          [sg.Checkbox('Save results', default=True, size=(12, 1)), sg.Checkbox('N/A', size=(20, 1))],      
          [sg.Text('_'  * 100, size=(65, 1))],      
          [sg.Text('Starting Populations', font=('Helvetica', 15), justification='left')],      
          [sg.Text('Random', size=(15, 1)), sg.In(default_text='20', size=(10, 1)),      
           sg.Text('Reciprocal', size=(15, 1)), sg.In(default_text='20', size=(10, 1))],      
          [sg.Text('Selfish', size=(15, 1)), sg.In(default_text='20', size=(10, 1)),
           sg.Text('Selfless', size=(15, 1)), sg.In(default_text='20', size=(10, 1))],      
          [sg.Text('Kin-selective', size=(15, 1)), sg.In(default_text='20', size=(10, 1)),      
           sg.Text('Reactionary', size=(15, 1)), sg.In(default_text='20', size=(10, 1))],          
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







'''sg.Popup('Title',      
     'The results of the window.',      
     'The button clicked was "{}"'.format(event),      
     'The values are', values) '''