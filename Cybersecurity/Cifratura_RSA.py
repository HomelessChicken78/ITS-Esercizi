'''
Esercizio per casa
⚫ Estrarre n (modulus), e (public exponent), d (private exponent) dal file PEM (chiave
pubblica)
⚫ Convertire n, e, d in numeri interi
• Esempio: n: togliere i «:», togliere «\n», togliere « « e poi con la funzione int(s, 16) => numero intero
• Prendete il messaggio e convertitelo in numero intero
• Poi eseguite
• Cifra: pow(M, e, n) => C (messaggio cifrato)
• Decifra: pow(C, d, n) => M
• Riconvertire M in stringa e verificare se avete decifrato correttamente
'''
publicExponent = 3
privateExponent = """
    25:08:eb:da:de:ac:26:05:69:f8:12:4e:66:1a:cb:
    a8:e2:9a:b9:7f:7a:da:88:5c:97:23:b3:2d:4b:12:
    04:52:53:7d:d8:e0:6d:d9:87:18:94:6c:ba:af:ac:
    93:52:70:ca:76:46:c0:d1:db:32:6e:ef:8f:5c:91:
    6e:39:f5:6d:c5:82:78:7e:e3:35:1e:1f:65:d8:93:
    a9:0e:28:b3:d8:f5:41:39:2a:63:6c:db:55:d4:17:
    23:0e:c4:e1:da:41:22:6f:63:5e:cc:4b:5d:af:95:
    a2:77:22:b1:ef:b9:3d:9e:dd:6c:de:39:61:aa:ad:
    a1:e3:f6:4c:6b:c9:42:b3:31:65:20:d4:58:3d:22:
    bf:c2:28:e9:eb:2e:1d:a8:49:f4:17:2d:c5:46:1e:
    4c:bf:e0:b4:fc:0a:01:c6:26:8b:e7:4b:14:b1:9b:
    7b:f7:5e:a8:cd:c0:1f:2e:29:89:48:34:74:52:2b:
    a1:ea:9b:f5:db:68:90:35:42:22:65:d8:90:60:20:
    ce:ce:e4:d5:39:ab:50:98:73:98:b7:3f:56:f7:09:
    23:51:c7:1d:f8:0e:b2:74:a8:67:92:ba:9a:d8:36:
    42:34:dd:2e:95:6a:f5:5f:b6:87:57:8d:aa:68:fc:
    e7:63:56:60:47:3d:16:79:d9:44:89:d7:4b:48:1c:
    1b"""
prime1 = """
    00:e1:20:e4:10:f3:f5:76:fa:bd:27:53:8a:cc:06:
    4c:ce:42:78:96:da:d6:3c:4d:db:8f:a0:29:49:95:
    b5:10:1a:ac:7c:0d:b7:36:dd:2a:00:8c:c6:07:e7:
    63:43:ec:1d:26:65:31:e4:d6:3c:87:66:1b:72:e6:
    95:4c:06:9d:b1:18:a1:d8:59:a0:92:44:ff:c6:7e:
    3a:c7:c4:6b:ce:5e:6e:7a:40:be:ac:28:c5:62:93:
    68:88:28:f1:37:bc:92:d2:a7:5f:4b:7d:2e:9b:07:
    bb:0f:bc:28:57:07:98:8e:c7:d7:d7:60:d7:b4:36:
    c8:41:67:32:0f:df:ab:a2:95"""
prime2 = """
    00:fc:ae:26:f8:9d:a9:39:ef:a4:40:09:8e:4c:2a:
    7c:3c:72:ac:43:34:56:d5:8b:4a:90:23:eb:33:cd:
    4f:fa:15:80:95:e2:37:ad:9a:1e:04:58:2e:ed:ab:
    a7:26:c1:57:70:51:6f:11:95:41:b5:d4:e0:b1:2d:
    39:e5:21:4b:29:ec:e6:2d:d2:95:35:56:95:aa:83:
    ca:46:5d:32:e8:99:30:1c:30:f4:0c:74:7e:a6:03:
    7c:ee:05:25:d7:4c:af:7e:9a:dc:76:f9:dc:d8:e7:
    3e:37:67:b4:82:26:63:6d:27:45:5e:42:61:9f:ae:
    85:55:a1:98:cc:70:07:41:09"""

def hex_to_int(s: str) -> int:
    new_s: str = s.replace(":", "")
    new_s = new_s.replace(" ", "")
    new_s = new_s.replace("\n", "")
    
    return int(new_s, 16)

def message_to_int(m: str) -> int:
        asciified: list[int] = [ord(char) for char in m]
        res: int = 0
        count: int = 0

        for num in asciified[::-1]:
            res += num*(256**count)
            count += 1

        return res

'''Oppure:
def stringToNumber(string: str) -> int:

    tot = 0
    for char in string:
        tot = (tot << 8) | ord(char)

    return tot
    '''

def int_to_message(big_number: int) -> str:
    asciified: list[int] = []
    num = big_number

    while num > 0:
        asciified.append(num % 256)
        num //= 256
    
    return [chr(n) for n in asciified][::-1]

def encrypt_RSA(m: str, p: str, q: str, e: int) -> int:
    p = hex_to_int(p)
    q = hex_to_int(q)
    M = message_to_int(m)

    n: int = p * q
    return pow(M, e, n)

def decrypt_RSA(C: int, p: str, q: str, d: str):
    p = hex_to_int(p)
    q = hex_to_int(q)
    d = hex_to_int(d)

    n: int = p * q
    return ''.join(int_to_message(pow(C, d, n)))

encrypted: int = encrypt_RSA("Ciao", prime1, prime2, publicExponent)
print(encrypted)
decrypted: int = decrypt_RSA(encrypted, prime1, prime2, privateExponent)
print(decrypted)