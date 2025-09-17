from paziente import Paziente
from dottore import Dottore
from fatture import Fattura

Mr: Dottore = Dottore("Mario", "Rossi", "Medico Generale", 120)
Mr.setAge(56)

Lv: Dottore = Dottore("Luigi", "Verdi", "Pediatra", 140)
Lv.setAge(36)

Aa: Paziente = Paziente("Alice", "Albero", "aa00AA")
Bb: Paziente = Paziente("Bob", "Barattolo", "bb11BB")
Cc: Paziente = Paziente("Charley", "Coccodrillo", "cc22CC")
Dd: Paziente = Paziente("David", "Divano", "dd33DD")

Mr.doctorGreet()
print()
Lv.doctorGreet()
print()

fattura1: Fattura = Fattura([Aa, Bb, Cc], Mr)
fattura2: Fattura = Fattura([Dd], Lv)

print()
print(f"Salvario di Mario Rossi: {fattura1.getSalary()} euro!")
print(f"Salvario di Luigi Verdi: {fattura2.getSalary()} euro!")

print()
fattura1.removePatient("cc22CC")
fattura2.addPatient(Cc)

fattura1: Fattura = Fattura([Aa, Bb, Cc], Mr)
fattura2: Fattura = Fattura([Dd], Lv)

print(f"In totale, l'ospedale ha incassato: tot euro! {fattura1.getSalary() + fattura2.getSalary()}")