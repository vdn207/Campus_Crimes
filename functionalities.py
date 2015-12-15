'''
Varun D N - vdn207@nyu.edu
'''

'''Contains functions that handle the different functionalities'''

import handlers
import GUI
import plots
import college as coll
import plottingParameters as plotting
import initial_gui as igui
import GUI2
import GUI3
import GUI4
#import plotting1 as plot1

def get_university_crime_details_and_plot(dataframe, college_obj, crimes_obj):
	'''Computes and generates the plots for the university'''

	crime_per_student_without_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj)	# Question 1
	crime_per_student_with_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj, average=True)	# Question 2
	crimes_per_student_by_category = handlers.average_crimes_per_student_by_category(dataframe, 'State', crimes_obj, overall_average = True)

	pltparam = plotting.pltParam()
	answers_obj = plots.Answers(crimes_obj, college_obj, pltparam, crime_per_student_without_average, crime_per_student_with_average, crimes_per_student_by_category)

	multibar_plot = answers_obj.visualize_answer1()
	pie_chart = answers_obj.pieChart(crime_per_student_with_average)	

	return multibar_plot, pie_chart

def university_crime_explorer(dataframe, crimes_obj, university_name, branch_name, GUI_Required):
	'''Gives out the crime details related to a university + branch'''

	if GUI_Required:
		GUI.start_user_interface(dataframe)
		university_name = GUI.get_uni()
		branch_name = GUI.get_branch()
		
	print "Details about %s (%s) is being generated. Please wait..." % (university_name, branch_name)
	
	college_instance = handlers.college_details(dataframe, university_name, branch_name)
	college_obj = coll.College(college_instance, crimes_obj)

	return get_university_crime_details_and_plot(dataframe, college_obj, crimes_obj)

def university_comparer(dataframe, crimes_obj):
	'''Handles the functionalities of University Comparer feature'''

	GUI2.start_user_interface(dataframe)
	university_name_1 = GUI2.get_uni1()
	branch_name_1 = GUI2.get_branch1()
	university_name_2 = GUI2.get_uni2()
	branch_name_2 = GUI2.get_branch2()

	university_crime_explorer(dataframe, crimes_obj, university_name_1, branch_name_1, False)
	university_crime_explorer(dataframe, crimes_obj, university_name_2, branch_name_2, False)

def category_wise_crime(dataframe, crimes_obj):
	'''Handles the functionalities of crimes by different categories'''

	GUI3.start_user_interface(dataframe)
	category, specific_choice = GUI3.get_choices()
	crimes_per_student_by_category = handlers.average_crimes_per_student_by_category(dataframe, category, crimes_obj, overall_average = True)

	pltparam = plotting.pltParam()
	answers_obj = plots.Answers(crimes_obj, None, pltparam, None, None, None)

	answers_obj.simpleBarChart(crimes_per_student_by_category, specific_choice)

def crime_comparisons():
	'''Handles the functionalities of different crime comparisons'''

	GUI4.start_user_interface()
	print GUI4.get_crimes()

def interface(dataframe, crimes_obj):
	'''Run the interace every time for the user'''

	igui.initial_gui()
	user_feature_choice = igui.get_result()

	if user_feature_choice == 1:
		print "Enter"
		multibar_plot, pie_chart = university_crime_explorer(dataframe, crimes_obj, "", "", True)
		print multibar_plot, pie_chart
		#plot1.plotting1("pie.jpg", pie_chart, "blue shit", "guihg")

	elif user_feature_choice == 2:
		university_comparer(dataframe, crimes_obj)

	elif user_feature_choice == 3:
		category_wise_crime(dataframe, crimes_obj)

	else:
		crime_comparisons()

