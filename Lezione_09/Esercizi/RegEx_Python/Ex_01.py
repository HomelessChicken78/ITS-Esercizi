'''
1. Verifica se una stringa è un numero intero

Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.

Esempio:

is_integer("123")      # True
is_integer("-456")     # True
is_integer("12.3")     # False
'''

from re import search

def is_integer(s: str) -> bool:
    '''Returns True if the string is an integer number'''

    #re.search returns "None" if it cannot match anything. We can use it to our advantage.
    if search(r"^-?[0-9]+$", s):
        return True
    return False

#Expected Output
if __name__ == "__main__":
    print(is_integer("123"))  #True
    print(is_integer("-456"))  #True
    print(is_integer("12.3"))  #False
    print(is_integer("a 733"))  #False
