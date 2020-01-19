import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.getcwd()
os.listdir()
file = 'masterCSVfmfull.csv'

data = pd.read_csv(file)
data = data[(data.country == 'Albania') & (data.year >=1995)]
#b = data[(data.year == 1985)]
#TO JEST SUMA SAMOBÓJSTW W DANYM KRAJU
data.info()
print(data.shape)
print(data.columns)
print(data.index)
data.describe()
print(data.describe())
data['country']
data.country
#print(data.country)
print(data['suicides_no'].sum())
#rows_albania = data.loc["Albania"]
#plot1 = rows_albania.loc['Albania','year']
#plot1 = rows_albania.loc[:'Albania', :'year']
#plot1 = rows_albania[['year', 'suicides_no']]
#s_no =  rows_albania[['suicides_no']]

#plot1.dropna(inplace = True)
#rows_albania['year']= rows_albania['year'].str.split(',' , n=0, expand = False)
#plt.style.use('fivethirtyeight')

#print(plot1['year'])

#x = plot1['year']

#y = plot1['suicides_no']

#plt.plot(x,y, label='gr')



#plt.xlabel('Rok')
#plt.ylabel('Liczba samobójstw')
#plt.title('Liczba samobójstw na przestrzeni lat')

#plt.legend()

#plt.tight_layout()

#plt.savefig('')

#plt.show()
