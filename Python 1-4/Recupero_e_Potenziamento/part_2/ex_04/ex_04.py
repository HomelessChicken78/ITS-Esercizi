'''
Scrivere un programma Python che legge in input prima un intero x positivo e poi una sequenza di interi positivi. Se
l'utente inserisce il numero 0, allora la sequenza deve terminare.

Per il numero x e per ogni numero della sequenza inserita, effettuare il controllo che il numero inserito sia
effettivamente un intero e forzare l'utente ad inserire un numero intero positivo nel caso in cui questa condizione non
venga rispettata.
Trovare una soluzione che eviti di scrivere codice duplicato per effettuare questa serie di controlli.
Suggerimento: per controllare che un numeri sia intero, usare la funzione is_integer().

Determinato il numero x e la sequenza di interi positivi, il programma deve produrre in output:
 
    stampare la sequenza

    Il numero occ di occorrenze di x, ovvero  il numero di volte in cui appare x nella sequenza;

    La posizione pos del primo valore uguale a x.

    La somma di tutti i valori diversi da x;


Ad esempio, se l'utente inserisce come valore x il numero 3 e poi immette la sequenza: 7; 5; 1; 3; 3; 3; 11; 2; 3; 3; 0
 
il programma dovra' scrivere in output:

    stampare in output la sequenza

    Il numero 3 compare 5 volte nella sequenza (attenzione all'output se il numero compare 1 sola volta!)

    Il numero 3 compare per la prima volta in posizione 3 nella sequenza

    La somma dei valori della sequenza diversi da 3 e' 26
'''

from typing import Any

def is_integer(num: int) -> bool:
    return isinstance(num, int)

def ask() -> int:
    while True:
        x = input("Inserisci il numero:\n->\t")
        if x.isnumeric():
            x: int = int(x)
        if is_integer(x) and x >= 0:
            break

    return x

def ask_numbers() -> tuple[int, list[int]]:
    x: int = 0
    while x == 0:
        x = ask()

    numbers: list[int] = [ask()]

    while numbers[len(numbers)-1] != 0:
        numbers.append(ask())

    return x, numbers

def count(search: Any, words: list[Any]) -> int:
    tot: int = 0

    for word in words:
        if word == search:
            tot += 1
    
    return tot

def first_occurrence(search: Any, words: list[Any]) -> int:
    i: int = 0

    while i < len(words):
        if words[i] == search:
            return i
        i += 1
    
    return False

def different_sum(ignore: int, numbers: list[int]) -> int:
    tot: int = 0

    for num in numbers:
        if num != ignore:
            tot += num
    
    return tot
    
x, numbers = ask_numbers()
print(numbers)
counted = count(x, numbers)
print(f"Il numero {x} compare {counted} {'volta' if counted == 1 else 'volte'} nella sequenza")
print(f"Il numero {x} compare per la prima volta in posizione {first_occurrence(x, numbers)} nella sequenza")
print(f"La somma dei valori della sequenza diversi da {x} e' {different_sum(x, numbers)}")
