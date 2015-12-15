
"""
Author: Sean D Rosario

Description :
This script creates a GUI for "University Crimes" project,
for the NYU grad course : DS-GA-1007 Programming for Data Science


References:
ZetCode Tkinter tutorial -Jan Bodnar (www.zetcode.com)
"""



from Tkinter import *
from math import *
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

University_name = ""
branch_name = ""
root = None

class Window(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("University Crimes")
        self.grid()






def gui(dataframe):


    df = dataframe['BASIC']
    global root
    root = Tk()

    def quit():
        root.destroy()
    
    
    #The next 4 lines output a string
    var = StringVar()
    label = Label(root,textvariable = var,relief=RAISED)
    var.set("Interactive GUI")
    label.grid(row=0,columnspan=4)

    #These lines print text
    L1 = Label(root, text="First University name :")
    L1.grid(pady=10,row=1,sticky=W)
    
    #Text box
    user_input1 = Entry(root,bd=3,selectforeground="yellow")
    user_input1.grid(row=1,column=1)

    L2 = Label(root, text="Second University name :")
    L2.grid(pady=10,row=2,sticky=W)
    
    #Text box
    user_input2 = Entry(root,bd=3,selectforeground="yellow")
    user_input2.grid(row=2,column=1)


    def get_branches(uni_name):
        """Returns a list of branches corresponding to a university"""
        mask=df['INSTNM']==uni_name
        subsetted_df = df[mask]
        return subsetted_df['BRANCH'].tolist()

    
    def button_press():
        uni_1 = str(user_input1.get())
        uni_2 = str(user_input2.get())
        """This function for what happens after GO is pressed"""
        if len(uni_1)==0:
            print "No input for university 1"
            pass
        if len(uni_2)==0:
            print "No input for university 2"
            pass

        set_uni1(uni_1)
        set_uni2(uni_2)

        remove_elements()

        L3 = Label(root, text="Pick a branch of {} : ".format(uni_1))
        L3.grid(pady=10,row=1,column=1)

        L4 = Label(root, text="Pick a branch of {} : ".format(uni_2))
        L4.grid(pady=10,row=2,column=1)
        
        #Text box
        choices1 = get_branches(uni_1)
        global var4
        var4 = StringVar(root)
        var4.set('None selected')
        drop1 = OptionMenu(root,var4,*choices1)
        drop1.grid(row=1,column=2)

        choices2 = get_branches(uni_2)
        global var5
        var5 = StringVar(root)
        var5.set('None selected')
        drop2 = OptionMenu(root,var5,*choices2)
        drop2.grid(row=2,column=2)

        #BUTTON
    	button5 = Button(text="SEARCH", command=branch_GO, fg="blue")
    	button5.grid(row=4,column =1,columnspan=2,padx=10)


    
    def branch_GO():
        """This function for what happens after SEARCH is pressed after the branch is chosen"""

        set_branch1(str(var4.get()))
        set_branch2(str(var5.get()))

        quit()

        
    

    def remove_elements():
        L1.grid_remove()
        L2.grid_remove()
        user_input1.grid_remove()
        user_input2.grid_remove()
        button1.grid_remove()


    #BUTTON
    button1 = Button(text="GO", command=button_press, fg="blue")
    button1.grid(row=3,column =1,columnspan=2,padx=10)
    

    

    Quit_button = Button(root, text="Quit", command=quit)
    Quit_button.grid(row=6,column =1)

    app = Window(root)
    root.mainloop()




def set_uni1(Uni_name):
    global University_name1
    University_name1 = Uni_name

def set_branch1(br_name):
    global branch_name1
    branch_name1 = br_name

def get_uni1():
    return University_name1

def get_branch1():
    return branch_name1

def set_uni2(Uni_name):
    global University_name2
    University_name2 = Uni_name

def set_branch2(br_name):
    global branch_name2
    branch_name2 = br_name

def get_uni2():
    return University_name2

def get_branch2():
    return branch_name2

def start_user_interface(dataframe):
    gui(dataframe)
    
    