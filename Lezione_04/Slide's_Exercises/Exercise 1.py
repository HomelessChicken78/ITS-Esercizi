'''Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.'''

def check_value(n: int = 1) -> None:
    if n > 5:
        print(f"The number {n} is greater than the number 5")
    elif n < 5:
        print(f"The number {n} is less than the number 5")
    else:
        print(f"The number {n} is equal to the number 5")

'''Output check
check_value(12)
check_value(-2)
check_value(5)'''