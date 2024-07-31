#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import string
def password(length, complexity):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    characters = ""
    if "lowercase" in complexity:
        characters += lowercase_letters
    if "uppercase" in complexity:
        characters += uppercase_letters
    if "digits" in complexity:
        characters += digits
    if "special" in complexity:
        characters += special_characters
    if not characters:
        print("Error: Select at least one character set for complexity.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    password_length = 12
    password_complexity = ["lowercase", "uppercase", "digits", "special"]
    password = password(password_length, password_complexity)
    if password:
        print("Generated Password:",password)


# In[ ]:





# In[ ]:




