from persona import *
from dottore import *
from paziente import *

# ###Test persone
Nicol: Persona = Persona("Nicol", "Jayasuriya Kuranage Perera")
Nicol.greet()

# Cognome_Invalido: Persona = Persona("Gianfrancesco", 0)
# Cognome_Invalido.greet()
# Eta_Invalida: Persona = Persona("Rachele", "Di Maria")
# Eta_Invalida.setAge("coccodrillo")
# print(f"Rachele Di Maria ha {Eta_Invalida.getAge()} anni")

# ###Test dottori
Mr: Dottore = Dottore("Mario", "Rossi", "Medico Generale", 1300.00)
print()
Mr.doctorGreet()

# Parcella_Invalida: Dottore = Dottore("Ferdinando", "Qualcosini", "Pediatra", [])
# print(Parcella_Invalida.getParcel())

print()
Mr.setAge(35)
Mr.isAValidDoctor()

# ###Test pazienti
Al: Paziente = Paziente("Alice", "Liguri", "ui39PnDML")
print()
Al.patientInfo()