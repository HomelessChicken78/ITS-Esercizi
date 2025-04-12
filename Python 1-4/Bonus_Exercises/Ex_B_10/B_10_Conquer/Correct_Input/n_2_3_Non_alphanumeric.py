'''r2.3 if there are not, check if there are non-alphanumerical characters'''

def isvalid(num_sys: str) -> bool:
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
    return True

if __name__ == "__main__":
    print(isvalid(input("Insert something:\n>\t")))