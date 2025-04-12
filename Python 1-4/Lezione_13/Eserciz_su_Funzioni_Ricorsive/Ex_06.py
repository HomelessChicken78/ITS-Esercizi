''' 
Esercizio 6.

Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi una produttoria definita come segue:
Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

Calcolare il valore della produttoria Pi se n = 7.'''

def recursiveProductSpace(n: int, increase: int):
    if n < 0:
        return 1
    elif n <= 1:
        return n + increase
    else:
        return n+increase * recursiveProductSpace(n-1, increase)
    
print(recursiveProductSpace(7, 2))