'''
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

For example:
 print(sum_above_threshold([15, 5, 25], 20))
>>> 25
'''

def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    res: int = 0
    for num in numbers:
        if num > threshold:
            res += num
    return res

if __name__ == "__main__":
    print(sum_above_threshold([15, 5, 25], 20))
