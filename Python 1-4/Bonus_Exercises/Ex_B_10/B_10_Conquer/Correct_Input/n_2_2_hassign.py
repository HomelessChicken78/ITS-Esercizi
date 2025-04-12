'''2.2 if it does not, check if there is any + or - in the string'''

def has_sign(num_sys: str) -> bool:
    if "+" in num_sys or "-" in num_sys:
        return True
    return False

if __name__ == "__main__":
    print(has_sign(input("Insert something:\n>\t")))