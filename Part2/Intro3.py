
# coding: utf-8

# In[5]:

import requests
from bs4 import BeautifulSoup
import re


# In[6]:

r = requests.get("http://pythonforengineers.com/reddit-raw-data/")

data = r.text

soup = BeautifulSoup(data)


# In[17]:

data_found = None
for s in soup('p'):
    string_found = re.findall("[\w]*\:[\d]+", s.text)
    if string_found:
        data_found = string_found

print data_found        


# In[3]:



