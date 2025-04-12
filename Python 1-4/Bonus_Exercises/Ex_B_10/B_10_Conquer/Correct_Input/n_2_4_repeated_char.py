'''r2.4 if there are not, check if any character is repeated'''

def isrepeated(num_sys: str) -> bool:
    duplicate: str = num_sys  #This is a duplicate of the original string which can be modified freely without messing with the while loop
    i: int = 0

    while i < len(num_sys):  #Check each index in the string one by one
        #If the character appears again in future return False
        if num_sys[i] in num_sys[i+1:]:
            return True
        i += 1
        return False

if __name__ == "__main__":
    print(isrepeated(input("Insert something:\n>\t")))