'''4.2.4 Convert the various numbers in the list of integers into the correspective base'''

#rTrasform the remainders (that are written in decimal) into the characters used by the new base
def from_remainders_to_new_base(remainders: list[int], num_system: str) -> str:
    result: str = ""
    for r in remainders[::-1]:
        result += num_system[r]  #The num_system[r] converts the remainder into the new character. It is the <r>th character of the new system
    return result

if __name__ == "__main__":
    print(from_remainders_to_new_base([10, 2], "0123456789ABCDEF"))