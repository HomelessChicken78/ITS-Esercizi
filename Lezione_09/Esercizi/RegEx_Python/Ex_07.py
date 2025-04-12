'''
7. Verifica un nome proprio

Scrivi una funzione is_valid_name(name) che controlla se la stringa inizia con una lettera maiuscola seguita da almeno due lettere minuscole.

Esempio:

is_valid_name("Marco")    # True
is_valid_name("marco")    # False
is_valid_name("Ma")       # False
'''

from re import search

def is_valid_name(name: str) -> bool:
    '''This function checks if the name, passed as an argument, respects the  following criteria:
    - Starts with an uppercase letter;
    - Follows with at least two lowercase letters.

    If the criteria are met it returns True, otherwise it returns False'''
    if search(r"^[A-Z][a-z]{2,}$", name):
        return True
    return False

#Expected Output
if __name__ == "__main__":
    print(is_valid_name("Marco"))  # True
    print(is_valid_name("marco"))  # False
    print(is_valid_name("Ma"))  # False