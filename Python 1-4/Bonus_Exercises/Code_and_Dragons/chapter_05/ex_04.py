'''Prossimo: Fra pochi passi le mura ti chiederanno di elencare ogni gemma prima fino alla soglia.

Fessure Prime
Le mura hanno incavi per gemme **prime**: devi elencarle tutte. Forja `primes_up_to(n)` per restituire la lista dei numeri primi **≤ n**
in ordine crescente; se `n` < `2`, ritorna `[]`. Mantieni la firma e apri i test.'''

def primes_up_to(n: int) -> list[int]:
    primes: list[int] = []

    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    
    return primes

def is_prime(n) -> bool:
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    for num in range(3, n, 2):
        if n % num == 0:
            return False
    
    return True

print(primes_up_to(100))

'''Hai contato quanti passi servono per superare il portale ritmico.'''