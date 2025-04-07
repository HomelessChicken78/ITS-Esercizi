'''Make the Fibonacci exercise, but this time use iterations'''

def fibonacci(num) -> int:
    if num < 0:
        return None
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    
    sequence: list[int] = [0, 1]
    i: int = 2
    while i <= num:
        sequence.append(sequence[0]+sequence[1])
        sequence.pop(0)
        i += 1
    return sequence[1]


if __name__ == "__main__":
    print(fibonacci(int(input("Insert a number:\n>\t"))))