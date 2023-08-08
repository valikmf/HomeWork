#!/usr/bin/env python
# coding: utf-8

# In[8]:


from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calc_average_value(numbers):
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)  
    squared_numbers = map(lambda x: x ** 2, odd_numbers)  
    total_sum = reduce(lambda x, y: x + y, squared_numbers) 
    count = len(numbers)
    average = total_sum / count  
    return average
value = calc_average_value(numbers)
print(f"Середнє значення: {value}")


# In[ ]:




