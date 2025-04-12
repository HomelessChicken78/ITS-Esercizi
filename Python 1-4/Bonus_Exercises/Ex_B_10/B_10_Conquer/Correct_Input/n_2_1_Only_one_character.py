'''r2.1 check if it contains only one character'''

def islongenough(num_sys: str) -> bool:
    if len(num_sys) <= 1:
        return False
    return True
    
if __name__ == "__main__":
    print(islongenough(input("Insert something:\n>\t")))