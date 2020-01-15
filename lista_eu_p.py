import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Kraje_eu.csv')

data.drop_duplicates(subset=['country'], keep='first', inplace=True)
print(data)
data.to_csv('lista_eu')
