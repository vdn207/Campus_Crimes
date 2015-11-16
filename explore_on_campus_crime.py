import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

if __name__ == '__main__':
	on_campus_crime = pd.read_excel("data/oncampuscrime101112.xls")
	print on_campus_crime.shape