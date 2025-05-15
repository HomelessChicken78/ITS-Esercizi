class Prodotto:
    def __init__(self, nome: str, quantita: int):
        self.nome = nome
        self.quantita = quantita
    
    def __repr__(self) -> str:
        return f"Prodotto('{self.nome}', {self.quantita})"

    def data(self) -> tuple[str, int]:
        return (self.nome, self.quantita)
    
class Magazzino:
    def __init__(self):
        self.prodotti: list[Prodotto] = []
    
    def aggiungi_prodotto(self, prod: Prodotto):
        if prod not in self.prodotti:
            self.prodotti.append(prod)
        else:
            print("Il prodotto già esiste nel magazzino")
    
    def cerca_prodotto(self, nome: str) -> Prodotto:
        for p in self.prodotti:
            if p.data()[0].lower() == nome.lower():
                return p
    
    def verifica_disponibilità(self, nome: str) -> str:
        cerca = self.cerca_prodotto(nome)
        if cerca and cerca.data()[1] > 0:
            return f"Prodotto \"{nome}\" disponibile in magazzino"
        elif cerca:
            return f"Il prodotto \"{nome}\" non è al momento disponibile in magazzino"
        else:
            return f"Il prodotto \"{nome}\" non esiste nel magazzino"