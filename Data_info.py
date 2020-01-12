
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


data = pd.read_csv('masterCSVfmfull.csv')


# In[4]:


data.info()


# In[5]:


print(data.shape)
print(data.columns)
print(data.index)


# In[6]:


data.describe()
