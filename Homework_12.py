#!/usr/bin/env python
# coding: utf-8

# In[5]:


string = input("Введіть строку")
count = {}
for i in string:
    count[i] = count.get(i, 0) + 1
for i, count in count.items():
    print(f"{i}, {count}")


# In[ ]:




