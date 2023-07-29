#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
number = random.randint(1, 10)
while True:
    user_number = int(input("Вгадайте число від 1 до 10: "))
    if user_number == number:
        print("Вітаємо! Ви вгадали число!")
        break
    elif user_number < number:
        print("Введене число менше від загаданого.")
    else:
        print("Введене число більше від загаданого.")


# In[ ]:




