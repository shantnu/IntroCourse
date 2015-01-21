
# coding: utf-8

## MatplotLib

# In[2]:

import numpy as np
import matplotlib.pyplot as plt


# In[3]:

x = np.linspace(0, 10)
print x


# In[4]:

y_sin = np.sin(x)
y_cos = np.cos(x)


# In[5]:

#get_ipython().magic(u'pylab inline')


# In[10]:

plt.plot(x, y_sin, "-r", label = "Sine Wave")
plt.plot(x, y_cos, "-b", label = "Cos Wave")

plt.legend(loc = "upper right")
plt.title("Sine and Cos graphs")
plt.ylim(-1.2, 1.2)
plt.show()


# In[ ]:



