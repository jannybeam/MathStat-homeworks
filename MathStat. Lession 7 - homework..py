#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# ЗАДАНИЕ №1 (основное)

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b = ((zp * ks).mean() - zp.mean() * ks.mean()) / ((zp ** 2).mean() - (zp.mean() ** 2))
b


# In[40]:


a = ks.mean() - b * zp.mean()
a


# In[41]:


plt.scatter(zp, ks)
plt.plot(zp, a + b * zp)


# In[42]:


mse_ = np.sum(((a + b * zp) - ks) ** 2 / 10)
mse_


# In[43]:


# ЗАДАНИЕ 1 (без использования intercept)

zp = zp.reshape(1, len(zp))
ks = ks.reshape(1, len(ks))

np.dot(np.dot(np.linalg.inv(np.dot(zp, zp.T)), zp), ks.T)


# In[44]:


mse_ = np.sum(((0 + 5.88982042 * zp) - ks) ** 2 / 10)
mse_


# In[38]:


def mse_(w1, y=ks, X=zp, n=10):
    return np.sum((w1 * X - y) ** 2) / n

mse_(5.88982042)


# In[34]:


# ЗАДАНИЕ 1 (с использованием intercept)

zp = np.vstack([np.ones((1, 10)), zp])

np.dot(np.dot(np.linalg.inv(np.dot(zp, zp.T)), zp), ks.T)


# In[52]:


# ЗАДАНИЕ 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

alpha = 1e-6
w1 = 0.1

def mse_(w1, y=ks, X=zp, n=10):
    return np.sum((w1 * X - y) ** 2) / n

for i in range(1000):
    fp = (1 / 10) * np.sum(2 * (w1 * zp - ks) * zp)
    w1 -= alpha * fp
    if i % 100 == 0:
        print(f'iteration: {i}, w1 : {w1}, mse: {mse_(w1) }')

