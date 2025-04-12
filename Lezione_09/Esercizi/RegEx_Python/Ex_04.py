'''
4. Verifica un CAP

Scrivi una funzione is_valid_cap(cap) che restituisce True se il CAP è valido (5 cifre), False altrimenti.

Esempio:

is_valid_cap("70124")   # True
is_valid_cap("A0123")   # False
'''

from re import search

def is_valid_cap(cap: str) -> bool:
    '''Returns True if the italian CAP is valid.
    Otherwise it reutrns False'''
    if search(r"^\d{5}$", cap):
        return True
    return False

#Expected Output
if __name__ == "__main__":
    print(is_valid_cap("00054"))  #True
    print(is_valid_cap("A0123"))  # False