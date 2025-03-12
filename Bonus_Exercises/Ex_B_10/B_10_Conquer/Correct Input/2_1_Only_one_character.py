'''2.1 check if it contains only one character'''

def check_input(num_sys: str) -> bool:
    if len(num_sys) <= 1:
        return False
    
if __name__ == "__main__":
    print(check_input(input("Insert something:\n>\t")))