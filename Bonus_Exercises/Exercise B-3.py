'''Make a function that, passes a list and two index of that list, it will invert those two elements and return the new list.
If the index don't exist an error message is printed and the original list is returned instead'''

from typing import Any

def invert_indexes(original_list: list[Any], index_1: int, index_2: int = 0) -> list[Any]:
    tmp: Any = original_list[index_1]
    original_list[index_1] = original_list[index_2]
    original_list[index_2] = tmp
    return original_list

#Output Check
print(invert_indexes([3, 2, 1], 2))
print(invert_indexes([7, 2, 4, 6, 1, 8, 9, 11], 4))