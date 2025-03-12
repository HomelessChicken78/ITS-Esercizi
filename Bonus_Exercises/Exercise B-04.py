''''Create a function that, passed a list of integers, it will order them from the smallest to the biggest.
Do not use sets or any built-in function. Try to do so using the function you created in exercise B-3'''

import random
from typing import Any

#This function inverts the position of two elements in a list
def invert_indexes(original_list: list[Any], index_1: int, index_2: int = 0) -> list[Any]:
    if index_1 < 0 or index_1 >= len(original_list) or index_2 < 0 or index_2 >= len(original_list):
        print("Error: One or both indices are out of range.")
        return original_list
    tmp: Any = original_list[index_1]
    original_list[index_1] = original_list[index_2]
    original_list[index_2] = tmp
    return original_list

#Order the list
def order(nums: list[int]) -> list[int]:
    i: int = 0
    j: int = 0
    #Check a number in the list.
    while i < len(nums):
        j = i + 1
        #Check another one and iterate over it. When the number are finished, iterate the next "i"
        while j < len(nums):
            #If the first number is bigger than the second, invert them using the function
            if nums[i] > nums[j]:
                nums = invert_indexes(nums, i, j)
            j += 1
        i += 1
    return nums

#Output Check
#Fill in the list
nums: list[int] = []
for i in range(0, random.randint(3, 7)):
    n = random.randint(-100, 100)
    nums.append(n)

#Print the result
print("Unordered list: ", nums)
print(order(nums))