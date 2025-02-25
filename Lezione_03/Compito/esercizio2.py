'''Esercizio 2

Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa.
Il risultato deve essere visualizzato in output.'''

#Chiedi all'utente di inserire una stringa
sentence: str = input("Digita una frase:\n>\t")
spaces: int = 0

#Conta gli spazi
for i in sentence:
    if i == " ":
        spaces += 1
print(f"\nNumero di spazi presenti in \"{sentence}\": {spaces}")