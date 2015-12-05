import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import handlers

if __name__ == '__main__':
	'''Handling the functionalities'''

	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112.csv")
	college_name = "University of Alabama in Huntsville"
	college_instance = dataframe[dataframe.INSTNM == college_name]
	crime_per_student = handlers.all_crimes_per_student_over_years("On Campus", "Crime", college_instance, crimes_obj)

	for crime in crime_per_student.keys():
		print crime
		print crime_per_student[crime]
		print ""

print dataframe['INSTNM'][:10]
#print crime_per_student

	
