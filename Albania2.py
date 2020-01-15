
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('masterCSVfmfull.csv')


# In[2]:


df = pd.DataFrame(data, columns = ['sex', 'country', 'year', 'age', 'generation', 'suicides_no',
       'population', 'suicides/100k pop', 'HDI for year', 'gdp_for_year ($) ',
       'gdp_per_capita ($)'])


# In[3]:


dA = pd.DataFrame(data, columns = ['suicides_no'])
dB = pd.DataFrame(data, columns = ['country'])


# In[4]:


dat_all = pd.read_csv('masterCSVfmfull.csv', index_col = ['country', 'sex'])
dat_all


# In[5]:


rows_albania = dat_all.loc["Albania"]
rows_albania
#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html


# In[7]:



x = ['dA']
y = ['dB']
plt.bar(x,y)
plt.show()


# In[ ]:


x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x,y)
plt.show()

