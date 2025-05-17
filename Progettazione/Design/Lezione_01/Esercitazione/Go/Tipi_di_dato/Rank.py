from typing import Self

class Rank(int):
    def __new__(cls, v: int|float|str) -> Self:
        if v <= 0:
            raise ValueError("Il rank deve essere un numero positivo")
        return super().__new__(cls, v)

if __name__ == "__main__":
    # rank_mio: Rank = Rank(-2)
    rank_mio: Rank = Rank(22)
    print(type(rank_mio))