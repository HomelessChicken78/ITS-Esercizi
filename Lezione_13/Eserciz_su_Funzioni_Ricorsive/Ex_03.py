'''Esercizio 3.

Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.'''

def recursiveFactorial(nb: int) -> int:
    if (not isinstance(nb, int)) or nb <= 0:
        return 1
    if nb > 1:
        return nb*recursiveFactorial(nb - 1)
    else:
        return 1

if __name__ == "__main__":
    print(recursiveFactorial(1))
    print(recursiveFactorial(0))
    print(recursiveFactorial(4))

