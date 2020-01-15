
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('masterCSVfmfull.csv')
#pd.to_datetime(data['year'], format='%Y')


# In[8]:


df = pd.DataFrame(data, columns = ['sex', 'country', 'year', 'age', 'generation', 'suicides_no',
       'population', 'suicides/100k pop', 'HDI for year', 'gdp_for_year ($) ',
       'gdp_per_capita ($)'])


# In[21]:


da = pd.read_csv('masterCSVfmfull.csv', index_col = ['country'])
da


# In[ ]:


#data.suicides_no.isnull()
#data.suicides_no = data.suicides_no == False
#data[data.suicides_no]
#suicides_no = pd.DataFrame(data, columns = ['suicides_no']
#data[~suicides_no.isnull()]


# In[ ]:


#data['suicides/100k pop'] = data['suicides/100k pop'].astype(int)


# In[ ]:


# data.country== 'Albania' - Warunek filtrujący
#filtr_Albania = df.country == 'Albania'
#suicides_no = pd.DataFrame(df, columns = ['suicides_no'])


# In[ ]:


#filtr_Albania


# In[ ]:


#filtr_Albania['suicides_no'] = filtr_Albania['suicides_no'].astype(int)
#filtr_Albania['suicides_no']


# In[ ]:


#filtr_Albania['suicides_no'].mean()


# In[ ]:


#filtr_Albania['country'].count()


# In[22]:


rows = da.loc["Albania"]
rows


# In[27]:




