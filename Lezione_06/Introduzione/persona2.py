class Persona:
    def __init__(self):
        self.name: str = ""
        self.lastname: str = ""
        self.age: int = 0

    #Funzione che mi mostri in output i dati relativi ad una persone
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")
    
    #Funzione che mi consenta di impostare il valore di self.name
    def setName(self, name: str) -> None:
        self.name = name

    #Funzione che mi consenta di impostare il valore di self.lastname
    def setLastname(self, lastname: str) -> None:
        self.lastname = lastname

    #Funzione che mi consenta di impostare il valore di self.age
    def setAge(self, age: str) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    #Funzione che mi consenta di ritornare il valore di self.name
    def getName(self) -> str:
        return self.name

    #Funzione che mi consenta di ritornare il valore di self.lastname
    def getLastname(self) -> str:
        return self.lastname
    
    #Funzione che mi consenta di ritornare il valore di self.age
    def getAge(self) -> int:
        return self.age