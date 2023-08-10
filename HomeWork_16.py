#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result
    return wrapper


# In[ ]:




