'''Esercizio 4.

Scrivere una funzione ricorsiva recursiveDigitCounter che restituisca il numero di cifre di un numero intero n passato
in input.
Sono permessi sia valori positivi che negativi per n.
Ad esempio, il numero -120 ha 3 cifre.
Non si tenga conto di eventuali zeri non significativi.

Suggerimento: per il calcolo delle cifre, fare un controllo se il valore assoluto di n sia minore di 10. In caso positivo,
significa che il numero n ha una sola cifra. In caso negativo, significa che il numero n ha più cifre; dunque, dividere n
per 10 per rimuovere l'ultima cifra e richiama ricorsivamente la funzione, fino a ottenere un numero con una sola cifra.'''

# def recursiveDigitCounter(n):
#     n = abs(n)
#     return len(str(n))

def recursiveDigitCounter(n: int) -> int:
    if abs(n) < 10:
        return 1
    else:
        return 1 + recursiveDigitCounter(n//10)

if __name__ == "__main__":
    print(recursiveDigitCounter(-100)) #>>> 3
    print(recursiveDigitCounter(123)) #>>> 3
    print(recursiveDigitCounter(1)) #>>> 1
    print(recursiveDigitCounter(-20)) #>>> 2
    print(recursiveDigitCounter(0)) #>>> 1