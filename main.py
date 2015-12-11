import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import handlers
import GUI

if __name__ == '__main__':
	'''Handling the functionalities'''

	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112.xls")
	GUI.start_user_interface(dataframe)
	print "gigioghiowegn"

	'''
	#college_name = "Samford University"
	#college_instance = dataframe[dataframe['BASIC']['INSTNM'] == college_name]
	#crime_per_student = handlers.all_crimes_per_student_over_years(college_instance, crimes_obj, average=True)
	#print crime_per_student
	#average_crime_per_student = handlers.average_crimes_per_student(college_instance, crimes_obj)	
	#print average_crime_per_student
	average_crime_per_student = handlers.average_crimes_per_student_by_category(dataframe, 'Sector_desc', crimes_obj, overall_average = False)
	print average_crime_per_student
	#print average_crime_per_student.keys()
	#print average_crime_per_student.values()
	#print average_crime_per_student['MURD'].index.values
	'''