import numpy as np
import pandas as pd

lista = [1,2,3]
lista_np= np.array([list])
print(lista)

matrix=np.array(([1,2],[3,4]))
print(matrix)

df= pd.DataFrame({
'ColA': [1, 2, 3],
'ColB': [4, 5, 6],
'ColC': [7, 8, 9]},
index = ['x', 'y', 'z'])

print(df)
type(df)
