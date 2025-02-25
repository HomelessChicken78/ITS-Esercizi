'''Esercizio 7

Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''

#Creo le tre liste (di cui una vuota)
a: list[int] = [0, 5, 12, 80, -3]
b: list[int] = [3, 20, 18, -3, 0]
c: list[int] = []
i: int = 0

#Fanne la somma incrociata
while (i != len(a)):
    c.append(a[i] + b[(len(b)-i)-1])
    i += 1
print(f"lista a: {a}\nlista b: {b}\nlista c: {c}")