
# coding: utf-8

# In[ ]:


#Crime in India
#•	This dataset contains complete information about various aspects of crimes happened in India from 2001. Most of the data is from 2001 to 2010. But there are few files which has data only from 2011 and few are having 2001-14.
#•	OBJECTIVE: - The objective this exercise is to understand how you approach a problem statement and visualize it by solving in Python
###•	What is the major reason people being kidnapped in each state.
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import os


# In[ ]:


os.chdir("C:/Users/Administrator/Desktop/Data vizualization/Data Set/rajanand-crime-in-india")


# In[ ]:


reason = pd.read_csv("39_Specific_purpose_of_kidnapping_and_abduction.csv")


# In[ ]:


reason.columns


# In[ ]:


reason = reason[['Area_Name','Sub_Group_Name','K_A_Grand_Total']]


# In[ ]:


reason.columns


# In[ ]:


reason = reason[0:3231]


# In[ ]:


reason = reason.dropna(subset = reason.columns)


# In[ ]:


reason.shape


# In[ ]:


res_sta = reason.groupby(['Sub_Group_Name','Area_Name']).sum()
type(res_sta)


# In[ ]:


res_sta.columns


# In[ ]:


res_sta.index


# In[ ]:


frle = (res_sta.index.labels)
coln = [list(x) for x in frle]
print(len(coln[0]))


# In[ ]:


frli = res_sta.index.levels
ind = ([list(x) for x in frli])
print(ind[1])


# In[ ]:


type(coln[0][0])


# In[ ]:


col1 = list()
col2 = list()
col = list()
for i in [0,1]:
    nlab = coln[i]
    nlev = ind[i]
    col = list()
    for j in range(0,len(nlab)):
        col.append(nlev[nlab[j]])
    if(i == 0):
        col1 = col
    else:
        col2 = col


# In[ ]:


print(col1)


# In[ ]:


sumKA = list(res_sta.K_A_Grand_Total)


# In[ ]:


dictReas = ({"Reason" : col1, "State" : col2, "Sum" : sumKA})
df = pd.DataFrame(dictReas)


# In[ ]:


df.head()


# In[ ]:


df2 = df.pivot("State","Reason","Sum")
gr = sns.heatmap(df2, linewidths=.3,center=1)

