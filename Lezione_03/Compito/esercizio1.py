'''Esercizio 1

Scrivere un programma che permetta all'utente di inserire una serie di parole in input,
terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''

word: str = ""
while(word != "fine"):
    word = input("Inserire una parola (digita \"fine\" per terminare il programma)\n>\t")
    if (word[0] == word[len(word)-1]):
        print(f"La prima e l'ultima lettera di \"{word}\" sono uguali: \"{word}\" inizia e finisce con la lettera \"{word[0]}\"\n")

'''NOTE POST-TESTING (NON HO MODIFICATO NULLA PER EVITARE DI USCIRE FUORI TRACCIA):
1. se l'utente inserisce una parola contenente un solo carattere, l'if verrà eseguito a prescindere
2. se l'utente non inserisce nulla allora il programma va in errore
3. IL PROGRAMMA E' CASE SENSITIVE!!!'''