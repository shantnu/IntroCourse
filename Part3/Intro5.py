
# coding: utf-8

## In which we cover Numpy

# Numpy is a library that was based on Scipy

# In[1]:

a = [1,2, 3,4,5]


# In[2]:

b = []
for i in a:
    b.append(i * 2)
    
print b    


# In[3]:

a * 2


# In[4]:

b = range(5)
print b


# In[5]:

# Not allowed
# a *b


# In[6]:

import numpy as np

a2 = np.array([1,2,3,4,5])
print a2


# In[8]:

a2 * 2


# In[9]:

b2 = np.arange(5)
print b2


# In[10]:

print a2 * b2


# In[11]:

a3 = np.array([2, 56, 1, 9, 0])
print np.sort(a3)


# In[12]:

print np.mean(a2)


# In[13]:

np.average(a2)


# In[ ]:



