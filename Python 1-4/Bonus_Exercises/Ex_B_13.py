'''Bogo sort: write a function that takes a list and order it in the most inefficient way possible'''

import random

def is_ordered(seq: list[int]) -> bool:
    i: int = 0
    while i < len(seq)-1:
        if seq[i] > seq[i+1]:
            return False
        i += 1
    return True

def bogo_sort(seq: list[int]) -> list[int]:
    while not is_ordered(seq):
        # print(seq)
        random.shuffle(seq)
    return seq

if __name__ == "__main__":
    my_list = list(range(1, 12))
    random.shuffle(my_list)

    print(bogo_sort(my_list))