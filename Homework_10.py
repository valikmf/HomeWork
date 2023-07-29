#!/usr/bin/env python
# coding: utf-8

# In[3]:


for a in range(1, 101):
    if a % 3 == 0 and a % 5 == 0:
        print("Fizz Buzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)


# In[ ]:




