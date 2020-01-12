import pandas as pd
import os

os.getcwd()
print(os.getcwd())
os.listdir()
print(os.listdir())

master = 'masterCSV.csv'

data = pd.read_csv(master)

data.info()
print(data.shape)
print(data.columns)
print(data.index)
print(data.head(2))
data.describe()
print(data.describe())
data['country']
data.country
print(data.country
)
