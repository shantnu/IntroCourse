
# coding: utf-8

# In[30]:

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt


# In[31]:

#get_ipython().magic(u'pylab inline')


# In[32]:

r = requests.get("http://pythonforengineers.com/reddit-raw-data/")

data = r.text

soup = BeautifulSoup(data)


# In[33]:

data_found = None
for s in soup('p'):
    string_found = re.findall("[\w]*\:[\d]+", s.text)
    if string_found:
        data_found = string_found

print data_found        


# In[34]:

data_dict = {}
for data in data_found:
    temp = data.split(":")
    data_dict[temp[0]] = int(temp[1])
    
print data_dict    


# In[35]:

column_names =  ['Language', 'num_subscribers']
reddit_data = pd.DataFrame(data_dict.items(), columns=column_names)


# In[36]:

print reddit_data


# In[37]:

reddit_data.set_index("Language", inplace=True)
print reddit_data


# In[38]:

print "Least popular languages:"
print reddit_data.sort("num_subscribers")[:10]


# In[39]:

print "Most popular languages:"
print reddit_data.sort("num_subscribers", ascending=False)[:10]


# In[40]:

reddit_data.sort("num_subscribers")[:10].plot(kind='bar', title = "The least popular languages on Reddit")

plt.tight_layout()

plt.show()


# In[41]:

top_five =  reddit_data.sort("num_subscribers", ascending=False)[:5]

sum_five = float(top_five.sum())
print sum_five


# In[42]:

top_five['percent'] = (top_five['num_subscribers'] * 100) / sum_five
print top_five


# In[43]:

colors_mine = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightcyan']
explode = (0.1, 0, 0, 0, 0) # only "explode" the 2nd slice (i.red_panda. 'Hogs')
top_five['percent'].plot(kind="pie", autopct='%.2f%%', shadow=True, colors = colors_mine, explode=explode, startangle=90, title = "The Top 5 languages on Reddit")

plt.show()


# In[43]:



