__author__ = 'SeansMBP'


from Tkinter import *
from math import *
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt



class Window(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent

        self.initUI()
        

    def initUI(self):

        self.parent.title("University Crimes")
        self.pack()






def plotting1(path1,path2):

    root = Tk() 
    
    def quit():
        root.quit()



    img = ImageTk.PhotoImage(Image.open(path1))
    label = Label(root, image = img)
    label.image = img # keep a reference!
    label.pack(side = LEFT) 

    img2 = ImageTk.PhotoImage(Image.open(path1))
    label2 = Label(root, image = img)
    label2.image = img # keep a reference!
<<<<<<< HEAD
    label2.grid(side = RIGHT) 
=======
    label2.pack(side = RIGHT) 
>>>>>>> upstream/master

    Button(root, text="BACK TO MAIN", command=quit).pack(side = BOTTOM)



    app = Window(root)
    root.mainloop()


if __name__ == '__main__':
<<<<<<< HEAD
    plotting1
=======
    plotting1("histoByState.jpg","histoByState2.jpg")
	
>>>>>>> upstream/master
