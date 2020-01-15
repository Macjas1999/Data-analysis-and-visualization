
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


dat_all = pd.read_csv('masterCSVfmfull.csv', index_col = ['country', 'sex'])
dat_all


# In[5]:


rows_albania = dat_all.loc["Albania"]
rows_albania
#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html


# In[6]:


#sex = pd.DataFrame(rows_albania, index_col = ['sex'])


# In[8]:


dev_x = ['sex']
dev_y = ['suicides_no']

plt.plot(dev_x, dev_y)

