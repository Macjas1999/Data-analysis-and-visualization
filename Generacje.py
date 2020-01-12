from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('masterCSVgeneration.csv')
year = data['year']
age = data['age']
generation = data['generation']

print(generation)
