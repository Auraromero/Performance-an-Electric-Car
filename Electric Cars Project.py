#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Impoting Data ser
electric_car = pd.read_csv('ElectricCarData_Norm.csv')


# In[3]:


# Checking content of data (first five rows)
electric_car.head()


# In[6]:


# Porcentage of missing data
print("Porcentage of missing values")
print(electric_car.isnull().mean())


# In[8]:


# Make a copy of the file
electric_cars = electric_car.copy()


# In[14]:


electric_cars.head()


# In[13]:


# Check data type
electric_cars.dtypes


# In[39]:


electric_cars.isnull().sum()


# In[24]:


# Drp unnecessary columns
electric_cars.drop(['Segment', 'Seats','PlugType', 'BodyStyle'], axis = 1, inplace = True)


# In[25]:


electric_cars.head(10)


# In[27]:


# Checking for duplicates
electric_cars.duplicated()


# In[33]:


# Let's make some quick analisys of the data
# Let's count the number of car/model per Brand

modelper_brand = electric_cars['Model'].groupby(electric_cars['Brand'])
print(modelper_brand)


# In[36]:


modelper_brand.agg('sum')


# In[40]:


electric_cars


# In[42]:


electric_cars.to_csv('electric_cars_clean.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




