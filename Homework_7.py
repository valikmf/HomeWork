#!/usr/bin/env python
# coding: utf-8

# In[3]:


while True:
    n = int(input("Введіть число 1<= n <= 9 : "))
    if 1 <= n <= 9:
        break
    print("Введіть число 1<= n <= 9 : ")
penguin = [
    "   _~_    ",
    "  (o o)   ",
    " /  V  \\  ",
    "/(  _  )\\ ",
    "  ^^ ^^   "
]
for i in penguin:
    print(i * n)


# In[ ]:




