'''Esercizio 9.

Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma
di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da
restituire.
'''

def vowelRemover(string: str) -> str:
    vowels: list[str] = ["a", "e", "i", "o", "u", "y"]
    if len(string) == 0:
        return string
    elif string[0] in vowels:
        return vowelRemover(string[1:])
    else:
        return string[0] + vowelRemover(string[1:])

if __name__ == "__main__":
    print(vowelRemover("Cristiano"))
    print(vowelRemover("CeaPoeoUi"))