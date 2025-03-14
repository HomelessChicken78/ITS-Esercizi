'''2. check if the input is correct'''

from B_10_Conquer.Correct_Input.2_1_Only_one_character

def check_input(num_sys: str) -> bool:
    if len(num_sys) <= 1:
        return False
    elif "+" in num_sys or "-" in num_sys:
        return False
    valid_char: list = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]
    for char in num_sys:
        if char not in valid_char:
            return False

if __name__ == "__main__":
    print(check_input(input("Insert something:\n>\t")))