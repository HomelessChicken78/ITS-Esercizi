def recursiveCountdown(n: int) -> None:
    if n < 0:  #Casi di base
        print("Errore")
    elif n == 0:  #Casi di interruzione
        print(0)
    else:
        print(n)
        recursiveCountdown(n-1)

recursiveCountdown(-5)
print("-------------------------------")
recursiveCountdown(5)