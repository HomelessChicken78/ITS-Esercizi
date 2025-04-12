'''Replicate the exercise B-4, but this time the list can contain both strings and numbers.
Numbers should be displayed before the strings. Strings should be ordered following the lexico-graphic order'''

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

#This function creates two list, each one of them only contain elements of a specific type
def list_subtype(mylist: list[Any]) -> tuple:
    strings: list[str] = []
    numbers: list[int] = []
    for i in mylist:
        #Fill a list with only numbers
        if isinstance(i, int) or isinstance(1, float):
            numbers.append(i)
        #Fill a list with only strings
        elif isinstance(i, str):
            strings.append(i)
    mytuple: tuple[list[int], list[str]] = (numbers, strings)
    return mytuple

#Output Check
#Fill in the list
values: list[int|float|int] = [
    13, 4.5, "Kiner", "koala", 3, "100", 99, 42, -2, -4,
    "99", 47021, -32, "python", -73.4, 3, 42, -23, "its",
    0, "virgola", "cat", 57.13, 3.14, "cat is on the table"
    ]
print("Unordered list:", values)

#Divide the strings from the numbers
values_tuple: tuple[list[int], list[str]] = list_subtype(values)

#Order the singular elements
values = order(list(values_tuple[0])) + order(list(values_tuple[1]))

#Print the result
print("Ordered list: ", values)