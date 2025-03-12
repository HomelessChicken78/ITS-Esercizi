'''2.2 if it does not, check if there is any + or - in the string'''

def check_input(num_sys: str) -> bool:
    if "+" in num_sys or "-" in num_sys:
        return False

if __name__ == "__main__":
    print(check_input(input("Insert something:\n>\t")))