'''Esercizio 1

Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')'''

class FileManager:

    def __init__(self, f: str, mode: str) -> None:
        self.f = f
        self.mode = mode

    def __enter__(self) -> None:
        self.wrap = open(self.f, self.mode)
        print("Opened the file correctly")
        return self.wrap
    
    def __exit__(self, exc_type, exc_value, tracebac):
        print(exc_type)

with FileManager('Esercizi/example.txt', 'w') as f:

    f.write('Hello, world!')

with FileManager('Esercizi/dsagggwd.txt', 'r') as f:

    f.read()