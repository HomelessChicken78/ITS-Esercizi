from classi import *

'''
### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato'''

def print_cool(string: str) -> None:
    join: str = ''.join(['-' for _ in range(len(string))])
    print(f"{join}\n{string}\n{join}")

cifr1: CifratoreAScorrimento = CifratoreAScorrimento(3)
cifr2: CifratoreACombinazione = CifratoreACombinazione

# Leggi testo
text = cifr1.leggi("decodificato.txt")
print("Testo originale:")
print_cool(text)

# Cifratura a scorrimento
codificato = cifr1.codifica(text)
cifr1.scrivi("codifica_a_scorrimento.txt", codificato)
print("\n\n\nTesto codificato a scorrimento:")
print_cool(codificato)

# Decifratura a scorrimento
decodificato = cifr1.decodifica(codificato)
print("\n\n\nTesto decodificato nuovamente:")
print_cool(decodificato)
assert decodificato == text
