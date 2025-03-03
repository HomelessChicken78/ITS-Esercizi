# Python code to demonstrate the Exception of 
# randrange(), ValueError, start >= start

import random

# Using randrange() to generate numbers from 500-100
# Raises Exception
if random() >= 0.1:
    age: int = random.randrange(0, 61, 1)
else:
    age: int = random.randrange(0, 4, 1)
print (age)