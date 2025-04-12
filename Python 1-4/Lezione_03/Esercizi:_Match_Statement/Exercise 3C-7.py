'''r
Esercizio 3C-7. Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente con 2 cifre decimali.
Usare il match statement.

Expected Output:

Per ciascun lancio della moneta inserisci "t" o "T" se e' uscito "testa" mentre inserisci "c" o "C" se e' uscito "croce".

Lancio 1: t
Lancio 2: c
Lancio 3: t
Lancio 4: t
Lancio 5: c
Lancio 6: c
Lancio 7: t
Lancio 8: t

Totale "testa": 5
Percentaule "testa": 62.50%

Totale "croce": 3
Percentuale "croce": 37.50%
'''

#Crea e riempi la lista con i "t" o "c". Se l'utente inserisce altro, forzane l'inserimento
lanci: list[str] = []
testa: int = 0
croce: int = 0  #Fun fact: questa variabile si può anche calcolare facendo 8 - testa
for i in range(0, 8):
    lancio: str = input("Inserire \"t\" se esce testa o \"c\" se esce croce:\n>\t")
    lancio = lancio.lower()
    while lancio not in ["t", "c"]:
        lancio = input("Errore, carattere non riconosciuto!\nPerfavore, inserire \"t\" se esce testa o \"c\" se esce croce:\n>\t")
    lanci.append(lancio)

#Incrementa le variabili a seconda se l'elemento della lista su cui si itera è "c" o "t" (NB: non vi è un caso default in quanto non è possibile altri casi oltre a "t" e "c")
for lancio in lanci:
    match lancio:
        case "t":
            testa += 1
        case "c":
            croce += 1

#Calcola il risultato in percentuale (fatto direttamente nel print) e stampalo a schermo
print("\n------------------------------------\n")
print(f"Totale \"testa\": {testa}\nPercentuale \"testa\": {(testa/8)*100:.2f}%\n")
print(f"Totale \"croce\": {croce}\nPercentuale \"testa\": {(croce/8)*100:.2f}%\n")