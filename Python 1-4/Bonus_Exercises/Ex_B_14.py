'''Well that was inefficient!
Quick sort: what if instead you try to make something efficient'''

def quick_sort(seq: list[int]) -> list[int]:
    lower: list[int] = []
    higher: list[int] = []

    if len(seq) <= 1:
        return seq

    pivot: int = seq.pop(0)

    for num in seq:
        if num > pivot:
            higher.append(num)
        else:
            lower.append(num)
    
    return quick_sort(lower) + [pivot] + quick_sort(higher)



if __name__ == "__main__":
    from random import shuffle
    my_list = list(range(1, 12001))
    shuffle(my_list)

    print(quick_sort(my_list))