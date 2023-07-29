#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
keys_a = list(a.keys())
keys_b = list(b.keys())
common_keys = []
for key in keys_a:
    if key in keys_b:
        common_keys.append(key)
common_keys[0], common_keys[1] = common_keys[1], common_keys[0]        
print(*common_keys)


# In[ ]:




