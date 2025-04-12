class Persona:
    #Costruttore
    def __init__(self, name: str, lastname: str, age: int):
        #self è una keyword che assume come valore l'oggetto 
        self.name = name
        self.lastname = lastname
        self.age = age

    #Funzione che mi mostri in output i dati relativi ad una persone
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")