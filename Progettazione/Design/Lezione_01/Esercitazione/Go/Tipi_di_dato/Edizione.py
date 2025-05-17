from typing import Self

class Edizione(int):
    def __new__(cls, v: int|float|str) -> Self:
        if v < 1900:
            raise ValueError("L'edizione non può avvenire prima del 1900. Hai qualche amico che prima del 1900 praticava questo sport?")
        return super().__new__(cls, v)

if __name__ == "__main__":
    # year: Edizione = Edizione(1899)
    primo_anno: Edizione = Edizione(1900)
    secondo_anno: Edizione = Edizione(1980)
    terzo_anno: Edizione = Edizione(1985)

    for y in [primo_anno, secondo_anno, terzo_anno]:
        print(y)