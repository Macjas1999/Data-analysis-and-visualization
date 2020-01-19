import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.getcwd()
os.listdir()
file = 'lista_eu.csv'

data = pd.read_csv(file)

print(data.shape)
print(data.columns)
print(data.index)

Y = data['country'].unique()

print(Y)
