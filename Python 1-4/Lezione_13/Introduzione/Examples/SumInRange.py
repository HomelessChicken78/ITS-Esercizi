def recursiveSumInRange(a: int, b: int) -> int:
    if a > b:
        temp: int = a
        a = b
        b = temp

    if b == a:
        return b
    
    if b > a:
        return b + recursiveSumInRange(a, b-1)

print(recursiveSumInRange(5, 10))
print(recursiveSumInRange(10, 5))