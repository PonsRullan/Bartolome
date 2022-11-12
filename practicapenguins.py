#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install palmerpenguins')


# In[2]:


import pandas as pd
from palmerpenguins import load_penguins


# In[3]:


penguins = load_penguins()


# In[73]:


penguins1=penguins.dropna()
print(penguins1)


# In[5]:


penguins2=penguins1.iloc[:,[2,6]]
penguinssex=penguins2.groupby('sex').count()
penguinssex


# In[6]:


penguinssex1=penguins2.groupby('sex').mean()
penguinssex1


# In[68]:


penguins3=penguins1.iloc[:,[2,3]]
bill_area=penguins3['bill_length_mm']*penguins3['bill_depth_mm']
penguins3['bill_area']=bill_area
penguins4=penguins3
print(penguins4)


# In[62]:


penguins5=penguins1.iloc[:,[0,2,6]]
penguins6=penguins5.groupby(['species','sex']).mean()
print(penguins6)


# In[64]:


penguins6['sex']=np.arange(len(penguins6))%2
penguins7=penguins6[penguins6['sex'] == 0]
penguins7=penguins7.drop(['sex'],axis=1)
print(penguins7)


# In[74]:


penguins8=penguins1
body_mass_kg=penguins8['body_mass_g']*0.001
penguins8['body_mass_kg']=body_mass_kg
penguins8=penguins8.drop(['body_mass_g'],axis=1)
print(penguins8)


# In[ ]:




