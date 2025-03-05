'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

def check_lenght(phrase: str) -> None:
    if len(phrase) > 10:
        print(f"The phrase you provided is longer than 10 charachers")
    elif len(phrase) < 10:
        print(f"The phrase you provided is shorter than 10 charachers")
    else:
        print(f"The phrase you provided contains exactly 10 charachers")

'''Output Check
check_lenght("Hungry")
check_lenght("The cake is a lie!")
check_lenght("Chimpanzee")
'''