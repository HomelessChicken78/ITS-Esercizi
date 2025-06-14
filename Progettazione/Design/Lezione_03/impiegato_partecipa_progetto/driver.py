from classi import *
from datetime import date

alice: Impiegato = Impiegato("Alice", "Abba", date(2000, 10, 20), 2000)
bob: Impiegato = Impiegato("Bob", "Balcone", date(2001, 2, 4), 1200)
charlie: Impiegato = Impiegato("Charley", "Castagna", date(2004, 10, 16), 2000)

pegaso: Progetto = Progetto("Pegaso", 1000000)
phoenix: Progetto = Progetto("Phoenix", 500000)

oggi: date = date(2025, 6, 12)
# alice.add_progetto(pegaso,oggi)
# pegaso.add_impiegato(alice, oggi)
alice_pegaso: partecipa = partecipa(alice, pegaso, oggi)

print([a.__str__() for a in alice.progetti()])
print([p.__str__() for p in pegaso.impiegati()])

print()
bob_pegaso: partecipa = partecipa(bob, pegaso, oggi)
print([b.__str__() for b in bob.progetti()])
print([p.__str__() for p in pegaso.impiegati()])