
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import math


# In[28]:


terror = pd.read_csv("C:/Users/Administrator/Desktop/Python/Python Assignments/DataSets/terror.csv", encoding = "latin")
terror.head()


# In[29]:


terror.columns


# In[30]:


#Q.1)	How many attacks happened in India?
terror[terror.country_txt == "India"].shape[0]


# In[31]:


#Q.2)	How many attacks happened in India and upto 3 people were killed? 
df = terror[(terror.country_txt == 'India') & (terror.nkill <= 3)]
print(df.shape[0])


# In[32]:


#Q.3)	Extract the city and summary for attacks above
df.query("country_txt == 'India' and nkill <= 3")[['country_txt','city','summary']]


# In[33]:


#Q.4)	In a single terror incident in India, find out top 5 cities by number killed
terror[terror.country_txt=='India'][['city','nkill','nwound']].sort_values(by = "nkill",ascending = False).head()


# In[34]:


#Q.5)	In a single terror incident in India, find out top 5 cities by number killed and wounded 
terror[terror.country_txt=='India'][['city','nkill','nwound']].nlargest(5, 'nwound')


# In[35]:


#Q.6)	How many attacks were successful that were suicide attacks?
len(terror[(terror.success ==1) & (terror.suicide == 1)])


# In[36]:


#Q.7) label all the incidents where the number killed was more than 5 as severe. 
terror['label_kill']=['severe' if i > 5.0 else 'not_severe' for i in terror.nkill]
terror['label_kill']


# In[37]:


#Q.8) write a function to label an incident that was both successful and suicidal
def func(x):
           x['Label_Suicide'] = ["Sucide_Success" if( x.iloc[i].suicide == 1 and x.iloc[i].success == 1)   else "Suicide_NotSuccess" for i in list(range(0,len(x)))]
           return x['Label_Suicide']
          
func(terror)


# In[38]:


#Q.9)	Create a new category representing if the incident occured in Afghanistan, 
#Pakistan or India as one level of the category and all the other countries as another level

terror['category']=['Asia' if (terror.iloc[i].country_txt=='Afghanistan' or terror.iloc[i].country_txt=='Pakistan' 
                               or terror.iloc[i].country_txt=='India') else 'ROW' for i in list(range(0,len(terror)))]
#print(terror['category'].head())

terror[['eventid','country_txt','category']].head()


# In[ ]:


#Q.10)	How many incidents happened in Af-Pak-India vs ROW?
p=terror.groupby('category').category.count()
print("incidents happened in Af-Pak-India vs ROW:\n",p)


# In[ ]:


#Q.11)	List the number of suicides attacks and average kills by Af-Pak-India vs ROW. 
#Rename columns in the output as Average_Kills and Number_Incidents.
print(terror.query("suicide == 1").groupby('category')[['nkill']].agg(['count','mean']).
      rename(columns = {'count' : "Number_Incidents",'mean':"Average_kills"}))

