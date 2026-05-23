#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[16]:


df = pd.read_csv("My_Food_Business_Sales_Inventory.csv")


# In[34]:


df.head()


# In[35]:


df.info()


# In[10]:


df.shape


# In[13]:


df['Date'] = pd.to_datetime(df['Date'])


# In[5]:


df.isnull().sum()


# In[9]:


df.duplicated().sum()


# In[12]:


## Created Month and year Columns.
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year


# In[14]:


##Created Wastage Column.
df['Wastage'] = df['Total_Quantity_Prepared'] - df['Quantity_Sold']


# In[47]:


##Total Revenue.
print(df['Revenue'].sum())


# In[48]:


##Total Profit.
df['Profit'].sum()


# In[45]:


##Net Profit/Loss
print(df['Net_Profit/Loss'].sum())


# In[49]:


## Total Quantity Sold.
df['Quantity_Sold'].sum()


# In[51]:


# Product-wise Revenue Analysis.
product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
product_sales


# In[20]:


##Product-wise NetProfit/Loss Analysis.
product_netProfit_Loss = df.groupby('Product')['Net_Profit/Loss'].sum().sort_values(ascending=False)
product_netProfit_Loss


# In[55]:


##Visualization.
product_sales.plot(kind='bar', figsize=(10,5))
plt.title('Product-wise Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()


# In[21]:


product_netProfit_Loss.plot(kind='bar', figsize=(10,5))
plt.title('Product-wise Profit & Loss')
plt.xlabel('Product')
plt.ylabel('Net_Profit/Loss')
plt.show()


# In[58]:


##Weekend vs Weekday Analysis.
weekend_sales = df.groupby('Weekend')['Revenue'].sum()
weekend_sales


# In[59]:


sns.barplot(x='Weekend', y='Revenue', data=df)
plt.title('Weekend vs Weekday Revenue')
plt.show()


# ###  Weekend sales were higher than weekday sales.

# In[60]:


##Weather Analysis.
weather_sales = df.groupby('Weather')['Revenue'].sum()
weather_sales


# In[61]:


sns.barplot(x='Weather', y='Revenue', data=df)
plt.title('Weather Impact on Revenue')
plt.show()


# ### Rainy weather reduced customer sales.

# In[64]:


##Monthly Net Profit Trend.
month_order = [
    'August','September','October','November',
    'December','January','February',
    'March','April','May'
]

df['Month'] = pd.Categorical(
    df['Month'],
    categories=month_order,
    ordered=True
)

monthly_profit = df.groupby('Month')['Net_Profit/Loss'].sum()


# In[65]:


monthly_profit.plot(kind='line', marker='o', figsize=(10,5))
plt.title('Monthly Net Profit Trend')
plt.ylabel('Net Profit')
plt.show()


# ### The business experienced unstable profits and overall losses across multiple months.
# 

# In[67]:


##Wastage Analysis.
wastage_analysis = df.groupby('Product')['Wastage'].sum().sort_values(ascending=False)
wastage_analysis


# In[68]:


wastage_analysis.plot(kind='bar', figsize=(10,5))
plt.title('Product-wise Wastage')
plt.ylabel('Wastage')
plt.show()


# ### Over-preparation increased food wastage and contributed to business losses

# In[23]:


##Platform Analysis.
platform_profit = df.groupby('Platform')['Net_Profit/Loss'].sum()
platform_profit


# In[24]:


platform_profit.plot(kind='bar', figsize=(8,5))
plt.title('Platform-wise net Loss')
plt.xlabel('Platform')
plt.ylabel('Net Profit')
plt.show()


# ### The business faced losses on all platforms. Offline sales had the highest loss because daily operating expenses were high, while Swiggy and Zomato profits were reduced due to commission charges and fewer orders.

# In[10]:


## Payment Mode Analysis.
payment_sales = df.groupby('Payment_Mode')['Revenue'].sum()
payment_sales


# In[11]:


payment_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Paymrnt_Mode')
plt.ylabel('')
plt.show()


# ### Cash remained the dominant payment method because the area is rural, but digital payments were also widely used.

# ## Overall Insight.
# ### These analysis revealed that the business was generating regular sales ,especially on weekends ,but low daily customer traffic, food wastage, rural area demand limitations, online platform commissions resulted in an overall net business loss.

# In[ ]:




