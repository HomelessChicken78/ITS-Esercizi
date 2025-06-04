'''
Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.

[1, 7, 3, -5, 10], 5 -> -15
'''

def  mul(numbers: list[int], threshold: int) -> int:
    res = 1

    for n in numbers:
        if n < threshold:
            res *= n
    
    return res

if __name__ == "__main__":
    print(mul([1, 7, 3, -5, 10], 5))