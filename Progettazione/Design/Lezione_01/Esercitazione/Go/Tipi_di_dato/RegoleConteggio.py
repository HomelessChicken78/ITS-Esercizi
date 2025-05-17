from enum import *

class RegoleConteggio(StrEnum):
    giapponese = auto()
    cinese = auto()

if __name__ == "__main__":
    c1 = RegoleConteggio.cinese
    print(c1)

    g1 = RegoleConteggio.giapponese
    print(g1)

    c2 = RegoleConteggio.cinese
    print("c1 e c2 sono uguali?", c1 == c2)

    lista_regole = []
    lista_regole.extend([c1, g1, c2])

    print("\n----------------\nLista regole:\n----------------")
    for r in lista_regole:
        print(r)

    print("\nregola cinese è nella lista delle regole? ", RegoleConteggio.cinese in lista_regole)