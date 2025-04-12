'''Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:
tutti i numeri pari vengano prima di tutti i numeri dispari;
l’ordine relativo tra pari e dispari va mantenuto;
l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.

Test:
print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
>>>[6, 8, 4, 3, 1, 7]
'''

def even_odd_pattern(numbers:list[int]) -> list[int]:
    pari: list[int] = []
    dispari: list[int] = []

    for n in numbers:
        if n % 2 != 0:
            dispari.append(n)
        else:
            pari.append(n)
    
    pari.extend(dispari)

    return pari

if __name__ == "__main__":
    print(even_odd_pattern([3, 6, 1, 8, 4, 7]))