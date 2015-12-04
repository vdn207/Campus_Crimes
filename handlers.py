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

def all_crimes_per_student_over_years(data_source, type_of_data, college_instance, crimes_obj):
	'''Returns the rate of crimes per student for every crime at a given college'''

	college_obj = coll.College(data_source, type_of_data, college_instance, crimes_obj)
	all_crimes_frequencies = college_obj.get_all_crimes_frequencies()
	total_students = college_obj.get_total_students()

	crime_per_student = {}
	for crime in all_crimes_frequencies.keys():	
		try:
			per_student = []
			for freq in all_crimes_frequencies[crime].values[0]:
				per_student.append(freq / total_students)
			crime_per_student[crime] = per_student

		except ZeroDivisionError as z:
			print str(z)

		except ValueError as v:
			print str(v)

	return crime_per_student
