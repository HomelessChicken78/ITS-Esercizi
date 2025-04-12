'''
3. Sostituisci tutti i numeri con '###'

Scrivi una funzione mask_numbers(text) che sostituisce tutte le sequenze di cifre con ###.

Esempio:

text = "Il codice è 12345 e la data è 2025."
mask_numbers(text)  # "Il codice è ### e la data è ###."
'''

from re import sub

def mask_numbers(text: str) -> str:
    '''This function replace all the numbers in a text with a #'''
    return sub(r"\d","#", text)

#Expected Output
if __name__ == "__main__":
    print(mask_numbers("Hello my number is +393934945514"))
    print(mask_numbers("The PIN to unlock my vault is 5514! Use it if you want to!"))
    print(mask_numbers("42 is a cool number"))