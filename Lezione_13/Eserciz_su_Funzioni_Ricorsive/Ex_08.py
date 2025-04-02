'''Esercizio 8.

Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa
formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.'''

def vowelsCounter(string: str, vowel: int=0) -> int:
    vowels: list[str] = ["a", "e", "i", "o", "u", "y"]
    if len(string) == 0:
        return 0
    elif string[0].lower() in vowels:
        return 1+vowelsCounter(string[1:])
    else:
        return vowelsCounter(string[1:])

if __name__ == "__main__":
    print(vowelsCounter("aeiouy"))
    print(vowelsCounter("ciao"))
    print(vowelsCounter("aiuole"))
    print(vowelsCounter("pIzzA"))