__author__ = 'SeansMBP'


#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Sean D Rosario

Description :
This script creates a GUI for "University Crimes" project,
for the NYU grad course : DS-GA-1007 Programming for Data Science


References:
ZetCode Tkinter tutorial
Author: Jan Bodnar (www.zetcode.com)
"""



from Tkinter import *
from math import *
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt



global output

class Window(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.initUI()
        
        """
        self.image = Image.open("./blurry-can-have-wall-please-wallpaper.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    
    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
        """

    def initUI(self):

        self.parent.title("University Crimes")
        self.grid()






def initial_gui():

    root = Tk() 


    #The next 4 lines output a string
    var = StringVar()
    label = Label(root,textvariable = var,relief=RAISED)
    var.set("Interactive GUI")
    label.grid(row=0,columnspan=4,pady = 10)


    #The next 4 lines output a string
    var = StringVar()
    label = Label(root,textvariable = var,relief=RAISED)
    var.set("Choose a function to excecute :")
    label.grid(row=2,columnspan=4,pady = 10)

    #BUTTON
    button1 = Button(text="See stats of 1 university", command=option1, fg="blue")
    button1.grid(row=3,column=1)

    button2 = Button(text="Compare two universities", command=option2, fg="green")
    button2.grid(row=4,column=1)

    button2 = Button(text="View stats by Crimes", command=option2, fg="green")
    button2.grid(row=5,column=1)





    #im = Image.open("the_plot.jpg")
    #img = ImageTk.PhotoImage(Image.open("the_plot.jpg"))
    #label = Label(root, image = img)
    #label.image = img # keep a reference!
    #label.grid(row=5,column=1) 
    #label.grid()

    app = Window(root)
    root.mainloop()


def option1():
	result =1
def option2():
	result =2
def option3():
	result =3





    

if __name__ == '__main__':
    
    initial_gui()
    print result