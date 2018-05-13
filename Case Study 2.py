
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import math


# In[29]:


ship = pd.read_csv("C:/Users/Administrator/Desktop/Python/Python Assignments/DataSets/Store.csv",sep = ",",
                   header=0,encoding="Latin")
ship.columns


# In[33]:


#•	How many unique cities are the orders being delivered to
len(ship.City.unique())


# In[14]:


#•	What is the total quantity sold in the East Region?
ship[ship.Region == "East"].count()['Quantity']


# In[15]:


#•	Find the sum of the quantity sold in the East Region
ship[ship.Region == "East"].sum()['Quantity']


# In[17]:


#•	In the south region sort the sales in decreasing order
ship[ship.Region == "South"].sort_values(by = "Sales", ascending = True)


# In[18]:


#•	Find the mean of quantity for every region
ship.groupby('Region').mean()['Quantity']


# In[19]:


#•	Find the mean of sales for every category
ship.groupby('Category').mean()['Sales']


# In[24]:


#•	Find the max, min, sum of sales and profit for every category
max_sp = ship.groupby('Category').max()[['Sales','Profit']]
print(max_sp)

min_sp = ship.groupby('Category').min()[['Sales','Profit']]
print(min_sp)

sum_sp = ship.groupby('Category').sum()[['Sales','Profit']]
print(sum_sp)


# In[39]:


ship.groupby('Category')[['Sales','Profit']].agg(['min','max','sum'])


# In[87]:


#•	Find sum of sales and max profit for every segment
sum_sales = ship.groupby('Segment').sum()['Sales']
print(sum_sales)

max_profit = ship.groupby('Segment').max()['Profit']
print(max_profit)


# In[38]:


ship.groupby('Segment').agg({'Sales':np.sum, 'Profit':np.max})


# In[86]:


#•	For every segment find the mean of the discount
mean_dis = ship.groupby('Segment').mean()['Discount']
print(mean_dis)


# In[80]:


#•	For every segment find the most profitable customers
def get_cid(profit):
    profit = profit.max()
    return ship[ship.Profit == profit]['Customer Name']
group_seg = ship.groupby('Segment').agg({'Profit':[get_cid,'max']})
print(group_seg)


# In[85]:


a = [ship.groupby('Segment').max()['Profit']]
#print(a)
b = [ship.Profit]
#print(b)
ship[['Customer Name','Segment']][np.in1d(b,a)]


# In[45]:


#•	What are the top 5 categories that give maximum profit?
ship.groupby('Sub-Category').max()['Profit'].head(5)


# In[46]:


#•	What is the Total Sales, Quantity, Discount, Profit across Total US.
ship[['Sales','Quantity','Discount','Profit']].sum()


# In[99]:


#•	How many times has it taken more than 5 days from placing an order to shipping
ship['Order Date'] = pd.to_datetime(ship['Order Date'])
#print(ship['Order Date'])
ship['Ship Date'] = pd.to_datetime(ship['Ship Date'])
#print(ship['Ship Date'])

shipping = ship['Ship Date']-ship['Order Date']
print((shipping.dtype))
sum(shipping >'5 days')


# In[96]:


#•	Find the total number of orders in every category which has been shipped with a duration > 5 days
shipmore5 = ship[shipping >'5 days']
ship_order = shipmore5.groupby('Category').count()['Order ID']
print`(ship_order)


# In[102]:


#•	What’s the percentage of items which has been shipped within 5 days
shipless5 = ship[shipping <'5 days']
ship_order1 = shipless5.groupby('Category').count()['Order ID']
ship_order1*100/shipless5.shape[0]


# In[103]:


#•	What’s the percentage of items which has been shipped after 5 days
shipmore5 = ship[shipping >'5 days']
ship_order = shipmore5.groupby('Category').count()['Order ID']
ship_order*100/shipmore5.shape[0]

