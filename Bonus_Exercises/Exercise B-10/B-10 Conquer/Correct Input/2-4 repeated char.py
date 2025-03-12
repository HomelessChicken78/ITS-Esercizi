'''2.4 if there are not, check if any character is repeated'''

def isrepeated(num_sys: str) -> bool:
    duplicate: str = ""
    i: int = 0
    while len(num_sys) > 0:
        duplicate += num_sys[0]
        num_sys = num_sys[1:]
        print(f"{duplicate[-1]} in {num_sys}")
        if duplicate[-1] in num_sys:
            return False

if __name__ == "__main__":
    print(isrepeated(input("Insert something:\n>\t")))