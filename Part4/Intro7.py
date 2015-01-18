
# coding: utf-8

## In which we study Pandas

# In[1]:

import pandas as pd


# In[2]:

data = pd.ExcelFile("intro_pandas.xls")


# In[3]:

print data.sheet_names


# In[4]:

data_sheet1 = data.parse(u'Sheet1')


# In[5]:

data_sheet1


# In[6]:

data_sheet1.sort('Age')


# In[7]:

data_sheet1.sort('Salary')


# In[8]:

get_ipython().magic(u'pylab inline')


# In[9]:

data_sheet1.plot('Name', 'Age')
plt.show()


# In[10]:

data_sheet1.plot('Name', 'Salary')
plt.show()


# In[ ]:



