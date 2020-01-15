import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('masterCSVfmfull.csv', index_col = ['country','year','suicides_no'])
rows_albania = data.loc["Albania"]

plt.style.use('fivethirtyeight')

x = [['year']]

y = [['suicides_no']]
plt.plot(x,y, label='gr')



plt.xlabel('Rok')
plt.ylabel('Liczba samobójstw')
plt.title('Liczba samobójstw na przestrzeni lat')

plt.legend()

plt.tight_layout()

plt.savefig('')

plt.show()
