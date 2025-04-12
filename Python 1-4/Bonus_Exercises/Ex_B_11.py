'''Exercise 6: Create a recursive function

Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

>>> 55'''

def rec_sum(start: int = 0, end: int = 10):
    if start < end:
        return end + rec_sum(start, end-1)
    else:
        return 0

print(rec_sum())