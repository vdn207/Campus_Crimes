

from math import *
import pandas as pd
import numpy as np



def remove_bad_states(input_df):
	mask = input_df['State'].isin(['PR', 'GU', 'PW', 'VI', 'MH', 'AS', 'MP', 'FM'])
	clean_df = input_df[~mask]
	return clean_df

def remove_branches_outside_USA(input_df):
	clean_df = input_df.dropna(subset = ['State'])
	return clean_df

def remove_bad_sector(input_df):
	clean_df = input_df[~(input_df['Sector_desc']=='Administrative Unit Only')]
	return clean_df

def remove_unwanted_columns(input_df):
	clean_df = input_df.drop(["City", "Address", "ZIP", "sector_cd"],axis =1)
	return clean_df


if __name__ == "__main__":
	df = pd.read_excel('data/oncampuscrime101112.xls')
	df = remove_bad_states(df)
	df = remove_branches_outside_USA(df)
	df = remove_bad_sector(df)
	df = remove_unwanted_columns(df)
	df.to_csv("data/oncampuscrime101112_cleaned.csv", sep=',', encoding='utf-8')


