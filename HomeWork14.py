#!/usr/bin/env python
# coding: utf-8

# Припустимо, що у нас є дві множини, які містять моделі деяких автомобілів:
# 
# car1 = {"Toyota", "Sedan", "Automatic", "Black"} 
# car2 = {"Honda", "SUV", "Manual", "White"}
# Напишіть логіку, яка повертає множину, що містить спільні моделі обох множин.
# 
# 

# In[7]:


car1 = {"Toyota", "Sedan", "Automatic", "Black"} 
car2 = {"Honda", "SUV", "Manual", "White"} 
car1.isdisjoint(car2)
intersection_set = car1.intersection(*car2)
print(intersection_set)


# In[ ]:





# In[ ]:




