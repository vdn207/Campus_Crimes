
"""
Author: Sean D Rosario

Description :
This is the GUI that launches if the User clicks on the first button of the initial GUI
"""



from Tkinter import *
from math import *
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

University_name = ""
branch_name = ""

Error_message=None

class Window(Frame):
    """This class defines the frame of the gui and sets the title of the window"""

    def __init__(self, parent):
        """This function makes the size of the window flexible
        so that it dynamically readjusts itself to accomodate
         all the widgets and GUI elements"""
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Interactive GUI") #Sets the title
        self.grid()






def gui(dataframe):


    df = dataframe#['BASIC']

    root = Tk()

    def quit():
        """Quits the GUI"""
        root.destroy()
    
    
    #The next 4 lines output a string
    Title = Label(root, text="Exploring crimes of a single university",fg="black").grid(row=0,column=0, columnspan=10,pady=10)

    #Text widget
    Text_widget = Label(root, text="Enter a University :")
    Text_widget.grid(pady=10,row=1,sticky=W)
    
    #Text box
    user_input = Entry(root,bd=3,selectforeground="yellow")
    user_input.grid(row=1,column=1)

  


    def get_branches(uni_name):
        """Returns a list of branches corresponding to a university"""
        mask=df['INSTNM']==uni_name
        subsetted_df = df[mask]
        return subsetted_df['BRANCH'].tolist()

    
    def button_press():
        

        uni_1 = str(user_input.get())
        
        """This function for what happens after GO is pressed"""
        if len(uni_1)==0:
            global Error_message
            Error_message = Label(root, text="No input detected!",fg="red").grid(row=1,column=5)
            return None
        if not(uni_1 in df['INSTNM'].values):
            global Error_message
            Error_message = Label(root, text="University not found!",fg="red").grid(row=1,column=5)
            return None

        set_uni(uni_1)

        remove_elements()

        branch_prompt = Label(root, text="Pick a branch of {} : ".format(uni_1))
        branch_prompt.grid(pady=10,row=1,column=1)

        
        #Text box
        list_of_corresponding_branches = get_branches(uni_1)
        global branch_input
        branch_input = StringVar(root)
        branch_input.set('None selected')
        drop1 = OptionMenu(root,branch_input,*list_of_corresponding_branches)
        drop1.grid(row=1,column=2)


        #BUTTON
    	button5 = Button(text="SEARCH", command=branch_GO, fg="blue",width=10)
    	button5.grid(row=4,column =1,columnspan=10,padx=10)


    
    def branch_GO():
        """This function for what happens after SEARCH is pressed after the branch is chosen"""

        set_branch(str(branch_input.get()))

        quit()

        
    

    def remove_elements():
        Text_widget.grid_remove()
        user_input.grid_remove()
        GO_button.grid_remove()
        if not(Error_message==None):
            Error_message.grid_remove()


    #BUTTON
    GO_button = Button(text="GO", command=button_press,width=10,fg="blue")
    GO_button.grid(row=3,column =1,columnspan=2,padx=10)
    

    

    Quit_button = Button(root, text="Quit", command=quit,width=10)
    Quit_button.grid(row=6,column =1, pady=20,columnspan=10)

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
    