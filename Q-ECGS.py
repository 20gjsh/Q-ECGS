from tkinter import *
import os

#Create parent window
root = Tk()
root.title("Q-ECGS")

def spaceRemover(userString): 
    '''
    Replaces all underlines _ with a space from an inputted string

    Parameters:
        userString (string): The inputted string containing underlines that you would like replaced with spaces
    
    Returns:
        newString (string): Returns the input string without underlines but with spaces instead
    '''
    
    newString = ''
    #Iterates over the inputted string to check where the underlines are and replaces them with spaces
    for i in userString:
        if i == '_': newString += ' '
        else: newString += i
    
    return newString


class rhythm:
    '''Class used to simplify the button functionality. Gives a name and path for every sinus rhythm'''
    def __init__(self, name):
        self.name = spaceRemover(name) #Removes the underlines, as those were only there for calling the file more easily but we want to display with spaces.
        self.path = './gifs/' + name + '.gif'
    
    def openGif(self):
        os.system("taskkill /IM Microsoft.Photos.exe /F")
        os.system("start "+ self.path)

#Defines all the Rhythms used into a dictionary and list for iterating over.
sinusRhythms = ['NORMAL_SINUS','TACHYCARDIA','BRADYCARDIA']
sinusDysrhythmias = ['SEGMENT_ELEVATION', 'SEGMENT_DEPRESSION']
atrialRhythms = ['ATRIAL_FLUTTER','ATRIAL_TACHYCARDIA']
junctionalRhythms = ['JUNCTIONAL_RHYTHM','JUNCTIONAL_TACHYCARDIA']
AVblockage = ['1ST_DEGREE','2ND_DEGREE_TYPE_1']
pacing = ['ATRIAL_PACING','VENTRICULAR_PACING']

rhythms = {'SINUS RHYTMS':sinusRhythms,'SINUS DYSRHYMTHMIAS':sinusDysrhythmias,'ATRIAL RHYTHMS':atrialRhythms,
          'JUNCTIONAL RHYTHMS':junctionalRhythms,'AV BLOCKAGE':AVblockage,'PACING':pacing}

categories = ['SINUS RHYTMS','SINUS DYSRHYMTHMIAS','ATRIAL RHYTHMS','JUNCTIONAL RHYTHMS','AV BLOCKAGE','PACING']

#Iterates over all the rhythms to create an interface, with buttons for each rhythm and categories.
for category in categories:
    #Creates a label with for each category.
    sinuslabel = Label(root, text=category).pack()
    for type in rhythms[category]: 
        temp = rhythm(type)
        #creates a button for each type of rhythm.
        Button(root, text=temp.name, command=temp.openGif).pack()

#Activates the GUI
root.mainloop()