
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[5]:


data = pd.read_csv('masterCSVfmfull.csv')
data.columns


# In[6]:


data


# In[9]:


eu = pd.read_csv('countries europe1.csv')
eu.columns


# In[14]:


eu['EUC']


# In[24]:


data=data.sort_values(by= 'Albania', ascending=False)


# In[13]:


e = data['country'] - (data['country'] - eu['EUC'])
data[e]

