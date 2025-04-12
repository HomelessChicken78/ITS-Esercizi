'''9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters.
Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. Finally,
implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.'''

from typing import Any
from random import randint

class LotteryMachine:
    def __init__(self, possibilities: list[Any], win: list[Any] = []):
        self.possibilities = possibilities
        self.win = win
    
    def random_pick(self) -> None:
        del self.win[:]
        for n in range(0, 4):
            self.win.append(self.possibilities[randint(0, len(self.possibilities)-1)])
    
    def display(self) -> None:
        print(f"\n{self.win}\nAny ticket matching the above 4 items wins a prize!!")

if __name__ == "__main__":
    my_lottery: LotteryMachine = LotteryMachine(["0", "1", "2", "3", "4", "5", "7", "8", "9", "A", "B", "C", "D", "E"])
    my_lottery.random_pick()
    my_lottery.display()