class Contatore:
    def __init__(self):
        self.conteggio = 0
    
    def setZero(self) -> None:
        '''Imposta il conteggio a 0.'''
        self.conteggio = 0
    
    def add1(self) -> None:
        '''Incrementa il conteggio di 1.'''
        self.conteggio += 1
    
    def sub1(self) -> None:
        '''Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo.\n
        Se il conteggio è già 0, stampa un messaggio di errore.'''
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
    
    def get(self) -> int:
        '''Restituisce il valore corrente del conteggio.'''
        return self.conteggio
    
    def mostra(self) -> None:
        '''Stampa a schermo il valore corrente del conteggio.'''
        print(f"Conteggio attuale: {self.conteggio}")

if __name__ == "__main__":
    c = Contatore()  
    c.add1()
    c.mostra()

    print()
    c2 = Contatore()  
    c2.sub1()
    c2.mostra()

    print()
    c3 = Contatore() 
    c3.add1()
    c3.add1()
    c3.add1()
    c3.add1()
    c3.sub1()  
    c3.add1()
    c3.add1()
    z  = c3.get()
    print(z)