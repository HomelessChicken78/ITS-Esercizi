'''Esercizio 8

Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******
'''


numbers: list[int] = [ ]
for i in range(5):
    #Più o meno equivalente di un repeat until
    number = int(input("Inserisci un numero compreso tra 1 e 30: \n>\t"))
    if(not((number >= 1) and (number <= 30))):
        while(number < 1 or number > 30):
            number = int(input("NO! Il numero deve esser compreso tra 1 e 30\nInserisci un numero compreso tra 1 e 30: \n>\t"))
    #Dopo aver fatto il "repeat until" metti il numero nella lista
    numbers.append(number)

#Printa gli *
for i in numbers:
    print("*" * i)