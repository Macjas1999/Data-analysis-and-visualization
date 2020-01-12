import pandas as pd

data = pd.read_csv('masterCSVfmfull.csv')


#suicides_ratio =suicides/100k pop

data.info()
print(data.shape)
print(data.columns)
print(data.index)
data.describe()
print(data.describe())
data['country']
data.country
print(data.country)
