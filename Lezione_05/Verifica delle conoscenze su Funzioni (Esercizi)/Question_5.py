'''Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.

Un fattore primo di n è un numero primo che divide esattamente n (cioè senza resto), e la
cui moltiplicazione in sequenza restituisce n. Un numero può avere lo stesso fattore primo più volte.

Cosa sono i fattori primi?

I fattori primi di un numero sono numeri primi che, moltiplicati tra loro, danno come risultato proprio quel numero.


🔹 Esempio:
Il numero 60 si può scomporre in: 2 * 2 * 3 * 5 → cioè: 2² * 3 * 5


🔎 Suggerimento:
Prova a pensare a come potresti "smontare" un numero dividendolo più volte, iniziando dal
numero primo più piccolo possibile. Cosa succede ogni volta che la divisione ha resto 0? E
cosa potresti fare quando non lo è più?

For example:
print(prime_factors(4))
>>>[2, 2]

print(prime_factors(60))
>>>[2, 2, 3, 5]'''

#This function checks whether the number is prime or not
def is_prime(n: int) -> bool:
    i = 2
    while i < n+1 // 2:
        if n % i == 0:
            return False
        i += 1

    return True

def prime_factors(n: int) -> list[int]:
    primes: list[int] = [
        2, 3, 5, 7, 11, 13,
        17, 19, 23, 29, 31,
        37, 41, 43, 47, 53,
        59, 61, 67, 71, 73,
        79, 83, 89, 97, 271, 3541, 9091, 27961
    ]

    prime_factors: list[int] = []

    while n > 1:

        #Check whether it is a prime number
        if is_prime(n):
            prime_factors.append(n)
            n = 1

        #Check each prime number
        for prime in primes:

            #If the prime number is a prime factor, append it to the list and divide the number by that prime factor
            if n % prime == 0:
                prime_factors.append(prime)
                n //= prime
                break
    
    return sorted(prime_factors)
        
#Test cases
if __name__ == "__main__":
    print(prime_factors(4))
    print(prime_factors(60))
    print(prime_factors(99999999999999999999))