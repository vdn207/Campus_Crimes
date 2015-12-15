'''
author: Michael Higgins

'''
import handlers
import plots
import college as coll
import numpy as np
import pandas as pd
import colorsys
from collections import OrderedDict
from scipy.interpolate import interp1d
import mikeCustomException as cexcep


class pltParam:
	'''
	Includes several helper functions to generate graphs

	'''
	
	def __init__(self):
		self.width = .3
		self.fontsize = 15
		self.padding =.1

	
	#http://stackoverflow.com/questions/470690/how-to-automatically-generate-n-distinct-colors
	def getColors(self,num_colors):
		'''
		input is an integer, output is a list of distinct colors in rgb format.
		
		'''
		if not isinstance(num_colors,int):
			raise cexcep.WrongFormat("Input must be a integer")
		
		colors=[]
		try:
			for i in np.arange(0., 360., 360. / num_colors):   #possible problem when num_colors =0 
				hue = i/360.
				lightness = (50 + np.random.rand() * 10)/100.
				saturation = (90 + np.random.rand() * 10)/100.
				colors.append(colorsys.hls_to_rgb(hue, lightness, saturation))
			return colors
		
		except ZeroDivisionError :
			print "We don't have any crime record on this college on this campus."
			return None

	def alternatingDictionary(self, unSortedDic):
		'''
		Input is dictionary or panda series. This is for plotting data on a pie Chart.  We want the values 			of big and small items to alternate so there is no labeling overlap issues. 
		returns list of keys that represent alternating order of values.
		'''
		if type(unSortedDic) != dict:  
			if not isinstance(unSortedDic , pd.core.series.Series ):  #if its not a series throw error
				raise cexcep.WrongFormat("Input must be a dictionary")
			unSortedDic = unSortedDic.to_dict()  # if its series can convert to dictionary
		
		sortedDic = OrderedDict(sorted(unSortedDic.items(), key=lambda t: t[1]))
		keys = sortedDic.keys()
		numKeys= len(keys)
		firstHalf= keys[:int(.5*numKeys)]
		secondHalf= keys[int(.5*numKeys):]
		secondHalf=secondHalf[::-1]  #reverse order of second list
		
		target = []
		for i in range(len(firstHalf)):  #put back together 
			target= target + [firstHalf[i]] + [secondHalf[i]]
		
		if numKeys%2==1:  #if there is an odd number of keys then must add last element
			target+= [secondHalf[-1]] 

		return target
	

	def getTickFontSize(self,numTicks):
		'''
		input: int, output float
		helper function for picking appropriate font size for graphs with ticks 
		'''
		if not isinstance(numTicks , int):  #if its not a series throw error
			raise cexcep.WrongFormat("Input must be an int")
			return None

		if numTicks <15:
			return 15

		maxFont = 15
		minFont = 4
		fontSizeFunction = interp1d([14,75],[maxFont,minFont])  #maps linearly range in [14,75] to [15,4]
		fontsize= float( fontSizeFunction(numTicks) )
		return fontsize

	
	def subsetDictionary(self, data , category):
		'''
		input is dictionary with crimes as keys, Series as values.  Need to extract the
		index that is category.
		returns Series
		'''
		output= pd.Series()
	
		for key in data.keys():
			output = output.set_value(key, (data[key])[category] )
		return output
		

			

if __name__ == '__main__':
	p = pltParam()

	university_name= "Harvard University"

	branch_name = "Main Campus"
	dataframe, crimes_obj = handlers.data_initialization("data/oncampuscrime101112_cleaned.csv")
	college_instance = handlers.college_details(dataframe, university_name, branch_name)
	college_obj = coll.College(college_instance, crimes_obj)
	crime_per_student_without_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj) # Question 1
	crime_per_student_with_average = handlers.all_crimes_per_student_over_years(college_obj, crimes_obj, average=True) # Question 2
	crimes_per_student_by_category = handlers.average_crimes_per_student_by_category(dataframe, 'State', crimes_obj) # Question 3
	pltparam = plotting.pltParam()
	answers_obj = plots.Answers(crimes_obj, college_obj, pltparam, crime_per_student_without_average, crime_per_student_with_average, crimes_per_student_by_category)


	d = handlers.average_crimes_per_student_by_category(dataframe, 'State' ,crimes_obj, overall_average = True)
	
	

	answers_obj.simpleBarChart(d,"MA")


