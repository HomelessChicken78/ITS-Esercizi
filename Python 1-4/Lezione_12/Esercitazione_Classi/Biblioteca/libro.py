class Libro:
    def __init__(self, titolo: str, autore: str):
        self.titolo = titolo
        self.autore = autore
        self.prestato: bool = False
    
    def __str__(self) -> str:
        return f"Titolo: {self.titolo};\nAutore: {self.autore}"