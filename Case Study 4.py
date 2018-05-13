
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np
import math


# In[54]:


air = pd.read_csv("C:/Users/Administrator/Desktop/Python/Python Assignments/DataSets/airquality.csv")
air.columns


# In[55]:


air
air.info()


# In[56]:


#1.	Fetch the observations for 9 day of June
air[(air.Month == 6) & (air.Day == 9)]


# In[57]:


#2.	Find Average temperature for the month of June
air[air.Month == 6].mean()


# In[58]:


#3.	To which day of June has the least temperature
air[air.Month == 6].min()['Temp']


# In[94]:


min = air[air.Month == 6].min()['Temp']
air.Day[(air.Month == 6) & (air.Temp == min)]


# In[95]:


#4.	Find Maximum Ozone value for the month of May
air[air.Month == 5].max()['Ozone']


# In[96]:


#5.	Find the count of the missing values in the ozone column of the data set
len(air.Ozone[np.isnan(air.Ozone)])


# In[97]:


oz = air.Ozone
print(oz.shape[0] - oz.dropna().shape[0])


# In[98]:


air.Ozone.isnull().sum()


# In[99]:


#6.	Find out What is the mean of the Ozone column in this dataset
round(air.Ozone.mean(),2)


# In[102]:


#7.	Find out which month has the highest temperature
air[air.Temp == air.Temp.max()]['Month']


# In[101]:


air.Month[max(air.Temp)]


# In[103]:


#8.	Find out the wind value when the Ozone becomes maximum
air[air.Ozone == air.Ozone.max()]['Wind']


# In[104]:


#9.	Find out the months for which the airquality observations have been carried out
air.Month.unique()


# In[112]:


#10.	Find the Ozone and temperature values for the 1st observation of every month.
air[air.Day == 1][['Month','Ozone','Temp']]


# In[106]:


#11.	Which day of which month corresponds to the least Ozone Value.
air[air.Ozone == air.Ozone.min()][['Month','Day']]


# In[107]:


#12.	Convert the temperature for all the observations to Centigrade scale
def celsius(T):
     return (round(float(5.0)/9.0)*(T-32,2))
celsius(air.Temp)

