'''Prossimo: Fra poco dovrai smascherare anagrammi e parole gemelle nelle camere successive.

Parole Gemelle
Due iscrizioni sembrano reciproci riflessi. Verifica l'incanto con `are_anagrams(a, b)`: ritorna `True`
se le due parole/frasi usano le **stesse lettere** al netto degli **spazi** e delle **maiuscole**, altrimenti `False`.
Mantieni la firma e soddisfa i test.'''

def are_anagrams(a: str, b: str) -> bool:
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()

    letters_in_a: dict[str, int] = {
        "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0,
        "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0,
        "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0,
        "y" : 0, "z" : 0
        }
    
    letters_in_b: dict[str, int] = {
        "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0,
        "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0,
        "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0,
        "y" : 0, "z" : 0
        }
    
    for char in a:
        letters_in_a[char] += 1
    
    for char in b:
        letters_in_b[char] += 1
    
    return letters_in_a == letters_in_b

'''Gli archivi delle parole confermano i veri gemelli: Parole Gemelle verificate.'''