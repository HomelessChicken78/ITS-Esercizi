'''Password Validation:  Write a function validate_password(password) that checks whether a password meets
the following criteria: Minimum length of 20 characters, At least three uppercase letters, At least four special
characters (non-alphanumeric). If the password is valid, the function should return True. If the password is
invalid, the function should raise a built-in exception (e.g., ValueError) with a message indicating which criteria
were not met.'''


#Return the number of uppercase letters
def  uppercaseNumber(string: str) -> bool:
    i: int = 0
    uppercases: list[str] = [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y",
        "Z"
    ]
    for char in string:
        if char in uppercases:
            i += 1
    return i

#Return the number of special characters
def specialCharNumber(string: str) -> bool:
    i: int = 0
    specialChar: list[str] = [
        "!", "?", ".",
        ",", ";", ":",
        "-", "_", "+"
    ]
    for char in string:
        if char in specialChar:
            i += 1
    return i

def validate_password(password: str) -> bool:
    if len(password) >= 20 and uppercaseNumber(password) >= 3 and specialCharNumber(password) >= 4:
        return True
    else:
        raise ValueError("The criteria were not met :(")