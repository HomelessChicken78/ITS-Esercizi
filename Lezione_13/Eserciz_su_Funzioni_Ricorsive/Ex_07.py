'''
Esercizio 7.

Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. Sia Pi3 una produttoria definita come segue:
Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  

Calcolare il valore della produttoria Pi3 se n = 5.
'''

def recursivePowerSpace(n: int, power_of: int):
    if n < 0:
        return 1
    elif n <= 1:
        return n ** power_of
    else:
        return n**power_of * recursivePowerSpace(n-1, power_of)
    
print(recursivePowerSpace(5, 3))
# print((5**3)*(4**3)*(3**3)*(2**3)*(1**3))