from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s: str, key: int) -> str:
    res: str = ""  # This is the result that will be returned

    # Check all letters in the string
    for letter in s:
        if letter in ascii_lowercase:
            alphabet_index: int = ascii_lowercase.index(letter)  # Find what position that the letter has in the alphabet
            # Append to the result the letter that is {key} positions ahead. Take into consideration if it goes out of range
            if alphabet_index + key > 25:
                res += ascii_lowercase[(alphabet_index + key)%26]
            else:
                res += ascii_lowercase[alphabet_index + key]

        elif letter in ascii_uppercase:
            alphabet_index: int = ascii_uppercase.index(letter)  # Find what position that the letter has in the alphabet
            # Append to the result the letter that is {key} positions ahead. Take into consideration if it goes out of range
            if alphabet_index + key > 25:
                res += ascii_uppercase[(alphabet_index + key)%26]
            else:
                res += ascii_uppercase[alphabet_index + key]

        else:
            res += letter

    return res

def caesar_cypher_decrypt(s: str, key: int) -> str:
    res: str = ""  # This is the result that will be returned

    # Check all letters in the string
    for letter in s:
        if letter in ascii_lowercase:
            alphabet_index: int = ascii_lowercase.index(letter)  # Find what position that the letter has in the alphabet
            # Append to the result the letter that is {key} positions ahead. Take into consideration if it goes out of range
            if alphabet_index - key < 0:
                res += ascii_lowercase[(alphabet_index - key)%26]
            else:
                res += ascii_lowercase[alphabet_index - key]

        elif letter in ascii_uppercase:
            alphabet_index: int = ascii_uppercase.index(letter)  # Find what position that the letter has in the alphabet
            # Append to the result the letter that is {key} positions ahead. Take into consideration if it goes out of range
            if alphabet_index - key < 0:
                res += ascii_uppercase[(alphabet_index - key)%26]
            else:
                res += ascii_uppercase[alphabet_index - key]

        else:
            res += letter
    
    return res

if __name__ == "__main__":
    print(caesar_cypher_encrypt("ciao", 2))  #ekcq
    print(caesar_cypher_decrypt("ekcq", 2))  #ciao
    print(caesar_cypher_encrypt("ciao come stai", 2))  #ekcq eqog uvck
    print(caesar_cypher_encrypt("CIAO COME STAI", 2))  #EKCQ EQOG UVCK
    print(caesar_cypher_decrypt("EKCQ EQOG UVCK", 2))  #CIAO COME STAI
    print(caesar_cypher_encrypt("C!4O C0m3 st4I?", 2))  #E!4Q E0o3 uv4K?
    print(caesar_cypher_decrypt("E!4Q E0o3 uv4K?", 2))  #C!4O C0m3 st4I?
    print(caesar_cypher_encrypt("zz ZZ", 2))  #bb BB
    print(caesar_cypher_decrypt("bb BB", 2))  #zz ZZ
    print(caesar_cypher_encrypt("a", 28))