'''

5. Estrai tutte le date nel formato gg/mm/aaaa

Scrivi una funzione find_dates(text) che trova tutte le date in formato italiano (dd/mm/yyyy) in un testo.

Esempio:

text = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)  # ['09/04/2025', '15/08/2023']
'''

from re import findall

def find_dates(text: str) -> list[str]:
    '''Returns a list which contains all the date in the format dd/mm/yyyy found in a string.'''
    return findall(r"(?:0[1-9]|[1-2]\d|3[01])\/(?:0[1-9]|1[0-2])\/\d{4}", text)

#Expected Output
if __name__ == "__main__":
    print(find_dates("Le date importanti sono 09/04/2025 e 15/08/2023."))  # ['09/04/2025', '15/08/2023']
    print(find_dates("Hey io sono nato il 32/03/2004"))  #[]
    print(find_dates("Dal 20/06/2000 al 17/13/2001. E poi il 00/04/2025"))  #['20/06/2000']