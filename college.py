'''
Varun D N - vdn207@nyu.edu
'''

'''Contains class definition for a college/university'''

class College:
	'''Class definition'''

	def __init__(self, data_source, type_of_data, college_tuple, crimes_obj):	# college_tuple: A row of data pertaining to the college
		'''Constructor'''

		self.data_source = data_source 		# The source of the data - on-campus, off-campus, etc.
		self.type_of_data = type_of_data 	# The type of data - arrest, crime etc.

		# University details
		self.id = college_tuple["UNITID_P"].values
		self.name = college_tuple["INSTNM"].values
		self.branch = college_tuple["BRANCH"].values
		self.address = college_tuple["Address"].values
		self.city = college_tuple["City"].values
		self.state = college_tuple["State"].values
		self.zip = college_tuple["ZIP"].values
		self.sector = college_tuple["Sector_desc"].values
		self.total_men = college_tuple["men_total"].values
		self.total_women = college_tuple["women_total"].values

		# Crime details pertaining to the university
		#self.crime_frequency_over_years = dict([(crime, college_tuple[[crime + year for year in crimes_obj.get_years_recorded()]]) for crime in crimes_obj.get_crimes_list_short()])
		self.crime_frequency_over_years = {}
		for crime in crimes_obj.get_crimes_list_short():
			self.crime_frequency_over_years[crime] = college_tuple[[crime + year for year in crimes_obj.get_years_recorded()]].values.tolist()[0]

	def get_crime_frequency(self, crime):
		'''Returns the frequency of crime over the years recorded'''

		if crime in crime_frequency_over_years.keys():
			return crime_frequency_over_years[crime]
		else:
			raise cexcep.CrimeNotFoundError("Crime not found in the records")

	def get_all_crimes_frequencies(self):
		'''Returns the dictionary of all crimes and their frequencies'''

		return self.crime_frequency_over_years

	def get_total_students(self):
		'''Returns total students in the college'''

		return (self.total_women + self.total_men)