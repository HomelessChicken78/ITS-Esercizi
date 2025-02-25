'''Esercizio 9

Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate.
Quindi:

    progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
    modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.

Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''

i: int = 0
value: float = 4
denominator: int = 3

#Usa la sequenza per arrivare più o meno a 3.14
while (((value*100)//1)/100  != 3.14):
    if (i % 2 == 0):
        value -= 4/denominator
    else:
        value += 4/denominator
    i += 1
    denominator += 2
print(f"È necessario usare ~{i} termini per arrivare a ~3.14!")

#Usa la sequenza per arrivare più o meno a 3.141
while (((value*1000)//1)/1000  != 3.141):
    if (i % 2 == 0):
        value -= 4/denominator
    else:
        value += 4/denominator
    i += 1
    denominator += 2
print(f"È necessario usare ~{i} termini per arrivare a ~3.141!")

#Usa la sequenza per arrivare più o meno a 3.1415
while (((value*10000)//1)/10000 != 3.1415):
    if (i % 2 == 0):
        value -= 4/denominator
    else:
        value += 4/denominator
    i += 1
    denominator += 2
print(f"È necessario usare ~{i} termini per arrivare a ~3.1415!")

#Usa la sequenza per arrivare più o meno a 3.14159
while (((value*100000)//1)/100000  != 3.14159):
    if (i % 2 == 0):
        value -= 4/denominator
    else:
        value += 4/denominator
    i += 1
    denominator += 2
print(f"È necessario usare ~{i} termini per arrivare a ~3.14159!")

'''Notare: la formula "((value*10^X)//1)/10^X" serve ad arrotondare (dove X rappresenta quanti decimali vogliamo arrotondare)'''