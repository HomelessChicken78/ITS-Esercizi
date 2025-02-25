'''Esercizio 10

Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

    acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
    calcolare e visualizzare la somma di tutti i numeri pari inseriti;
    calcolare e visualizzare la media di tutti i numeri dispari inseriti;
    determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
    se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0

Output:

Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''

numbers: list = []
sum_even = 0
sum_odd = 0
amount_odd = 0
number = 0

#Riempi la lista creata con numeri creati dall'utente
while True:
    number = int(input("Inserisci un numero (0 per terminare): \n>\t"))
    if number != 0:
        numbers.append(number)
    else:
        break

#Fa la somma dei pari e dei dispari
for i in numbers:
    if i%2 == 0:
        sum_even += i
    else:
        sum_odd += i
        amount_odd += 1

#Fa visualizzare la somma dei pari e la media dei dispari
print(f"La somma dei numeri pari è di: {sum_even}")
if amount_odd > 0:
    print(f"Mentre la media dei numeri dispari è di {sum_odd/amount_odd}")

#Calcola i numeri che compaiono più volta inserendoli in un dizionario la cui chiave è il numero stesso, mentre il valore è quante volte essa compare
frequency: dict[int] = {}
i = 0
while (i <= len(numbers) - 1):
    find = False
    for singular_key in frequency:
        if singular_key == numbers[i]:
            find = True
            break
    if find == True:
        frequency[numbers[i]] += 1
    else:
        frequency[numbers[i]] = 1
    i += 1

#Determinare il/i numeri con la frequenza più alta nel dizionario
Max = 0
MaxDict = {}
for key, value in frequency.items():
    if value > Max:
        #Pulisci il dizionario MaxDict
        for key in list(MaxDict.keys()):
            del MaxDict[key]
        #Riempi di nuovo il dizionario col nuovo valore massimo
        MaxDict[key] = value
        Max = value
    elif value == Max:
        #Aggiungi solo il valore al dizionario senza bisogno di svuotarlo
        MaxDict[key] = value

#Printa il risultato
if (len(MaxDict) > 1):
    print(f"I valori con più frequenza compaiono {Max} volte. Essi sono:")
else:
    print(f"Il valore più frequente si manifesta {Max} volte. Esso è")
for key in MaxDict.keys():
    print(key)


'''*NOTARE: Ho usato il break (e "While True") poichè utilizzare la lista stessa nel while mi dava problemi
(cioè, usando "While (numbers[-1]) >= 0" avevo vari problemi, legati soprattutto al fatto che la lista è inizialmente vuota
e, che per qualche ragione, non mi faceva usare operatori di comparazione con "numbers[-1]")
NOTARE2: inizialmente per calcolare la frequenza dei numeri avevo utilizzato due contatori: "i" e "j". Tuttavia, dopo aver avuto diversi problemi - poichè
a ogni iterazione la frequenza trovata ritornava a 1 (per esempio in una lista[1, 2, 2 ,3], il programma trovato il primo "1" ne metteva la frequenza a 1,
poi la portava a 2 e dopodichè la riportava a 1) - ho analizzato meglio il problema e ho deciso che un modo migliore sarebbe stato di farlo controllando se
l'elemento già esiste nella lista o meno.'''