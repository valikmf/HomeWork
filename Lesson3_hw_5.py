#!/usr/bin/env python
# coding: utf-8

# In[16]:


string = input("Введіть список цілих чисел")
lst = [int(num) for num in string.split()]
print(lst)
count0 = lst.count(0) # тут знайшов кількість нулів 
lst1 = [num for num in lst if num != 0]  
lst=lst1+count0*[0]
print(lst) 
 # я намагався якось зробити без циклів, знайшов ось це, але це все одно цикл, доволі цікаво, але розібратися було складно


# In[ ]:




