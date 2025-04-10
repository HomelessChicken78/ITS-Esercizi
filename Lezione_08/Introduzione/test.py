from persona import Person
from studente import Student

#creare un oggetto "p" di classe persona
p: Person = Person("Cristiano", "Coccia", 21)

#visualizzare le informazioni relativa alla persona "p"
print(p)

#creare l'oggetto studente1 di classe Student
studente1: Student = Student("Mario", "Rossi", 33, "0198ABZX")

#voglio controllare che studente sia istanza della classe Studente
if isinstance(studente1, Student):
    print("\nl'oggetto \"studente1\" è un oggetto della classe Student")

#La funzione isinstance(obj, Class) -> True se l'oggetto obj è un'istanza della classe Class

#voglio sapere se student1 sia anche istanza della classe Person dato che la classe Student eredita dalla classe Person
if isinstance(studente1, Person):
    print("\nl'oggetto \"student1\" è anche un'istanza della classe Person")
else:
    print("\nl'oggetto \"student1\" è solo un'istanza della classe Student e non della classe Persona")

#voglio controllare che l'oggetto p sia un'istanza di Person
if isinstance(p, Person):
    print("\nl'oggetto p è un'istanza della classe Person")

#voglio controllare se l'oggetto p sia anche istanza della classe Student
if isinstance(p, Student):
    print("\nl'oggetto \"p\" è anche un'istanza della classe Student")
else:
    print("\nl'oggetto \"p\" è solo un'istanza della classe Person e non della classe Student")

#voglio controllare se Student è sottoclasse della classe Person
#issubclass(Class1, Class2) -> Controllare se Class1 è sottoclasse della classe Class2: -> In caso affermativo ritorna "True"
if issubclass(Student, Person):
    print("\nla classe Student è sottoclasse della classe Person")

#voglio controllare se Person è sottoclasse della classe Student
if issubclass(Person, Student):
    print("\nla classe Person è sottoclasse della classe Student")
else:
    print("\nla classe Person non è sottoclasse della classe Student")

print(studente1)
print(studente1.__repr__())

print(f"La media dei voti relativi agli esami sostenuti dallo studente {studente1.getName()} è: {studente1.getMediaEsami([10, 20, 30])}")

#creiamo uno studente2 oggetto della classe Student
studente2: Student = Student(p.getName(), p.getSurname(), p.getAge(), "IO19CC43")
print(studente2)

#confrontare se student1 == p
print("\n", studente2 == p)

#confronto studente1 e studente2
print("\n", studente1 == studente2)

#verifichiamo che lo studente1 sia uguale a sè stesso
print("\n", studente1 == studente1)

#modificare nome, cognome, età dello studente2 affinchè abbia stesso nome, stesso cognome, stessa età dello studente1
studente2.setName(studente1.getName())
studente2.setSurname(studente1.getSurname())
studente2.setAge(studente1.getAge())

#confronto studente1 con studente2
print("\n", studente1 == studente2)

# ho forzato la matricola dello studente2 ad essere uguale alla matricola dello studente1
studente2.setMatricola(studente1.getMatricola())

#confronto se studente1 è == studente2
print("\n", studente1 == studente2)