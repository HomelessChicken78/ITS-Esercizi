'''8. Trova parole con lettere maiuscole e numeri

Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, con lettere maiuscole e numeri.

Esempio:

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
find_codes(text)  # ['AB12CD34', '12345678']'''

from re import findall

def find_codes(text: str) -> list[str]:
    '''This function returns a list containing all the words have a total of 8 characters, that can be uppercase letters or numbers'''
    return findall(r"(?:[A-Z]|\d){8,}", text)

#Expected Output
if __name__ == "__main__":
    print(find_codes("I codici sono AB12CD34 e 12345678 e XYZZYZZZ"))  # ['AB12CD34', '12345678']