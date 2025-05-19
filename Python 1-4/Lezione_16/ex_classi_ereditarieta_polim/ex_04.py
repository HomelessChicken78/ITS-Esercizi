class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione_iniziale = popolazione_iniziale
        self.popolazione_attuale = popolazione_iniziale
        self.tasso_crescita = tasso_crescita
    
    def cresci(self) -> None:
        '''Aggiornare la popolazione per l'anno successivo.'''
        self.popolazione_attuale = int(self.popolazione_attuale * (1 + self.tasso_crescita/100))

    def getDensita(self, area_kmq: float) -> int:
        '''Calcola in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².'''
        y: int = 0
        while self.popolazione_attuale / area_kmq < 1:
            self.cresci()
            y += 1
        return y
    
    def anni_per_superare(self, other: 'Specie') -> int:
        '''Calcola in quanti anni la popolazione di questa specie supererà quella di un'altra specie.'''
        y = 0
        while self.popolazione_attuale <= other.popolazione_attuale and y < 1000:
            self.cresci()
            other.cresci()
            y += 1
        return y


class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("BufaloKlingon", popolazione_iniziale, tasso_crescita)

class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)


if __name__ == "__main__":
    # Creazione delle istanze delle specie
    bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
    elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

    # # # Calcolo degli anni necessari per superare
    anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
    print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}") # 16

    # Calcolo della densità di popolazione per i Bufali Klingon
    anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
    print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}") # 4
