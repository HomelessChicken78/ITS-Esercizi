'''
Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico
'''

oggetti: list[str] = []

#Riempi la lista
for i in range(3):
    oggetto = input("Scrivi il nome di un oggetto:\n>\t")
    oggetti.append(oggetto.lower())

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")

'''INDIFFERENTEMENTE DALL'ORDINE
match oggetti:
    case oggetti if "penna" and "matita" and "quaderno" in oggetti:
        print("Materiale scolastico")
    case oggetti if "pane" and "latte" and "uova" in oggetti:
        print("Prodotti alimentari")
    case oggetti if "sedia" and "tavolo" and "armadio" in oggetti:
        print("Mobili")
    case oggetti if "telefono" and "computer"and "tablet" in oggetti:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")'''