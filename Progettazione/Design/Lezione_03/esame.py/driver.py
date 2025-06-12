from attempt_classi import *

s1: Studente = Studente("Ciao")
s2: Studente = Studente("Buongiorno")

m1: Modulo = Modulo("prog123")
m2: Modulo = Modulo("py321")

e1: esame = esame(m1, 20)
e2: esame = esame(m2, 24)
e3: esame = esame(m1, 31)
e4: esame = esame(m1, 19)

# Aggiungo un esame allo studente
s1.add_esame(e1)
# s1.add_esame(e1)
print(e1._studente)
print([e.voto() for e in s1.esami()])

print()
# Aggiungo un'altro esame allo studente
s1.add_esame(e2)
print(e2._studente)
print([e.voto() for e in s1.esami()])

print()
# Aggiungo un'altro esame allo studente. L'esame che aggiungo appartiene a un modulo che già ha superato
s1.add_esame(e3)
print(e3._studente)
print([e.voto() for e in s1.esami()])
# Questo è sbagliato in quanto ho detto che "Ciao" ha superato due volte il modulo m1 (una volta nell'esame e1 e l'altra nell'esame e3)