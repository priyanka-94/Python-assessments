
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import math


# In[141]:


oj = pd.read_csv("C:/Users/Administrator/Desktop/Python/Python Assignments/DataSets/oj.csv")
print(oj.head())


# In[142]:


# 1.	Find the dimensions of the oj data set
np.shape(oj)


# In[143]:


# 2.	Find the structure of the data set
oj.info()


# In[144]:


#3.	Find out the column names in the data set
oj.columns


# In[145]:


#4.	Describe the data set
pd.DataFrame.describe(oj)


# In[148]:


oj.describe


# In[150]:


#1.	Fetch the first row 3rd column from the data set
print(oj.iloc[0,[2]])


# In[151]:


#2.	Fetch the first, second and Third columns of the oj data frame

print(oj.iloc[:,[0,1,2]])


# In[152]:


# 3.	Fetch the first, second, eighth and the 456th rows of the 1st, third and the sixth columns of the data frame
print(oj.iloc[[0,1,7,455],[0,2,5]])


# In[ ]:


#4.	Fetch the top 5 rows of the brand column
print(oj.loc[0:4,['brand']])


# In[153]:


oj.head()['brand']


# In[ ]:


#5.	Fetch top 5 rows of the brand, week and feat details
print(oj.loc[0:4,['brand','week','feat']])


# In[156]:


oj.head()[['brand','week','feat']]


# In[ ]:


#6.	Fetch the details of all distinct stores
print(oj.store.unique())


# In[ ]:


#7.	Fetch all the observations for Tropicana brand
oj[oj.brand=="tropicana"]


# In[ ]:


#8.	Fetch all the observations for Tropicana brand using query function
oj.query("(brand == 'tropicana')")


# In[ ]:


#9.	Fetch bottom 5 observations for those who have bought Tropicana or dominics
oj[(oj.brand == "tropicana") | (oj.brand == "dominics")].tail(5)


# In[ ]:


#10.	Fetch the income, brand, price observations with Tropicana brand without feature advertisement
oj[(oj.brand == "tropicana") & (oj.feat == 0)][['INCOME','brand','price']]


# In[ ]:


#11.	Add a new column in the dataset: logInc which is the logarithm of the income
oj['LogInc'] = list(map(lambda x:math.log(x), oj.INCOME))
oj.head()


# In[ ]:


#12.	Sort the Data in the increasing order of the week
oj.sort_values(by = 'week')


# In[ ]:


#13.	Sort the data in the decreasing order of Income
oj.sort_values(by = 'INCOME', ascending = False)


# In[159]:


#14.	Find the mean of the juice price for each brand
oj.groupby('brand').mean()['price']


# In[158]:


oj.groupby('brand').price.mean()


# In[ ]:


#15.	Find the average income for each brand and at each store
oj.groupby(['brand','store']).mean()['INCOME']


# In[ ]:


#16.	Find:
#a.	Mean and std deviation of the income
mean_inc = oj.INCOME.mean()
print(mean_inc)
sd_inc = oj.INCOME.std()
print(sd_inc)


# In[161]:


oj['INCOME'].agg({'mean','std'})


# In[168]:


pd.crosstab(oj.INCOME,oj.brand)


# In[162]:


oj.groupby(['brand']).agg({'week':np.mean,'INCOME':np.sum})


# In[ ]:


#b.	For income greater than or equal to 10.5, find the mean income
oj[oj.INCOME>=10.5].mean()['INCOME']


# In[ ]:


#c.	For each brand having price >=2.5 find the mean, median, sd of the log of income
mean_log = oj[oj.price>=2.5].groupby('brand').mean()['LogInc']
print(mean_log)


# In[ ]:


median_log = oj[oj.price>=2.5].groupby('brand').median()['LogInc']
print(median_log)


# In[ ]:



sd_log = oj[oj.price>=2.5].groupby('brand').std()['LogInc']
print(sd_log)


# In[ ]:


#17.	Find the Cross tabulation of brands and feature advertisement
pd.crosstab(oj.brand,oj.feat)

