# USA GDP (Github / JSON): http://api.worldbank.org/v2/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json
# years range from 1960 to 2021 in data set, total number of years is 61

import json 
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import pyplot as plt

paths = ['usagdp.json']
usagdp = []
for path in paths: 
    with open(path, encoding = 'ascii') as i: 
        text = i.read()
        usagdp += json.loads(text)
gdp = usagdp[1]

yrs = []
for years in gdp: 
    yr = years['date']
    yrs.append(yr)
yrs.sort()
yrsrange = [] 
for yr in yrs: 
    yrrange = int(yr)
    yrsrange.append(yrrange)

gdpvalueforusa = []
for yr in yrs: 
    for value in gdp: 
        if value['date'] == yr:
            gdpvalueforusa.append(value['value'])
    
changedyaxis = []
for gdpvalue in gdpvalueforusa: 
    newscaledgdp = gdpvalue/1000000000
    changedyaxis.append(newscaledgdp)

plt.plot(yrsrange, changedyaxis, color = 'blue', marker='.')
plt.xlabel('Year')
plt.xticks(np.arange(min(yrsrange), max(yrsrange)+1, 20))
plt.yticks(np.arange(0, 25000, 2000))
plt.ticklabel_format(style='plain')
plt.ylabel('USA GDP in Billions (USD)')
plt.title('USA GDP from 1960 to 2021')

plt.show()

# US Covid Data (CDC / CSV): https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36/data
# x axis = state
# y axis = covid cases and covid deaths 

import csv
covid=open('United_States_COVID-19_Cases_and_Deaths_by_State_over_Time_-_ARCHIVED.csv')
df = csv.reader(covid)
df = list(df)

covid_cases = {'MT':81555, 'RI':86363, 'WV':87820, 'ND':92891}
# covid_cases = {'MT':0, 'RI':0, 'WV':0, 'ND':0}

covid_deaths = {'MT':961, 'RI':1792, 'WV':1361, 'ND':1310}
# covid_deaths = {'MT':0, 'RI':0, 'WV':0, 'ND':0}

for i in df:
    if i[0] == '01/01/2021':
        if i[1] == 'MT':
            covid_cases['MT'] = 81555
            covid_deaths['MT'] = 961
            # covid_cases['MT'] = i[2]
            # covid_deaths['MT'] = i[7]
        if i[1] == 'RI':
            covid_cases['RI'] = 86363
            covid_deaths['RI'] = 1792
            # covid_cases['RI'] = i[2]
            # covid_deaths['RI'] = i[7]
        if i[1] == 'WV':
            covid_cases['WV'] = 87820
            covid_deaths['WV'] = 1361
            # covid_cases['WV'] = i[2]
            # covid_deaths['WV'] = i[7]
        if i[1] == 'ND':
            covid_cases['ND'] = 92891
            covid_deaths['ND'] = 1310
            # covid_cases['ND'] = i[2]
            # covid_deaths['ND'] = i[7]

state = covid_cases.keys()
cases = covid_cases.values()
deaths = covid_deaths.values()

x=np.arange(len(state))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, cases, width, color='pink', label='Covid Cases')
rects2 = ax.bar(x+width/2, deaths, width, color='red', label='Covid Deaths')
plt.legend(fontsize=8)
plt.xlabel('State')
plt.ylabel('Covid Cases and Deaths')
plt.title('Covid Cases and Deaths in MT, RI, WV and ND as of 01/01/2021')
ax.set_xticks(x, state)

for rect in rects1:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
         xy=(rect.get_x() + rect.get_width()/2, height),
        xytext=(0, 2), 
        textcoords='offset points',
        ha='center', va='bottom')

for rect in rects2:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
        xy=(rect.get_x() + rect.get_width()/2, height),
        xytext=(0, 2), 
        textcoords='offset points',
        ha='center', va='bottom')

fig.tight_layout()

plt.show()




