#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ЗАДАНИЕ: Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. 
# Даны значения роста в трех группах случайно выбранных спортсменов: 
# футболисты: 173, 175, 180, 178, 177, 185, 183, 182; 
# хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180; 
# штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.


# In[21]:


import pandas as pd
import numpy as np

footballers = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockeyplayers = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

f_mean = footballers.mean()
f_mean


# In[22]:


h_mean = hockeyplayers.mean()
h_mean


# In[23]:


w_mean = weightlifters.mean()
w_mean


# In[24]:


all_hight = np.hstack((footballers,hockeyplayers, weightlifters))
all_mean = all_hight.mean()
all_mean


# In[25]:


all_s2 = np.sum((all_hight - all_mean) ** 2)
all_s2


# In[26]:


s2f = (f_mean - all_mean) ** 2 * len(footballers) + (h_mean - all_mean) ** 2 * len(hockeyplayers) + (w_mean - all_mean) ** 2 * len(weightlifters)
s2f


# In[27]:


s2_ost = np.sum((footballers - f_mean) ** 2) + np.sum((hockeyplayers - h_mean) ** 2) + np.sum((weightlifters - w_mean) ** 2)
s2_ost


# In[28]:


s2_ost + s2f


# In[ ]:


# ОБЩАЯ ДИСПЕРСИЯ


# In[29]:


s2_general = all_s2 / (len(all_hight) - 1)
s2_general


# In[ ]:


# ФАКТОРНАЯ ДИСПЕРСИЯ


# In[30]:


s2_factor = s2f / (3 - 1)
s2_factor


# In[ ]:


# ОСТАТОЧНАЯ ДИСПЕРСИЯ


# In[31]:


s2_residual = s2_ost / (len(all_hight) - 3)
s2_residual


# In[32]:


F_h = s2_factor / s2_residual
F_h


# In[33]:


len(all_hight)


# In[34]:


alpha = 0.05
d_f1 = 3 - 1
d_f2 = len(all_hight) - 3
d_f1, d_f2


# In[35]:


F_kr = 3.4928

F_kr > F_h


# In[ ]:


# => отмечено существенное различие между выборками.

