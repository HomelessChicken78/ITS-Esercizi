def recursiveSum(n: int) -> int:
    if n <= 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(5))
print(sum(-5))