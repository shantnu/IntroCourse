
# coding: utf-8

## Intro to Regex

# In[1]:

str1 = "BigList = 5"

str1.find("List")


# In[2]:

str2 = "BigList_123 = 6"
str3 = "BigList_asd = 88"



# In[3]:

import re

re.findall("BigList_[\d]* = [\d]*", str2)


# In[4]:

re.findall("BigList_[\w]* = [\w]*", str3)


# In[5]:

re.findall("BigList_[\w]* = [\w]*", str2)


# In[5]:



