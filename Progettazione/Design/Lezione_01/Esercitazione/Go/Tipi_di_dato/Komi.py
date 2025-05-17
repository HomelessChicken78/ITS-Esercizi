from typing import Self

class Komi(int):
    def __new__(cls, v) -> Self:
        if v < 0 or v > 10:
            raise ValueError(f"The value for komi must be between 0 and 10. {v} is not within that range")
        return super().__new__(cls, v)

if __name__ == "__main__":
    k: Komi = Komi(4)
    # k2: Komi = Komi(23)
    k3 = Komi(k + 1)
    print(k3, type(k3))

    print("Dimostrazione che il Komi è anche un intero:", isinstance(k, int))

    not_komi = k + 1
    print("Sommando un int e un komi si ottiene un int:", type(not_komi))

    k4 = k + k3
    print("Sommando due komi si ottiene comunque un int:", type(k4))