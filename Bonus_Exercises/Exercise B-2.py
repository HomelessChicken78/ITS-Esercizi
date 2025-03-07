'''Create a function that, passes a number as a parameter, it returns True if the number is prime'''

def is_prime(num: int):
    if num == 1:
        return True
    elif num < 0:
        return False
    i = 2
    while i != (num // 2)+1:
        if num % i == 0:
            return False
        i += 1
    return True

#Output Check
if is_prime(int(input("Insert a number\n>\t"))):
    print("è numero primo")
else:
    print("non lo è")