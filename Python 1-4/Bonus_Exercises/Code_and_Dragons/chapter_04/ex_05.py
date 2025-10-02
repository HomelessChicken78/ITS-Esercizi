'''Prossimo: Al culmine del santuario ti sarà chiesto del santuario ti chiedera memoria arcana per percorrere il labirinto di Fibonacci.

Al cuore del santuario si snoda il labirinto di Fibonacci: evita di ripetere i passi già tracciati invocando `fib_memo(n)`,
che calcola l'ennesimo numero della sequenza con memoria per non rifare i calcoli. Mantieni la firma e lascia che i test si aprano.'''

def fib_memo(n) -> int:
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    sequence: list[int] = [0, 1]
    i: int = 2
    while i <= n:
        sequence.append(sequence[0]+sequence[1])
        sequence.pop(0)
        i += 1
    return sequence[1]

'''Hai memorizzato il labirinto di Fibonacci: la sequenza risponde al tuo richiamo. Hai risolto il Labirinto di Fibonacci: la sequenza custodisce i tuoi incanti.'''