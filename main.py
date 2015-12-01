import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import handlers

if __name__ == '__main__':
	'''Handling the functionalities'''

	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112.xls")
	college_name = "Samford University"
	college_instance = dataframe[dataframe.INSTNM == college_name]
	#crime_per_student = handlers.all_crimes_per_student_over_years("On Campus", "Crime", college_instance, crimes_obj)
	average_crime_per_student = handlers.average_crimes_per_student("On Campus", "Crime", college_instance, crimes_obj)	

	print average_crime_per_student.keys()
	print average_crime_per_student.values()
