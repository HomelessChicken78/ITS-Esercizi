from typing import Callable, Any

def cronometro(funct: Callable) -> Callable:
    def wrapper(*args) -> Any:
        from time import time

        start = time()
        funct(*args)
        print(f"Tempo richiesto: {time() - start}")
    
    return wrapper

@cronometro
def hi(num: int) -> None:
    c = 0

    for _ in range(0, 115035170):
        c += num
    
    print(c)

# hi = cronometro(hi) # -> Se non usi @cronometro sopra a def hi
hi(2)




