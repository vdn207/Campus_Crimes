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



global result

class Window(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent, background="white")
		self.parent = parent
		self.initUI()
		
   

	def initUI(self):
		self.parent.title("University Crimes")
		self.grid()






def initial_gui():


	global root
	root = Tk()
	result = 0


	#The next 4 lines output a string
	var = StringVar()
	label = Label(root,textvariable = var,relief=RAISED)
	var.set("Interactive GUI")
	label.grid(row=0,columnspan=4,pady = 10)


	#The next 4 lines output a string
	var = StringVar()
	label = Label(root,textvariable = var,relief=RAISED)
	var.set("Click on any one of the following 3 functions to excecute :")
	label.grid(row=2,columnspan=4,pady = 10)


	
	#BUTTON
	button1 = Button(text="See stats of 1 university", command=option1, fg="blue")
	button1.grid(row=3,column=1,pady = 10)

	button2 = Button(text="Compare two universities", command=option2, fg="blue")
	button2.grid(row=4,column=1,pady = 10)

	button2 = Button(text="View stats by Crimes", command=option3, fg="blue")
	button2.grid(row=5,column=1,pady = 10)

	app = Window(root)
	root.mainloop()



def option1():
	'''Sets the value of result to 1 and quits the GUI'''
	global result
	result =1
	root.quit()


def option2():
	'''Sets the value of result to 2 and quits the GUI'''
	global result
	result =2
	root.quit()


def option3():
	'''Sets the value of result to 3 and quits the GUI'''
	global result
	result =3
	root.quit()

def get_result():
	return result

if __name__ == '__main__':
	initial_gui()
	
	