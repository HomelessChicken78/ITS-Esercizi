from typing import Any

class Frazione:
    __numeratore: int
    __denominatore: int

    def __init__(self, numeratore: int, denominatore: int) -> None:
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def numeratore(self) -> int:
        return self.__numeratore
    
    def denominatore(self) -> int:
        return self.__denominatore
    
    def set_numeratore(self, nuovo_numeratore: int) -> None:
        if isinstance(nuovo_numeratore, int):
            self.__numeratore = nuovo_numeratore
        else:
            self.__numeratore = 13

    def set_denominatore(self, nuovo_denominatore: int) -> None:
        if isinstance(nuovo_denominatore, int) and nuovo_denominatore != 0:
            self.__denominatore = nuovo_denominatore
        else:
            self.__denominatore = 5
    
    def value(self) -> float:
        return round(self.numeratore() / self.denominatore(), ndigits= 3)

    def __str__(self) -> str:
        return f"{self.numeratore()} / {self.denominatore()}"
    
    def irreducible(self) -> bool:
        '''Calculate if the fraction given is irreducible or not'''
        if max_in_two(divisor(self.denominatore()), divisor(self.numeratore())) == 1:
            return True
        return False

def max_in_two(nums_1: list[int], nums_2: list[int]) -> int:
    '''Given two lists, return the highest number that is shared among both of them.
    If no number is found, return False.'''

    # Calculate the maximum of each list individually
    tmp_nums_1: list[int] = nums_1[:]
    tmp_nums_2: list[int] = nums_2[:]

    while tmp_nums_1 and tmp_nums_2:
        max_1: int = max(tmp_nums_1)
        max_2: int = max(tmp_nums_2)

        # Calculate the highest number in both lists
        absolute_max: int = max((max_1, max_2))

        # If the absolute maximum is present in both, it means the absolute maximum is shared. Therefore, return it
        if absolute_max in nums_1 and absolute_max in nums_2:
            return absolute_max
        
        # If that's not the case try both max individually
        if max_1 in nums_2:
            return max_1
        
        if max_2 in nums_1:
            return max_2
        
        # If no condition is met repeat, but before doing that remove items from the list
        tmp_nums_1.remove(max_1)
        tmp_nums_2.remove(max_2)
    
    return False
# print(max_in_two([1, 2, 3, 4, 6, 12], [1, 2, 3, 6, 9, 18]))
# print(max_in_two([12], [18, 19, 20]))
# print(max_in_two([6, 12], [1, 2, 3, 6, 9, 18]))

def divisor(num: int) -> list[int]:
    '''Return a list of numbers that are dividers of the given numbers.
    For 0 an empty list is returned'''
    if num == 0:
        return []

    divisors: list[int] = [1]

    i = 2

    while i <= num:
        if num % i == 0:
            divisors.append(i)
        i+=1
    
    return divisors
# print(divisor(12))
# print(divisor(18))

def mcd(x: int, y: int) -> int:
    res = max_in_two(divisor(x), divisor(y))
    if res:
        return res
    return 1
# print(mcd(12, 18))
# print(mcd(8, 33))
# print(mcd(18, 12))

def semplifica(l: list[Frazione]) -> list[Frazione]:
    res = []
    for fraction in l:
        if fraction.irreducible():
            res.append(fraction)
        else:
            div: int = mcd(fraction.numeratore(), fraction.denominatore())
            fraction.set_numeratore(fraction.numeratore()//div)
            fraction.set_denominatore(fraction.denominatore()//div)
            res.append(fraction)
    return res
# print([f.__str__() for f in semplifica([Frazione(2, 3), Frazione(3, 9), Frazione(4, 2), Frazione(90, 150)])])

def fractionCompare(original_l: list[Frazione], simplified_l: list[Frazione]) -> None:
    if len(original_l) != len(simplified_l):
        print("Le frazioni non hanno la stessa lunghezza")

    else:
        f = 0
        while f <= len(original_l)-1:
            print(f"Valore frazione originale: {original_l[f].value()} - Valore frazione ridotta: {simplified_l[f].value()}")
            f += 1
# fractionCompare([Frazione(2, 3), Frazione(3, 9), Frazione(4, 2), Frazione(90, 150)], [Frazione(2, 3), Frazione(1, 3), Frazione(2, 1), Frazione(3, 5)])

l = [Frazione(2.5, 0), Frazione(1, 2), Frazione(2, 4), Frazione(3, 5), Frazione(6, 9), Frazione(4, 7), Frazione(24, 36), Frazione(12, 36), Frazione(40, 60), Frazione(5, 11), Frazione(10, 45), Frazione(42, 78), Frazione(9, 15)]
l_s = semplifica(l=l)
fractionCompare(l, l_s)