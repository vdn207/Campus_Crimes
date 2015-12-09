'''
Varun D N - vdn207@nyu.edu
'''

'''Contains functions which handle different fuctionalities of the system'''

import crimes
import college as coll
import pandas as pd 
import numpy as np

def data_initialization(path):
	'''Initializes the initial data requirements of the system'''

	try:
		data_frame = pd.read_excel(path)

	except IOError as IOE:
		print str(IOE)

	# Crime types and their specifics
	crimes_list = ['MURD', 'NEG_M', 'FORCIB', 'NONFOR', 'ROBBE', 'AGG_A', 'BURGLA', 'VEHIC', 'ARSON']
	years = ['10', '11', '12']
	crime_full_names = {"MURD":"Murder", "NEG_M":"Negligent Manslaughter", "FORCIB":"Forcible Sex Offense", "NONFOR":"Non Forcible Sex Offense", "ROBBE":"Robbery", "AGG_A":"Aggravated Assault", "BURGLA":"Burglary", "VEHIC":"Motor Vehicle Theft", "ARSON":"Arson"}

	crimes_obj = crimes.Crimes(crimes_list, years, crime_full_names)

	return data_frame, crimes_obj

# Question 1
def all_crimes_per_student_over_years(data_source, type_of_data, college_instance, crimes_obj, per_student = True):
	'''Returns the rate of crimes per student for every crime at a given college'''

	college_obj = coll.College(data_source, type_of_data, college_instance, crimes_obj)
	all_crimes_frequencies = college_obj.get_all_crimes_frequencies()
	
	if not per_student:
		return all_crimes_frequencies

	total_students = college_obj.get_total_students()[0] 	# Because, the function is returning a list. Eg: [4567.]

	crime_per_student = {}
	for crime in all_crimes_frequencies.keys():	
		try:
			per_student = []
			for freq in all_crimes_frequencies[crime]:
				per_student.append(freq / total_students)
			crime_per_student[crime] = per_student

		except ZeroDivisionError as z:
			print str(z)

		except ValueError as v:
			print str(v)

	return crime_per_student, crimes_obj

# Question 2
def average_crimes_per_student(data_source, type_of_data, college_instance, crimes_obj):	
	'''Returns the average crimes per student committed over the years recorded'''

	college_obj = coll.College(data_source, type_of_data, college_instance, crimes_obj)
	all_crimes_frequencies = college_obj.get_all_crimes_frequencies()
	total_students = college_obj.get_total_students()[0] 	# Because, the function is returning a list. Eg: [4567.]

	average_crime_per_student = {}
	for crime in all_crimes_frequencies.keys():	
		try:
			total_crimes = 0
			for freq in all_crimes_frequencies[crime]:
				total_crimes += freq
			average_crime_per_student[crime] = total_crimes / total_students

		except ZeroDivisionError as z:
			print str(z)

		except ValueError as v:
			print str(v)

	return average_crime_per_student, crimes_obj

# Question 3
def average_crimes_per_student_by_category(dataframe, category, crimes_obj, overall_average = False):
	'''Returns the rate of crimes per student for every crime for a given category - where category can be thought
	   as ZIP Codes, State, College Sector

	   The output is a dictionary with key = crime and value is a series where indices are the different categories
	   and the values are rate of 'crime' per student in that sector

	   overall_average - set to True if you need the average over the years.)

	'''

	crimes_by_category_dict = {}
	for crime in crimes_obj.get_crimes_list_short():
		crime_by_category_list = []
		for year in crimes_obj.get_years_recorded():
			crime_by_category_list.append(dataframe.groupby(by=[category])[crime + year].sum() / dataframe.groupby(by=[category])['Total'].sum())

		if overall_average:
			crimes_by_category_dict[crime] = sum(crime_by_category_list)
		else:
			crimes_by_category_dict[crime] = crime_by_category_list

	return crimes_by_category_dict, crimes_obj

