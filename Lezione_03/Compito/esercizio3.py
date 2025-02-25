'''Esercizio 3

Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che corrisponda alla versione invertita della stringa originale.
Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

#Chiedi di inserire una stringa
word: str = input("Inserire una stringa:\n>\t")
word2 = ""
j = -1

#Inverti la stringa (e mettila in una nuova variabile)
for i in word:
    word2 += word[j]
    j -= 1

#Printa la versione invertita della stringa
print(f"\"{word}\" invertita diventa: \"{word2}\"")