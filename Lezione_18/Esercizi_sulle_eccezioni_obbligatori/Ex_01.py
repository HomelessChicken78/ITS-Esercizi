'''Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using
math.sqrt(). Handle ValueError if the input is negative by returning an informative message.'''

from math import sqrt

def safe_sqrt(number: int) -> int:
    try:
        sqrt(number)
    except ValueError as error:
        print("ERROR!")
        return 0
        # raise ValueError(error)
    else:
        return sqrt(number)

print(safe_sqrt(-2))