'''Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.
Expected Output:
Sum of integers from 1 to 10 is 55
Sum of integers from 20 to 37 is 513
Sum of integers from 35 to 49 is 630'''

sum: int = 0
for i in range(1, 11):
    sum += i
print(sum)

sum: int = 0
for i in range(20, 38):
    sum += i
print(sum)

sum: int = 0
for i in range(35, 50):
    sum += i
print(sum)