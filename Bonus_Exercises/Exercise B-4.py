''''Create a function that, passed a list of integers, it will order them from the smallest to the biggest.
Do not use sets or any built-in function. Try to do so using the function you created in exercise B-3'''

import random
from typing import Any

def invert_indexes(original_list: list[Any], index_1: int, index_2: int = 0) -> list[Any]:
    if index_1 < 0 or index_1 >= len(original_list) or index_2 < 0 or index_2 >= len(original_list):
        print("Error: One or both indices are out of range.")
        return original_list
    tmp: Any = original_list[index_1]
    original_list[index_1] = original_list[index_2]
    original_list[index_2] = tmp
    return original_list

def order(nums: list[int]) -> list[int]:
    i: int = 0
    j: int = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] > nums[j]:
                nums = invert_indexes(nums, i, j)
            j += 1
        i += 1
    return nums

nums: list[int] = []
for i in range(0, random.randint(3, 7)):
    n = random.randint(-100, 100)
    nums.append(n)

print("Unordered list: ", nums)
print(order(nums))