'''
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista
di numeri interi. Un elemento è considerato isolato se non è affiancato sia a destra che a
sinistra da elementi uguali.

For example:
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
>>>2

print(count_isolated([1, 2, 3, 4, 5]))
>>>5'''

def count_isolated(MyList: list[int]) -> int:
    count: int = 0
    i: int = 0
    while i < len(MyList):
        #This is to prevent going out of range of the list
        if i == len(MyList) - 1:
            if not (MyList[i] == MyList[i-1]):
                count += 1

        else:
            if not (MyList[i] == MyList[i-1] or MyList[i] == MyList[i+1]):
                count += 1
        i += 1
    return count


if __name__ == "__main__":
    print("Test 1\n",
          count_isolated([1, 2, 2, 3, 3, 3, 4]))
    print("Test 2\n",
          count_isolated([1, 2, 3, 4, 5]))

'''Fun fact: i had my "i" increased inside the elif, instead of having it increased outside of the if-statement blocks, leading to infinite loops'''
