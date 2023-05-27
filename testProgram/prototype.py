from tkinter import *
import os
import socket
import time

root = Tk()  # create parent window
root.title("Q-ECGS")


# use Button and Label widgets to create a simple TV remote
def normalsinus():
    '''callback method used for turn_on button'''
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"normal.gif")
   

# use Button and Label widgets to create a simple TV remote
def bradycardia():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"bradycardia.gif")


def tachycadia():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"tachycadia.gif")

    
sinuslabel = Label(root, text="SINUS RHYTHMS")
sinuslabel.pack()

normalsinus_b = Button(root, text="NORMAL SINUS", command=normalsinus)
normalsinus_b.pack()

tachycadia_b = Button(root, text="TACHYCARDIA", command=tachycadia)
tachycadia_b.pack()

bradycardia_b = Button(root, text="BRADYCARDIA", command=bradycardia)
bradycardia_b.pack()

def elevation():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"2_ST_segment_elevation.gif")


def depression():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"2_ST_segment_depression.gif")


sinuslabel = Label(root, text=" ")
sinuslabel.pack()

sinuslabel = Label(root, text="SINUS DYSRHYTHMIAS")
sinuslabel.pack()

elevation_b = Button(root, text="SEGMENT ELEVATION", command=elevation)
elevation_b.pack()

depression_b = Button(root, text="SEGMENT DEPRESSION", command=depression)
depression_b.pack()

def flutter():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"3_atrial_flutter.gif")


def atachycardia():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"3_atrial_tachycardia.gif")

sinuslabel = Label(root, text=" ")
sinuslabel.pack()

sinuslabel = Label(root, text="ATRIAL RHYTHMS")
sinuslabel.pack()

elevation_b = Button(root, text="ATRIAL FLUTTER", command=flutter)
elevation_b.pack()

depression_b = Button(root, text="ATRIAL TACHYCARDIA", command=atachycardia)
depression_b.pack()

def junctional():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"4_junctional_rhythm.gif")

def junctionalt():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"4_junctional_tachycardia.gif")


sinuslabel = Label(root, text=" ")
sinuslabel.pack()

sinuslabel = Label(root, text="JUNCTIONAL RHYTHMS")
sinuslabel.pack()

elevation_b = Button(root, text="JUNCTIONAL RHYTHM", command=junctional)
elevation_b.pack()

elevation_b = Button(root, text="JUNCTIONAL TACHYCARDIA", command=junctionalt)
elevation_b.pack()

def first():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"5_1st_degree.gif")

def second():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"5_2nd_degree_type1.gif")

sinuslabel = Label(root, text=" ")
sinuslabel.pack()

sinuslabel = Label(root, text="AV BLOCKAGE")
sinuslabel.pack()

elevation_b = Button(root, text="1ST DEGREE", command=first)
elevation_b.pack()

elevation_b = Button(root, text="2ND DEGREE TYPE 1", command=second)
elevation_b.pack()

def atr():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"6_atrial_pacing.gif")

def vent():
    os.system("taskkill /IM Microsoft.Photos.exe /F")
    os.system("start "+"6_ventricular_pacing.gif")

sinuslabel = Label(root, text=" ")
sinuslabel.pack()

sinuslabel = Label(root, text="PACING")
sinuslabel.pack()

elevation_b = Button(root, text="ATRIAL PACING", command=atr)
elevation_b.pack()

elevation_b = Button(root, text="VENTRICULAR PACING", command=vent)
elevation_b.pack()




root.mainloop()