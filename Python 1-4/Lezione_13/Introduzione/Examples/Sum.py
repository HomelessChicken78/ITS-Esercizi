def recursiveSum(n: int) -> int:
    if n < 0:  #User inputted a negative number: unsupported
        print("Error")
        return 0
    elif n == 0:  #Stop when you arrive to 0
        return 0
    # elif n <= 0.9999:
    #     return 0
    else:
        return int(n + recursiveSum(n-1))
    
s: str = "-----------------"
print(recursiveSum(-5))
print(s)
print(recursiveSum(0))
print(s)
print(recursiveSum(5))
# print(s)
# print(recursiveSum(5.3468726))