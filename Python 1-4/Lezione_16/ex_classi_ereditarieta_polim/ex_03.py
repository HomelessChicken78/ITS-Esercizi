class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi_veicolo(self) -> None:
        '''metodo che stampa una descrizione del veicolo'''
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self) -> None:
        '''metodo che stampa una descrizione del veicolo'''
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self) -> None:
        '''metodo che stampa una descrizione del veicolo'''
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

if __name__ == "__main__":
    a1: Auto = Auto("honda", "non lo so", 2025, 5)
    a1.descrivi_veicolo()

    print()
    veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
    auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
    moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

    veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
    auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
    moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto