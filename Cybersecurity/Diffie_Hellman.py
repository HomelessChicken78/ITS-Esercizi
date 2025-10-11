'''
ALGORITMO DI SCAMBIO DI CHIAVE DIFFIE-HELLMAN

Implementare in maniera semplice un programma che simuli lo SCAMBIO DI CHIAVE Diffie-Hellman, nel quale:

        1. VENGONO SCELTI DUE PARAMETRI PUBBLICI: un NUMERO PRIMO p e un GENERATORE g
        2. ALICE E BOB SCELGONO SEGRETI CASUALI a e b
        3. CALCOLANO LE LORO CHIAVI PUBBLICHE A = g^a mod p e B = g^b mod p
        4. SCAMBIANO LE CHIAVI PUBBLICHE
        5. CALCOLANO LA CHIAVE SEGRETA CONDIVISA: K = B^a mod p = A^b mod p
        6. VERIFICANO CHE LE DUE CHIAVI CONDIVISE SIANO UGUALI

Se l'agoritmo funziona correttamente dovrà dare esito Positivo, mai negativo dato che -> gli esponenti e moltiplicazione modulo p sono commutativi.
In caso negativo, c'è qualcosa che non va con il calcolo degli esponenti e la moltlipicazionende del modulo p e NON saranno commutativi.

'''

from random import randint

p: int = 17
g: int = randint(0, 9999999999)

a: int = randint(0, 9999999999)
b: int = randint(0, 9999999999)

A: int = pow(g, a, p)
B: int = pow(g, b, p)

# Scambio chiavi

A2: int = pow(B, a, p)
B2: int = pow(A, b, p)

print(A2 == B2)