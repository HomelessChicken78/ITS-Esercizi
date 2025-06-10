'''
Validazione di un Indirizzo IPv4
Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.
Requisiti:
● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.
● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].
Esempi:
is_valid_ipv4("192.168.0.1") # True
is_valid_ipv4("255.255.255.255") # True
is_valid_ipv4("256.100.10.1") # False (256 è fuori range)
is_valid_ipv4("192.168.1") # False (solo 3 parti)
is_valid_ipv4("192.168.1.a") # False (parte non numerica)
'''

def is_valid_ipv4(address: str) -> bool:
    # Count the number of "."
    dot: int = 0
    for char in address:
        if char == ".":
            dot += 1
    
    # Check if they are exactly 3
    if dot != 3:
        return False

    numbers: list[str] = address.split(".")

    for char in numbers:
        # Check if they all are numbers
        if not char.isdigit():
            return False
        
        # Check if they all are in the range
        if int(char) < 0 or int(char) > 255:
            return False

    return True


if __name__ == "__main__":
    print(is_valid_ipv4("192.168.0.1")) # True
    print(is_valid_ipv4("255.255.255.255")) # True
    print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
    print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
    print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)