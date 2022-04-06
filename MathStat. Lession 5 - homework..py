#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
from scipy.stats import norm 
import math


# In[12]:


# ЗАДАНИЕ №1.


# In[13]:


mean_std = np.sqrt(16) / 256

t_stat(80, mean_std,256 - 1, 0.05, 'two-sided')


# In[ ]:


# ЗАДАНИЕ №2.


# In[6]:


X = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
mean_X = X.mean()
std_X = X.std(ddof=1)
mean_std_X = std_X / (np.sqrt(len(X)))

t_stat(mean_X, mean_std_X,len(X) - 1, 0.05, 'two-sided')


# In[ ]:


# ЗАДАНИЕ №3.


# In[7]:


U_fact = (17.5 - 17) / 4 * np.sqrt(100)

U_fact

#U_cr = 1.645
#U_fact < U_cr ВЕРНА НУЛЕВАЯ ГИПОТЕЗА (НЕ СОВПАДАЕТ С РАССЧЕТОМ В ТЕТРАДИ)


# In[14]:


# ЗАДАНИЕ №4.


# In[15]:


X = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
mean_X = X.mean()
std_X = X.std(ddof=1)

t_fact = (mean_X - 200) / std_X * np.sqrt(10)
t_fact

# t_cr = 3.25
# ВЕРНА НУЛЕВАЯ ГИПОТЕЗА.

