from main import *
from custom_types import StatoRiparazione

SC = ServiceCenter()
p = Smartphone("iPhone 14", "Giacomo Coccodrillini", 2022, StatoRiparazione.received, 128, True)
l = Laptop("Hp", "Drago Anonimo", 2020, StatoRiparazione.diagnosing, 15.6, True)
SC.add(p)
SC.add(l)

print(SC.list_all())
print()
print(f"Tempo aspettato per tel: {p.estimated_total_time()} minuti")
print(f"Tempo aspettato per laptop: {l.estimated_total_time()} minuti")

print()
SC.patch_status(p.id, StatoRiparazione.repairing)
print(f"Nuovo stato tel: {p.status}")

print()
SC.delete(l.id)
print(f"Lista dispositivi senza laptop:\n{SC.list_all()}")