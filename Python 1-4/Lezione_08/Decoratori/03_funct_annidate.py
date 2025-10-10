# Una funzione può contenere al suo interno altre funzioni

def parent(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"

    if num == 1:
        return first_child
    else:
        return second_child
    
my_new_funct = parent(1)
print(my_new_funct) # Memoria
print(my_new_funct())

print()

my_new_funct = parent(2)
print(my_new_funct) # Memoria
print(my_new_funct())

# N.B.: first_child e second_child nascono e muoiono all'interno di parent. Ciò significa che se togliessimo il return, una volta che parent finisce
# non avremo più accesso a queste funzioni

def reachable() -> None:
    def unreachable():
        print("If you manage to call me, you cheated")
    return "I forgot to return unreachable"

# reachable()() # errore in quanto reachable non ritorna nulla
# reachable().unreachable() # Errore in quanto la dot notation cerca l'attributo unreachable all'interno di "I forgot to return unreachable", che non esiste