
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
import re


# In[2]:

r = requests.get("http://pythonforengineers.com/reddit-raw-data/")

data = r.text

soup = BeautifulSoup(data)


# In[3]:

data_found = None
for s in soup('p'):
    string_found = re.findall("[\w]*\:[\d]+", s.text)
    if string_found:
        data_found = string_found

print data_found        


# In[4]:

data_dict = {}
for data in data_found:
    temp = data.split(":")
    data_dict[temp[0]] = int(temp[1])
    
print data_dict    

