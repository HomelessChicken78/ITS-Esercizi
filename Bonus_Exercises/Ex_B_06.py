'''Imagine you are playing an rpg game. Write a function that allows the user to organize their backpack:
- create a dictionary called backpack. Store each item as a key and their quantity as a value.
- the backpack's item are chosen by you
- If the user write "close" the program ends
- if the user writes "quantity", sort the backpack by item quantities from least to most
- If the user writes "quantity" again sort the backpack by item quantities most to least
- If the user writes "view" print all the items in the backpack'''

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

backpack: dict[str, int] = {
    "Sword" : 1,
    "Heal Potion" : 5,
    "Coin" : 50,
    "Slime Ball" : 4,
    "Arrows" : 14,
    "Throwable knife" : 5,
    "Bottle of Water" : 2,
    "Magician hat" : 2,
    "Magic Essence" : 4
}
sort = True

Choice: str = input("What you want to do with the backpack? (\"view\", \"quantity\" or \"close\")\n->\t")
Choice = Choice.lower()
while Choice != "close":
    match Choice:
        case "view":
            print(backpack)
        case "quantity":
            if sort:
                backpack = order(backpack.values)
                sort = False
            else:
                sort = True
        case _:
            print("Wrong command")
    Choice = input("What you want to do with the backpack? (\"view\", \"quantity\" or \"close\")\n->\t")