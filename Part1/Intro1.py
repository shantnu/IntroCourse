
# coding: utf-8

# In[4]:

import requests
from bs4 import BeautifulSoup


# In[5]:

r = requests.get("http://pythonforengineers.com/reddit-raw-data/")

data = r.text

soup = BeautifulSoup(data)


# In[ ]:


for s in soup('p'):
    print s.text


# In[ ]:



