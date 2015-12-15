import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import handlers
import college

if __name__ == '__main__':
	'''Handling the functionalities'''
	
	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112_cleaned.csv")
	coll =college.College(pd.Series({"a":3},crimes_obj))
	university_name = "University of Alabama in Huntsville"
	branch_name = "Main_Campus"
	college_instance = handlers.college_details(dataframe, university_name, branch_name)
	college_obj = coll.College(college_instance, crimes_obj)
	crime_per_student = handlers.all_crimes_per_student_over_years("On Campus", "Crime", college_instance, crimes_obj)

	
	answers_obj = plots.Answers(crimes_obj, college_obj, pltparam, crime_per_student_without_average, crime_per_student_with_average, crimes_per_student_by_category)

	d = handlers.average_crimes_per_student_by_category(dataframe, 'State' ,crimes_obj, overall_average = True)
	
	
	answers_obj.simpleBarChart(d,"MA")
	
	
