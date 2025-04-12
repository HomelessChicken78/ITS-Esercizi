'''
6. Verifica un codice prodotto

Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

Esempio:

check_product_code("PROD-9876-ZX")  # True
check_product_code("PROD-99-ZX")    # False
'''

from re import search

def check_product_code(code: str) -> list[str]:
    '''Returns True if the product's code is correct.'''
    if search(r"^PROD\-\d{4}\-[A-Z]{2}$", code):
        return True
    return False
    

#Expected Output
if __name__ == "__main__":
    print(check_product_code("PROD-9876-ZX"))  # True
    print(check_product_code("PROD-99-ZX"))  # False
    print(check_product_code(""))  #False