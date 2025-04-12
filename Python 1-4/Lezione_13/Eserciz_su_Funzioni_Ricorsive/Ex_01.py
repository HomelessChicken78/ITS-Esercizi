''''Esercizio 1. 

Scrivere in Python una funzione recursivePower che calcola la potenza di un numero utilizzando la ricorsione. La funzione deve ricevere due parametri in input:

    base: il numero da elevare a potenza.
    exponent: l’esponente a cui elevare la base.

Utilizzare, poi, la funzione per calcolare:

    3⁴, ovvero 3 elevato alla potenza di 4. 
    4^3 , ovvero 4 elevato alla potenza di 3.
    2^5, ovvero 2 elevato alla potenza di 5. 
    5^2, ovvero 5 elevato alla potenza di 2.

'''

def recursivePower(base: int, exponent: int) -> int:
    if exponent <= 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * recursivePower(base, exponent-1)

print(recursivePower(3, 4))
print(recursivePower(4, 3))
print(recursivePower(2, 5))
print(recursivePower(5, 2))
