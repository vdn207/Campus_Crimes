__author__ = 'Sean D Rosario'


#!/usr/bin/python
# -*- coding: utf-8 -*-

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
#import Image, ImageTk
import matplotlib.pyplot as plt



class Window(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("University Crimes")
        self.grid()






def gui():

    root = Tk()

    def quit():
        root.quit()
    
    
    #The next 4 lines output a string
    var = StringVar()
    label = Label(root,textvariable = var,relief=RAISED)
    var.set("Interactive GUI")
    label.grid(row=0,columnspan=4)

    #These lines print text
    L1 = Label(root, text="University name :")
    L1.grid(pady=10,row=1,sticky=W)
    
    #Text box
    user_input = Entry(root,bd=3,selectforeground="yellow")
    user_input.grid(row=1,column=1)


    
    def button_press(str_parameter):
        """This function for what happens after GO is pressed"""
        if len(str_parameter)==0:
            print "No input"
        else:

            L2 = Label(root, text="Pick a branch:")
            L2.grid(pady=10,row=3,sticky=W)
            
            #Text box
            choices = get_branches(str_parameter)
            var3 = StringVar(root)
            var3.set('None selected')
            drop = OptionMenu(root,var3,*choices)
            drop.grid(row=3,column=1)

            button5 = Button(text="GO", command=branch_GO, fg="blue")
            button5.grid(row=3,column =2,padx=10)


    
    def branch_GO():
        """This function for what happens after GO is pressed after the branch is chosen"""
        branch_name = str(var3.get())
        print branch_name
    
    
    def text_GO():
        """This function is for the GO button for Text box input"""
        button_press(str(user_input.get()))
        University_name = (str(user_input.get()))
        print University_name
        button3.grid_remove()
        button4.grid_remove()
        drop_filter_by_type.grid_remove()
        drop_filter_by_state.grid_remove()
        

    
    #BUTTON
    button1 = Button(text="GO", command=text_GO, fg="blue")
    button1.grid(row=1,column =2,padx=10)

    #The next 4 lines output a string
    var = StringVar()
    label = Label(root,textvariable = var)#relief=RAISED
    var.set("OR pick from drop down : ")
    label.grid(row=2,column=0)

    #DROPDOWN
    def drop_down(choices = np.sort(df['INSTNM'].unique())):

        global var1
        var1 = StringVar(root)
        var1.set('None selected')
        drop = OptionMenu(root,var1,*choices)
        drop.grid(row=2,column=1)

    
    
    def drop_down_GO():
        """This function is for the GO button for dropdown"""
        button_press(str(var1.get()))
        button3.grid_remove()
        button4.grid_remove()
        drop_filter_by_type.grid_remove()
        drop_filter_by_state.grid_remove()

    drop_down()
    

    #
    #The following code is for the filter by state option
    #

    choices2 = np.sort(df['State'].unique())
    var2 = StringVar(root)
    var2.set('State')
    drop_filter_by_state = OptionMenu(root,var2,*choices2)
    drop_filter_by_state.grid(row=3,column=1)

    def filter_by_state():
        mask = filtered_df['State']==str(var2.get())
        filtered_list = np.sort(filtered_df[mask]['INSTNM'].unique())
        drop_down(choices=filtered_list)
        #filtered_df = filtered_df[mask]

    button3 = Button(text="Filter by state", command=filter_by_state, fg="blue")
    button3.grid(row=3,column =2,padx=0)

    
    #
    #The following code is for the filter by university-type option
    #

    choices3 = np.sort(df['Sector_desc'].unique())
    var3 = StringVar(root)
    var3.set('type')
    drop_filter_by_type = OptionMenu(root,var3,*choices3)
    drop_filter_by_type.grid(row=4,column=1)

    def filter_by_type():
        mask = filtered_df['Sector_desc']==str(var3.get())
        filtered_list = np.sort(filtered_df[mask]['INSTNM'].unique())
        drop_down(choices=filtered_list)
        #filtered_df = filtered_df[mask]

    button4 = Button(text="Filter by type", command=filter_by_type, fg="blue")
    button4.grid(row=4,column =2,padx=10)



    #BUTTON
    button2 = Button(text="GO", command=drop_down_GO, fg="blue")
    button2.grid(row=2,column=2)
    
    
    Quit_button(root, text="Quit", command=quit).grid(row=6,column =1)

    app = Window(root)
    root.mainloop()







def get_branches(uni_name):
    """Returns a list of branches corresponding to a university"""
    mask=df['INSTNM']==uni_name
    subsetted_df = df[mask]
    return subsetted_df['BRANCH'].tolist()






def read_data():
    """Reads the data into global variable df and makes it publicly accessible"""
    global df
    df = pd.read_excel('oncampuscrime101112.xls') 
   


def main():
    try:
        read_data()
    except:
        print "Error in reading the data"
    try:
        gui()
    except:
        print "Error in GUI"




    

if __name__ == '__main__':
    read_data()
    gui()