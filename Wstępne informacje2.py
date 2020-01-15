
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


data = pd.read_csv('masterCSVfmfull.csv')
data
data.columns


# In[4]:


data


# In[15]:


X = ['Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba',
       'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
       'Barbados', 'Belarus', 'Belgium', 'Belize',
       'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Cabo Verde',
       'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba',
       'Cyprus', 'Czech Republic', 'Denmark', 'Dominica', 'Ecuador',
       'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France', 'Georgia',
       'Germany', 'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary',
       'Iceland', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
       'Kazakhstan', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
       'Lithuania', 'Luxembourg', 'Macau', 'Maldives', 'Malta',
       'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Netherlands',
       'New Zealand', 'Nicaragua', 'Norway', 'Oman', 'Panama', 'Paraguay',
       'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
       'Republic of Korea', 'Romania', 'Russian Federation',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and Grenadines', 'San Marino', 'Serbia',
       'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa',
       'Spain', 'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland',
       'Thailand', 'Trinidad and Tobago', 'Turkey', 'Turkmenistan',
       'Ukraine', 'United Arab Emirates', 'United Kingdom',
       'United States', 'Uruguay', 'Uzbekistan']


# In[54]:


len(X)


# In[55]:


data['year'] = data['year'].astype('category')
data['year']


# In[79]:


Y = data['year'].unique()
Y


# In[77]:


Y.sum()


# In[60]:


data['year'].unique()


# In[62]:


data.drop_duplicates()


# In[31]:


S = ['female', 'male']


# In[71]:


len (data['sex'].


# In[81]:


eu = pd.read_csv('countries europe1.csv')
eu


# In[47]:


data['suicides_no'].sum()


# In[38]:


data['country'].unique()


# In[3]:


#df = pd.DataFrame(data, columns = ['sex', 'country', 'year', 'age', 'generation', 'suicides_no',
#      'population', 'suicides/100k pop', 'HDI for year', 'gdp_for_year ($) ',
#      'gdp_per_capita ($)'])

#df = pd.DataFrame(data)
#df
pd.unique(['country'])


# In[4]:


data.set_index('country', inplace=True)
data


# In[5]:


data.count()
data.


# In[7]:


data['suicides_no'].sum()


# In[8]:


data.index


# In[16]:


data.columns


# In[49]:


c_anb = data.loc['Uzbekistan']


# In[48]:


c_anb['suicides_no'].sum()


# In[17]:


x = data['year']
y = data['suicides_no']
plt.bar(x,y)
plt.show()


# In[19]:


data['country'].sum()


# In[44]:


c_ala = data.loc[['Albania']]
c_ala


# In[46]:


c_ala['suicides_no'].sum()


# In[45]:


c_ala['suicides_no'].value_counts()


# In[23]:


c_ala['suicides_no'].value_counts().reset_index().sort_values(by='index').columns


# In[24]:


snum = c_ala['suicides_no'].value_counts().reset_index().sort_values(by='index')
snum


# In[29]:


x = c_ala['country']
y = snum['suicides_no']
plt.bar(x,y)
plt.show()


# In[31]:


data[['country','year']]

