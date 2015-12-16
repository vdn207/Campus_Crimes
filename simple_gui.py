
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


class Window(Frame):
    """This class defines the frame of the gui and sets the title of the window"""

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("University Crimes")
        self.grid()






def gui(dataframe):


    df = dataframe#['BASIC']

    root = Tk()

    def quit():
        root.destroy()
    
    
    #The next 4 lines output a string
    var = StringVar()
    label = Label(root,textvariable = var,relief=RAISED)
    var.set("Interactive GUI")
    label.grid(row=0,columnspan=4)

    #These lines print text
    L1 = Label(root, text="Enter a University :")
    L1.grid(pady=10,row=1,sticky=W)
    
    #Text box
    user_input1 = Entry(root,bd=3,selectforeground="yellow")
    user_input1.grid(row=1,column=1)

  


    def get_branches(uni_name):
        """Returns a list of branches corresponding to a university"""
        mask=df['INSTNM']==uni_name
        subsetted_df = df[mask]
        return subsetted_df['BRANCH'].tolist()

    
    def button_press():
        uni_1 = str(user_input1.get())
        
        """This function for what happens after GO is pressed"""
        if len(uni_1)==0:
            print "No input for university 1"
            pass

        set_uni(uni_1)

        remove_elements()

        L3 = Label(root, text="Pick a branch of {} : ".format(uni_1))
        L3.grid(pady=10,row=1,column=1)

        
        #Text box
        choices1 = get_branches(uni_1)
        global var4
        var4 = StringVar(root)
        var4.set('None selected')
        drop1 = OptionMenu(root,var4,*choices1)
        drop1.grid(row=1,column=2)


        #BUTTON
    	button5 = Button(text="SEARCH", command=branch_GO, fg="blue")
    	button5.grid(row=4,column =1,columnspan=2,padx=10)


    
    def branch_GO():
        """This function for what happens after SEARCH is pressed after the branch is chosen"""

        set_branch(str(var4.get()))

        quit()

        
    

    def remove_elements():
        L1.grid_remove()
        user_input1.grid_remove()
        button1.grid_remove()


    #BUTTON
    button1 = Button(text="GO", command=button_press,width=10,fg="blue")
    button1.grid(row=3,column =1,columnspan=2,padx=10)
    

    

    Quit_button = Button(root, text="Quit", command=quit,width=10)
    Quit_button.grid(row=6,column =1, pady=20)

    app = Window(root)
    root.mainloop()




def set_uni(Uni_name):
    global University_name
    University_name = Uni_name

def set_branch(br_name):
    global branch_name
    branch_name = br_name

def get_uni():
    return University_name

def get_branch():
    return branch_name




def start_user_interface(dataframe):
    gui(dataframe),
    

if __name__ == '__main__':
    start_user_interface(pd.read_csv("data/oncampuscrime101112.csv"))
    print get_uni()
    #print get_uni2(,)
    print get_branch()
    #print get_branch2()
    