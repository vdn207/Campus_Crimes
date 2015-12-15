'''
Varun D N - vdn207@nyu.edu
'''

'''The main program orchestrating the different components of the project'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import functionalities as func
import handlers

if __name__ == '__main__':
	'''The main program running the software'''

	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112_cleaned.csv")

	func.interface(dataframe, crimes_obj)

	'''
	while True:
		interface(dataframe)
		try:
			user_request = raw_input("Press 1 to go explore again or else type 'quit' to exit from the program: ")

			if user_request == 'quit':
				exit()
			if user_request == '1':
				continue

		except KeyboardInterrupt:
			continue 

	'''	