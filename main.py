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
import initial_gui as igui
import GUI2
import GUI3
import GUI4

def university_crime_explorer(dataframe):
	'''Handles the features of first GUI'''

	GUI.start_user_interface(dataframe)
	university_name = GUI.get_uni()
	branch_name = GUI.get_branch()

	print "Details about %s (%s) is being generated. Please wait..." % (university_name, branch_name)
	'''
	college_instance = handlers.college_details(dataframe, university_name, branch_name)
	college_obj = coll.College(college_instance, crimes_obj)

	crime_per_student_without_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj)	# Question 1
	crime_per_student_with_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj, average=True)	# Question 2
	crimes_per_student_by_category = handlers.average_crimes_per_student_by_category(dataframe, 'State', crimes_obj)	# Question 3
	
	pltparam = plotting.pltParam()
	answers_obj = plots.Answers(crimes_obj, college_obj, pltparam, crime_per_student_without_average, crime_per_student_with_average, crimes_per_student_by_category)

	#answers_obj.visualize_answer1()
	answers_obj.pieChart(crime_per_student_with_average)	
	'''

def university_comparer(dataframe):
	'''Handles the functionalities of University Comparer feature'''

	GUI2.start_user_interface(dataframe)
	university_name_1 = GUI2.get_uni1()
	branch_name_1 = GUI2.get_branch1()
	university_name_2 = GUI2.get_uni2()
	branch_name_2 = GUI2.get_branch2()

	print university_name_1, university_name_2
	print branch_name_1, branch_name_2

def category_wise_crime(dataframe):
	'''Handles the functionalities of crimes by different categories'''

	GUI3.start_user_interface(dataframe)
	print GUI3.get_choices()

def crime_comparisons():
	'''Handles the functionalities of different crime comparisons'''

	GUI4.start_user_interface()
	print GUI4.get_crimes()

if __name__ == '__main__':
	'''The main program running the software'''

	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112_cleaned.csv")

	while True:
		igui.initial_gui()
		user_feature_choice = igui.get_result()

		if user_feature_choice == 1:
			print "Enter"
			university_crime_explorer(dataframe)

		elif user_feature_choice == 2:
			university_comparer(dataframe)

		elif user_feature_choice == 3:
			category_wise_crime(dataframe)

		else:
			crime_comparisons()
