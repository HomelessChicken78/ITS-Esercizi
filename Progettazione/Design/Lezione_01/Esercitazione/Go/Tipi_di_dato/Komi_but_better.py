from typing import Self

class Komi(int):
    def __new__(cls, v) -> Self:
        if v < 0 or v > 10:
            raise ValueError(f"The value for komi must be between 0 and 10. {v} is not within that range")
        return super().__new__(cls, v)
    
    def __add__(self, other) -> Self:
        if isinstance(other, Komi|int|float):
            return Komi(int(self) + int(other))
        else:
            return super().__add__(other)
    
    def __sub__(self, other) -> Self:
        if isinstance(other, Komi|int|float):
            return Komi(int(self) - int(other))
        else:
            return super().__add__(other)

if __name__ == "__main__":
    k: Komi = Komi(4)
    # k2: Komi = Komi(23)
    k3 = Komi(k + 1)
    print(k3, type(k3))

    print("Dimostrazione che il Komi è anche un intero:", isinstance(k, int))

    another_komi = k + 1
    print("Sommando un int e un komi si ottiene un komi:", type(another_komi))

    k4 = k + k3
    print("Sommando due komi si ottiene un komi come risultato:", type(k4))

    # print((type(2 + "2")))
    # print((type(Komi(2) + "2")))

    print("Sommando un komi e un float il risultato è un komi", type(Komi(2) + 2.2))

    print("Sottraendo un komi e un int si ottiene un komi:", type(k - 1))

    print("Sottraendo due komi si ottiene un komi come risultato:", type(k4 - k))

    # print((type(2 - "2")))
    # print((type(Komi(2) - "2")))

    print("Sottraendo un komi e un float il risultato è un komi", type(Komi(2) - 2.2))