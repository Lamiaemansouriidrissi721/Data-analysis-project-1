#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd 


# In[8]:


data=pd.read_csv(r"C:\Users\kumak\Desktop\selfstudy\Python\file.csv")


# In[105]:


data


# In[ ]:


#exploring our data


# In[10]:


data.head()


# In[12]:


data.shape


# In[13]:


data.index


# In[ ]:


#coloumns names


# In[14]:


data.columns


# In[15]:


data.dtypes


# In[20]:


data['Weather'].unique()


# In[17]:


data.nunique()


# In[18]:


data.count


# In[21]:


data['Weather'].value_counts()


# In[22]:


data.info()


# In[ ]:


#Find all unique "wind speed"values in the data


# In[29]:


data.head(2)



# In[30]:


data['Wind Speed_km/h'].nunique()


# In[33]:


data['Wind Speed_km/h'].unique()


# In[32]:


data.nunique()


# In[ ]:


#Find the number of times where the weather is actually clear:


# In[34]:


#value_counts() 
data.Weather.value_counts()


# In[36]:


#filetering
data.head(10)
data[data.Weather=='Clear']


# In[38]:


#groupby()
data.groupby('Weather').get_group('Clear')


# In[ ]:


#Find the number of timers when the 'wind speed' was exactly 4 km/h


# In[42]:


data[data['Wind Speed_km/h'] == 4]



# In[ ]:


#Find out all the null value int the data


# In[51]:


null_values= data[data.isnull()]
null_values


# In[52]:


null_values.sum()


# In[ ]:


#rename the coloumn Wearher to  weather condition


# In[ ]:


data[Weather]='Weather condition'


# In[54]:


data.rename(columns={'Weather': 'Weather condition'}, inplace=True)
data


# In[ ]:


#What is the mean 'Visibility'


# In[59]:


v_mean=data['Visibility_km'].mean()
v_mean


# In[ ]:


#What is the standard deviation of 'pressure'in this data


# In[60]:


P_std=data['Press_kPa'].std()
P_std


# In[ ]:


#what is the variance of the relative humidity


# In[61]:


var_humidity=data['Rel Hum_%'].var()
var_humidity


# In[48]:


null_values.count()


# In[ ]:


#find all instances where snow was recorded


# In[70]:


data.sort_values(by='Date/Time')


# In[71]:


snow_records = data[data['Weather condition'] == 'snow']
snow_records


# In[ ]:


#find all instence where wind speed is above 24 and visibility equal to 25


# In[79]:


speed_wind = data[(data['Wind Speed_km/h'] >24) & (data['Visibility_km'] ==25)]
speed_wind.sort_values(by='Wind Speed_km/h')


# In[ ]:


#what is the mean of each value against each weather value


# In[104]:





# In[89]:


data.groupby('Weather condition').mean()


# In[ ]:


#the min and max of values against each weather condition


# In[90]:


data.groupby('Weather condition').min()


# In[91]:


data.groupby('Weather condition').max()


# In[ ]:


#show all the records where the weather condition is fog


# In[100]:


fog_data = data[data['Weather condition'] == 'fog']
fog_data


# In[ ]:


#find all instance whzere the weather is clear or the visibility is above 40


# In[106]:


condition=data[(data['Weather condition'] =='Clear') | (data['Visibility_km'] >40)]
condition


# In[ ]:


#find all instance when: the weather is clear and the humidity above 50 or visibiility above 40


# In[108]:


condition2=data[(data['Weather condition'] =='Clear')&(data['Rel Hum_%'] =='Clear') | (data['Visibility_km'] >40)]
condition2


# In[ ]:




