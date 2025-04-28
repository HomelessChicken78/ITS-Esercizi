from typing import Any
from persona import Person

class Student(Person):
    
    '''
    def inheritanceTest(self):
        #verificare che la classe studente eriditi tutti gli attributi della classe Persona
        self.name
        self.surname
        self.age

        #verificare che la classe studente eridit tutti i metodi della classe Persona
        self.getName()
        self.getSurname()
        self.getAge()
    '''
    '''
    attributi ereditati dalla classe persona
        self.name
        self.surname
        self.age

    attributi della classe
        self.matricola
    '''

    #inizializzare un oggetto della classe studente
    def __init__(self, name: str, surname: str, age: int, matricola: str):
        #inizializzare la superclasse
        super().__init__(name, surname, age)  #super() è una funzione built-in che ci consente di richiamare i metodi della superclasse

        #inizializzare la classe Studente
        #istruzioni che inizializzano uno studente
        self.setMatricola(matricola)
    
    #metodi setter

    #metodo che ci consente di impostare il valore dell'attributo self.matricola
    def setMatricola(self, matricola: str) -> None:

        #se la stringa non è vuota:
        if matricola:
            self.matricola = matricola
        else:
            raise ValueError("\n\nThe value for \"matricola\" cannot be an empty string!\n")
    
    #metodo che ritorna il valore dell'attributo self.matricola
    def getMatricola(self) -> str:
        return self.matricola
    
    #metodo che consente di visualizzare le informazioni relative ad un oggetto della classe Student
    def __str__(self) -> str:
        return f"Name: \t\t{self.name}\nSurname: \t{self.surname}\nAge: \t\t{self.age} years old\nMatricola: \t{self.getMatricola()}"
    
    def __repr__(self) -> tuple[str, str, int, str]:
        return ((self.name, self.surname, self.age), self.matricola)
    
    #metodo che mi consente di calcolare la media degli esami sostenuti da uno studente:
    def getMediaEsami(self, voti_esami: list[int]) -> float:
        #se la lista non è vuota
        if voti_esami:
            #calcolare la somma dei voti
            res: int = 0
            for voto in voti_esami:
                res += voto
            
            #ritornare la media
            return round(res/len(voti_esami), 2)
        
        #se la lista è vuota
        else:
            return 0.00
        
    # metodo che consente di confrontare due oggetti della classe Student e stabilire che questi due oggetti siano uguali o meno. (quando si fa x == y (o in questo caso self == other))
    # due studenti sono uguali se hanno la stessa matricola
    def __eq__(self, other: Any) -> bool:
        # se other è None, oppure se other non è un'istanza della classe Student ritorno "False"
        if other is None or not isinstance(other, type(self)):
            return False
        #altrimenti valuta la seguente uguaglianza
        else:
            return self.getMatricola() == other.getMatricola()