'''Esercizio 4

Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali).
L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

    1. Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
    2. Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).
'''
numbers: list[float] = []
result: float = 0.0
amount_integers: int = 0
minimum: float = 0 #per minimum dobbiamo successivamente portare il primo valore messo come minimo
maximum: float = 0 #teoricamente, siccome i numeri negativi non vengono calcolati, potremo mettere maximum come un qualsiasi numero negativo. tuttavia per mantere consistenza con minimum, facciamo come abbiamo fatto per quest'ultimo

#Chiedi ciascun numero. Quando incontri un numero negativo esci tramite break.*
while True:
    number = float(input("Inserisci un numero:\n>\t"))
    if(number < 0):
        break
    else:
        numbers.append(number)
        if(number.is_integer()):
            result += number
            amount_integers += 1
    #Come detto precedentemente, la prima iterazione è quella che di fatto va a inizializzare minimum e maximumù
    if(len(numbers) == 1):
        minimum = number
        maximum = number
    if(number < minimum):
        minimum = number
    elif(number > maximum):
        maximum = number
#Calcolo della media sfruttando la variabile "amount integers". Se quest'ultimo è zero (e quindi nessun intero è stato inserito) la media non è calcolata.
if(amount_integers > 0):
    result /= amount_integers
    print(f"La media dei numeri interi inseriti è: {result}")

#Scrivi il minimo e il massimo
print(f"Il numero più grande è: {maximum}\nIl numero più piccolo è: {minimum}")

'''*NOTARE: Ho usato il break (e "While True") poichè utilizzare la lista stessa nel while mi dava problemi
(cioè, usando "While (numbers[-1]) >= 0" avevo vari problemi, legati soprattutto al fatto che la lista è inizialmente vuota
e, che per qualche ragione, non mi faceva usare operatori di comparazione con "numbers[-1]")
ALTRA NOTA: per il calcolo del minimo e del massimo era possibile utilizzare probabilmente un set o un .sort(). Ho tuttavia preferito utilizzare
questo metodo anche per rimanere consistente con la soluzione dei flow chart
ULTIMA NOTA: se nessun numero è inserito il minimo e il massimo saranno 0'''