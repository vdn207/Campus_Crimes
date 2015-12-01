__author__ = 'SeansMBP'


#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Sean D Rosario

Description :
This script creates a GUI for "University Crimes" project,
for the NYU grad course : DS-GA-1007 Programming for Data Science


Reference:
ZetCode Tkinter tutorial
Author: Jan Bodnar (www.zetcode.com)
"""

from Tkinter import *
from math import *
import pandas as pd
import numpy as np


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
    #root.geometry("250x150+300+300") #Dimensions of the GUI box

    #The next 4 lines output a string
    var = StringVar()
    label = Label(root,textvariable = var,relief=RAISED)
    var.set("Beta version 69")
    label.grid(row=0)

    #These lines print text
    L1 = Label(root, text="University name :")
    L1.grid(pady=10,row=1,sticky=W)
    
    #Text box
    user_input = Entry(root,bd=3,selectforeground="yellow")
    user_input.grid(row=1,column=1)

    """This function for what happens after GO is pressed"""
    def button_press(str_parameter):
        if len(str_parameter)==0:
            print "No input"
        else:

            L2 = Label(root, text="Pick a branch:")
            L2.grid(pady=10,row=3,sticky=W)
            
            #Text box
            choices = get_branches(str_parameter)
            var1 = StringVar(root)
            var1.set('None selected')
            drop = OptionMenu(root,var1,*choices)
            drop.grid(row=3,column=1)

    
    """This function is for the GO button for Text box input"""
    def text_GO():
        button_press(str(user_input.get()))
        

    
    #BUTTON
    button = Button(text="GO", command=text_GO, fg="blue")
    button.grid(row=1,column =2,padx=10)

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

    
    """This function is for the GO button for dropdown"""
    def drop_down_GO():
        button_press(str(var1.get()))

    drop_down()
    
    choices2 = np.sort(df['State'].unique())
    var2 = StringVar(root)
    var2.set('State')
    drop = OptionMenu(root,var2,*choices2)
    drop.grid(row=3,column=1)

    def filter_by_state():
        mask = df['State']==str(var2.get())
        filtered_list = np.sort(df['INSTNM'][mask].unique())
        drop_down(choices=filtered_list)

    button = Button(text="Filter by state", command=filter_by_state, fg="blue")
    button.grid(row=3,column =2,padx=10)


    #BUTTON
    button = Button(text="GO", command=drop_down_GO, fg="blue")
    button.grid(row=2,column=2)

    app = Window(root)
    root.mainloop()




    

    
def get_branches(uni_name):
    mask=df['INSTNM']==uni_name
    subsetted_df = df[mask]
    return subsetted_df['BRANCH'].tolist()

    
   


def main():
    try:
        gui()
    except:
        print "Error in GUI"


def read_data():
    global df
    df = pd.read_excel('oncampuscrime101112.xls')
    #print df['INSTNM']
    #print "data_input ran!!!!! OMGGGGG"

if __name__ == '__main__':
    #gui()
    read_data()
    gui()
