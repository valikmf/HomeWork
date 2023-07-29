#!/usr/bin/env python
# coding: utf-8

# In[3]:


string = input("Введіть список цілих чисел")
lst = [int(num) for num in string.split()]
print(lst)
lst1 = []
for num in lst:
    if num not in lst1:
        lst1.append(num)
print(lst1)


# In[ ]:




