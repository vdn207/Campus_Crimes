'''
Varun D N - vdn207@nyu.edu
'''

'''The main program orchestrating the different components of the project'''

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import handlers
import GUI
import plots
import college as coll
import plottingParameters as plotting

if __name__ == '__main__':
	'''The main program running the software'''

<<<<<<< HEAD
	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112_cleaned.csv")
=======
	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112.xls")

>>>>>>> upstream/master
	GUI.start_user_interface(dataframe)
	university_name = GUI.get_uni()
	branch_name = GUI.get_branch()

	print "Details about %s (%s) is being generated. Please wait..." % (university_name, branch_name)

	college_instance = dataframe[(dataframe['BASIC']['INSTNM'] == university_name) & (dataframe['BASIC']['BRANCH'] == branch_name)]
	college_obj = coll.College(college_instance, crimes_obj)

	crime_per_student_without_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj)	# Question 1
	crime_per_student_with_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj, average=True)	# Question 2
	crimes_per_student_by_category = handlers.average_crimes_per_student_by_category(dataframe, 'State', crimes_obj)	# Question 3
	
	pltparam = plotting.pltParam()
	answers_obj = plots.Answers(crimes_obj, college_obj, pltparam, crime_per_student_without_average, crime_per_student_with_average, crime_per_student_with_average)

	answers_obj.visualize_answer1()
	answers_obj.pieChart(crime_per_student_with_average)
