'''Frequenza di Parole Uniche con Normalizzazione
Scrivi una funzione che prende una stringa di testo (contenente eventualmente
punteggiatura, lettere maiuscole e minuscole, spazi bianchi) e restituisce un dizionario che
associa a ciascuna parola unica (in minuscolo, privata della punteggiatura iniziale/finale) il
numero di occorrenze.
Requisiti:
● Suddividi l’input sugli spazi bianchi per ottenere i token.
● Normalizza ogni token:
1. Converti in minuscolo.
2. Rimuovi la punteggiatura iniziale e finale (ad esempio usando str.strip()
con un insieme di caratteri di punteggiatura).
● Ignora qualsiasi token che diventa stringa vuota dopo la rimozione della
punteggiatura.
● Restituisci un dict dove le chiavi sono parole normalizzate e i valori sono conteggi
interi.
Esempio:
text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)
● # output == {'hello': 2, 'world': 2, 'python': 1}'''

def word_frequencies(text: str) -> dict[str, int]:
    res: dict[str, int] = {}

    text = string_normalization(text)
    words = text.split()

    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    
    return res


def string_normalization(string: str) -> str:
    '''Remove any non alphabetical character and makes the string lowercase as well as stripping it.'''
    string = string.strip().lower()

    list_string: list[str] = [char for char in string]
    list_string_2: list[str] = list_string[:]

    for char in list_string:
        if not char.isalpha() and not char == " ":
            list_string_2.remove(char)
    
    return "".join(list_string_2)


if __name__ == "__main__":
    print(word_frequencies("Hello, world! Hello... PYTHON? world."))