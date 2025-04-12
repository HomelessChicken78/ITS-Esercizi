'''9. Trova tutti i codici fiscali in un testo

Scrivi una funzione find_fc(text) che trova tutti i codici fiscali all'interno di un testo.

Esempio:

testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
codici = find_fc(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']'''

from re import findall

def find_fc(text: str) -> list[str]:
    '''This functions returns a list containing all of the fiscal codes in the string passed as a parameter'''
    return [fc.upper() for fc in findall(r"[A-Za-z]{6}\d{2}[ABCDEHLMPRST][0-7]\d[A-Za-z]\d{3}[A-Za-z]", text)]

#Expected Output
if __name__ == "__main__":
    text: str = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
    print(find_fc(text))  # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']