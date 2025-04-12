'''4. Convert the number into the new base provided by the user'''

def base_conversion(decimal_number: int, new_base: int) -> list[int]:
    remainders: list[int] = []

    #Calculate the list of remainders. These will then be used for the conversion to the new base system
    while decimal_number > 0:
        remainders.append(decimal_number % new_base)
        decimal_number //= new_base  #Update the decimal number by dividing it
    return remainders

if __name__ == "__main__":
    print(base_conversion(42, 16))