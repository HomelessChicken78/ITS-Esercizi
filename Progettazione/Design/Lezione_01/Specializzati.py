from typing import Self

class Money(int):
    def __new__(cls, v: int|float|str) -> Self:
        if v < 0:
            raise ValueError("NON PUOI AVERE SOLDI NEGATIVI! NON SI VA IN DEBITO QUI!")
        return int.__new__(cls, v)

my_money = Money(4)
# impossible_money = Money(-2)
your_money = Money(4)
print(my_money == your_money)