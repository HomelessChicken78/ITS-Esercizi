'''
9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called simulate_until_win(self, my_ticket) that:

    Accepts a ticket (a list of 4 items).
    Repeatedly draws random tickets using the draw_ticket() method.
    Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    Returns the number of attempts and the winning ticket.

2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

    Your ticket
    The winning ticket
    How many attempts it took to win
'''

from typing import Any
from random import randint

class LotteryMachine:
    def __init__(self, pool: list[Any], win: list[Any] = [], my_ticket: list[Any] = []):
        self.pool = pool
        self.win = win
        self.my_ticket = my_ticket
    
    def random_pick(self) -> None:
        del self.win[:]
        for n in range(0, 4):
            self.win.append(self.pool[randint(0, len(self.pool)-1)])
    
    def display(self) -> None:
        print(f"\n{self.win}\nAny ticket matching the above 4 items wins a prize!!")
    
    def draw_ticket(self) -> list[Any]:
        del self.my_ticket[:]
        for n in range(0, 4):
            self.my_ticket.append(self.pool[randint(0, len(self.pool)-1)])

    def simulate_until_win(self, my_ticket: list[Any] = []):
        attempts: int = 0
        while self.my_ticket != self.win:
            self.draw_ticket()
            attempts += 1
        return attempts

my_ticket: LotteryMachine = LotteryMachine(["0", "1", "2", "3", "4", "5", "7", "8", "9", "A", "B", "C", "D", "E"])
my_ticket.random_pick()
my_ticket.display()
print("\n----------------------------------------------------\n")
print(f"It took {my_ticket.simulate_until_win()} attempts to win. My ticket is in fact: {my_ticket.my_ticket}")