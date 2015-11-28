import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure, show
import matplotlib.patches as mpatches

on_campus_crime = pd.read_csv("/home/ds-ga-1007/Desktop/workspace/CrimeProject/Campus_Crimes/data/oncampuscrime101112.csv")

colleges= on_campus_crime['INSTNM']
print list(on_campus_crime.columns.values)
college_name = "Harvard University" # User Input in the final software

crimes_list = ['MURD', 'NEG_M', 'FORCIB', 'NONFOR', 'ROBBE', 'AGG_A', 'BURGLA', 'VEHIC', 'ARSON']
years = ['10', '11', '12']

total_crime_facts = [ crime + year for crime in crimes_list for year in years]


college_specific = on_campus_crime[on_campus_crime.INSTNM == college_name]
number_of_students = college_specific.Total.values[0]
crime_freq_over_time = {}

crime_freq_reduced_by_university = {}

#print on_campus_crime

for crime in crimes_list:
    crime_freq_over_time[crime] = college_specific[[crime + year for year in years]]
    #per 10,000 students
    crime_freq_over_time[crime] = crime_freq_over_time[crime] / number_of_students *10000  




ax = plt.subplot(111)
w = 0.3
y_10 = []
y_11 = []
y_12 = []
padding =.1

fontsize=15

crimeNames= ["Forcible Rape", "Arson", "Manslaughter", "Murder", "NonForcible Rape", "Vehicle Theft","Burglary", "Aggravated Assault" ,"Robbery"]

for crime in crimes_list:
    freq_list = crime_freq_over_time[crime].values.tolist()
    y_10.append(freq_list[0][0])
    y_11.append(freq_list[0][1])
    y_12.append(freq_list[0][2])

print "freq_list  ", crimes_list


x = np.array(range(1, len(crimes_list) + 1))
#bar for each year
rect1 = ax.bar( x - w, y_10, width = w, color='r', align='center')
rect2 = ax.bar(x, y_11, width = w, color='g', align='center')
rect3 = ax.bar(x + w, y_12, width = w, color='b', align='center')

plt.xticks([ a + w/2 for a in  x],[name for name in crimeNames], rotation= 30, ha='right')


ax.set_xlabel('Particular Crime by Year ', fontsize=fontsize)
ax.set_ylabel('Crime Rate (per 10,000 students)', fontsize=fontsize)

ax.set_title(college_name + " Crime By Year ", fontsize=fontsize)
ax.autoscale(tight=True)

#add padding
plt.subplots_adjust(left=0.15,top=0.85)
#legends
r_patch = mpatches.Patch(color='red', label='2010')
g_patch = mpatches.Patch(color='g', label='2011')
b_patch = mpatches.Patch(color='b', label='2012')
ax.legend([r_patch,g_patch,b_patch],['2010','2011','2012'])

#adjust limits of yaxis to make room for annointed text
maxData=max(y_10+y_11+y_12)
plt.ylim(0,maxData * 1.15)




def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.1f' % height,
                ha='center', va='bottom')

autolabel(rect1)
autolabel(rect2)
autolabel(rect3)



plt.tight_layout()
plt.show()

