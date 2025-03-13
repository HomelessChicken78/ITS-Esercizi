'''2.2 if it does not, check if there is any + or - in the string'''

def not_contains_sign(num_sys: str) -> bool:
    if "+" in num_sys or "-" in num_sys:
        return False
    return True

if __name__ == "__main__":
    print(not_contains_sign(input("Insert something:\n>\t")))