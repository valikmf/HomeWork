#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input("Введіть число n: "))
word_count = {}
for _ in range(n):
    text = input("Введіть рядок тексту: ")
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
sorted_word_count = [(count, word) for word, count in word_count.items()]
sorted_word_count.sort(reverse=True)
for count, word in sorted_word_count:
    print(f"{word}, {count}")


# In[ ]:




