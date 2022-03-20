#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
from math import factorial as fl

def combinations(n, k):
    return fl(n) / (fl(k) * fl(n - k))


# In[ ]:


# ЗАДАНИЕ №1.


# In[37]:


salaries = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


# In[38]:


# Среднее арифметическое:
salaries_mean = salaries.sum() / salaries.size


# In[39]:


# Среднее квадратичное отклонение:
(np.sum((salaries - salaries_mean)**2) / salaries.size)**0.5


# In[40]:


# Смещенная дисперсия:
np.sum((salaries - salaries_mean)**2) / salaries.size


# In[41]:


# Несмещенная дисперсия:
np.sum((salaries - salaries_mean)**2) / (salaries.size - 1)


# In[ ]:


# ЗАДАНИЕ №2.


# In[49]:


# Ящик 1 - 0 белых мячей, ящик 2 - 3 белых мяча:
p1 = (combinations(5, 0) * combinations(3, 2)) / combinations(8, 2) * ((combinations(5, 3) * combinations(7, 1)) / combinations(12, 4))
p1


# In[50]:


# Ящик 1 - 1 белый мяч, ящик 2 - 2 белых мяча:
p2 = (combinations(5, 1) * combinations(3, 1)) / combinations(8, 2) * ((combinations(5, 2) * combinations(7, 2)) / combinations(12, 4))
p2                                                                      


# In[51]:


# Ящик 1 - 2 белых мяча, ящик 2 - 1 белый мяч:
p3 = (combinations(5, 2) * combinations(3, 0)) / combinations(8, 2) * ((combinations(5, 1) * combinations(7, 3)) / combinations(12, 4))
p3                                                                       


# In[52]:


p = p1 + p2 + p3
p


# In[ ]:


# ЗАДАНИЕ №3.


# In[53]:


A = 1/3 * 0.9 + 1/3 * 0.8 + 1/3 * 0.6
A


# In[54]:


# Выстрел произведен первым спортсменом:
(1/3 * 0.9) / A


# In[55]:


# Выстрел произведен вторым спортсменом:
(1/3 * 0.8) / A


# In[56]:


# Выстрел произведен третьим спортсменом:
(1/3 * 0.8) / A


# In[57]:


# ЗАДАНИЕ №4.


# In[58]:


A = 1/4 * 0.8 + 1/4 * 0.7 + 1/2 * 0.9
A


# In[59]:


# Факультет А:
(1/4 * 0.8) / A


# In[60]:


# Факультет В:
(1/4 * 0.7) / A


# In[61]:


# Факультет С:
(1/2 * 0.9) / A


# In[ ]:


# ЗАДАНИЕ №5.


# In[62]:


# Выйдут из строя все делали:
0.1 * 0.2 * 0.25


# In[63]:


# Выйдут из строя 2 детали:
0.9 * 0.2 * 0.25 + 0/8 * 0.1 * 0.25 + 0.75 * 0.1 * 0.2


# In[64]:


# Выйдет из строя хотябы 1 деталь:
1 - 0.9 * 0.8 * 0.75


# In[65]:


# Выйдет из строя от 1 до 2 деталей:
1 - 0.9 * 0.8 * 0.75 - 0.1 * 0.2 * 0.25

