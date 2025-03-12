'''2.4 if there are not, check if any character is repeated'''

def isrepeated(num_sys: str) -> bool:
    duplicate: str = num_sys  #This is a duplicate of the original string which can be modified freely without messing with the while loop
    i: int = 0

    while i < len(num_sys):
        #Update the list with the characters in the string which haven't been checked yet
        #duplicate = duplicate[1:]  #Remove the first character from the string
        
        #If the number appears again in future (aka if it is present in the duplicate of the string):
        if num_sys[i] in num_sys[i+1:]:
            return False
        i += 1

if __name__ == "__main__":
    print(isrepeated(input("Insert something:\n>\t")))