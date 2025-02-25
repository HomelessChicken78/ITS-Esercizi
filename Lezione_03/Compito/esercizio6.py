'''Esercizio 6

Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

#Chiede i due numeri
n1: int = int(input("Inserire il primo numero: \n>\t"))
n2: int = int(input("Inserire il secondo numero: \n>\t"))
result = 1 #numero neutro della moltiplicazione

#Fa il prodotto dei numeri in mezzo. Tiene conto di entrambi i casi
if(n1 < n2):
    while (n1 <= n2):
        result *= n1
        n1 += 1
else:
    while (n1 >= n2):
        result *= n1
        n1 -= 1

#Printa il risultato
print(f"Il risultato è: {result}")