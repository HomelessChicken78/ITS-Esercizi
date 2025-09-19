class Pagamento:
    __import: float

    def __init__(self):
        self.setImport(0.00)

    def getImport(self) -> float:
        '''View the import'''
        return self.__import
    
    def setImport(self, money: int) -> float:
        '''Set the import value'''
        self.__import = money

    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento: €{self.getImport():.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()
    
    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento in contanti: €{self.getImport():.2f}")
    
    def inPezziDa(self) -> None:
        '''Stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro,
        1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.'''

        rimanente: float = self.getImport() + 0.001
        banconote: list[float] = [500.00, 200.00, 100.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.5,  0.2, 0.1, 0.05, 0.02, 0.01]

        print("In pezzi da:")
        for b in banconote:
            if rimanente >= b:
                contante = rimanente // b
                print(f"{b:.2f}€: {contante}")
                rimanente -= contante * b

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, titolare: str, scadenza: str, numero_carta: str):
        super().__init__()

        self.__titolare = titolare
        self.__scadenza = scadenza
        self.__numero_carta = numero_carta
    
    def getTitolare(self) -> str:
        return self.__titolare

    def getScadenza(self) -> str:
        return self.__scadenza
    
    def getNumeroCarta(self) -> str:
        return self.__numero_carta
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.getImport():.2f}\nsulla carta {self.getNumeroCarta()} (scadenza: {self.getScadenza()}) di {self.getTitolare()}")

if __name__ == "__main__":
    contanti1: PagamentoContanti = PagamentoContanti()
    contanti1.setImport(1499.79)
    contanti1.inPezziDa()
    contanti1.dettagliPagamento()

    print()
    contanti2: PagamentoContanti = PagamentoContanti()
    contanti2.setImport(50)
    contanti2.dettagliPagamento()

    print()
    carta1: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Enrico Attrezzi", "13 luglio 2028", "027384001")
    carta1.setImport(119.99)
    carta1.dettagliPagamento()

    print()
    carta2: PagamentoCartaDiCredito = PagamentoCartaDiCredito("Samantha Della Barba", "25 gennaio 2029", "0003474850")
    carta2.setImport(44.99)
    carta2.dettagliPagamento()






























'''Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321'''