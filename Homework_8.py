#!/usr/bin/env python
# coding: utf-8

# In[8]:


string = input("Введіть рядок: ")
string1 = "  !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" # те що треба прибрати з строки 
string2 = "" # Видаляємо всі зайві символи та пробіли з введеного рядка
for a in string:
    if char not in string1:
        string2 += a
if not string2: # порожня строка чи ні 
    print("Хештег не може бути порожнім.")
else:
    hg = "#" + string2.title()[:139]
    hg=hg.replace(" ", "")
    print(hg)


# In[ ]:




