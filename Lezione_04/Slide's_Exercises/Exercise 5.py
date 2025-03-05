'''Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.
Example:
add_one_to_list([1, 2, 3])
>>> [2, 3, 4]'''

from typing import Any

def add_one(n: int) -> int:
    n += 1
    return n

def add_one_to_list(nums: list[int]) -> None:
    new_list: list[Any] = []
    for n in nums:
        new_list.append(add_one(n))
    print(new_list)

'''Output Check
original: list[int] = [41, 41, 0, -23, 3, 7, 5, 99, 149]
print("Original list: ", original)
print("New list: ", end = "")
add_one_to_list(original)
'''