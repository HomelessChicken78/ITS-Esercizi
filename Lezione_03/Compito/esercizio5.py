'''Esercizio 5

Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna.
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

    • Acquisisca in input un valore N (numero di euro disponibili).
    • Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
    • Mostri quanti buoni sconto avanzano al termine dell'acquisto.
Esempio:
Se l'utente inserisce N = 6, può acquistare 6 barrette ottenendo 6 buoni sconto, che gli permettono di riscattare 1 ulteriore barretta gratuita, per un totale di 7 barrette. Alla fine, non rimarranno buoni sconto inutilizzati.

Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.'''

#Chiedi quanti euro l'utente ha
barrette: int = int(input("Quanti euro hai? (non inserire i centesimi, non inserire il simbolo dell'euro)\n>\t"))

#Calcola quanti extra barrette si possono comprare con i buoni
buoni = barrette // 6

#printa il risultato e i buoni di avanzo 
print(f"Potresti acquistare {barrette + buoni} barrette\nTi avanzerebbere {barrette % 6} buoni")