#!/usr/bin/env python
# coding: utf-8

# **1) Написати лямбда-функцію, що перевірить, чи є число парним і викликати її.** 
# 
# 

# In[13]:


parne = lambda x: x % 2 == 0

n = int(input("Введіть число: "))

if parne(n):
    print(f"{n} є парним числом.")
else:
    print(f"{n} не є парним числом.")


# **2) Написати рекурсивну функцію для пошуку максимального елемента в списку**

# In[8]:


def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max(lst[1:])
        return max(lst[0], max_rest)
# Приклад
numbers = [3, 8, 1, 6, 10, 5] 
print(find_max(numbers))  #  10


# **3) Дано список кортежів, кожен з яких містить два значення: назва фільму (рядок) і рейтинг (дійсне число). Напишіть функцію(ї),  що поверне найбільш і найменш популярні з списку.**
# 

# In[12]:


films_data = [
    ('Captain Marvel', 7.0),
    ('Aladdin', 7.4),
    ('Toy Story 4', 8.2),
    ('Avengers: Endgame', 8.7)
]
def get_rating(film):
    return film[1]
most_popular = max(films_data, key=get_rating)
least_popular = min(films_data, key=get_rating)
print("Найпопулярніший фільм:", most_popular)
print("Найменш популярний фільм:", least_popular)


# In[ ]:




