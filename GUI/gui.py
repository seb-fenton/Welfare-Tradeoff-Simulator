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
    fileList[4] = str(values[0]) + "\n"
    fileList[6] = str(values[4]) + "\n"
    fileList[8] = str(values[6]) + "\n"
    fileList[40] = str(values[3]) + "\n"
    fileList[42] = str(values[5]) + "\n"

    #colour pops
    fileList[12] 

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
          [sg.Checkbox('Random Distribution', size=(12, 1), default=True), sg.Checkbox('Formidability', size=(20, 1))],      
          [sg.Checkbox('Plot individual games', size=(12, 1)), sg.Checkbox('N/A', size=(20, 1), default=True)],      
          [sg.Checkbox('Save results', default=True, size=(12, 1)), sg.Checkbox('N/A', size=(20, 1))],      
          [sg.Text('_'  * 100, size=(65, 1))],      
          [sg.Text('Starting Populations', font=('Helvetica', 15), justification='left')],      
          [sg.Text('Random', size=(15, 1)), sg.In(default_text='1', size=(10, 1)),      
           sg.Text('Reciprocal', size=(15, 1)), sg.In(default_text='1', size=(10, 1))],      
          [sg.Text('Selfish', size=(15, 1)), sg.In(default_text='1', size=(10, 1)),
           sg.Text('Selfless', size=(15, 1)), sg.In(default_text='1', size=(10, 1))],      
          [sg.Text('Kin-selective', size=(15, 1)), sg.In(default_text='1', size=(10, 1)),      
           sg.Text('Reactionary', size=(15, 1)), sg.In(default_text='1', size=(10, 1))],          
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