'''Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51'''

def print_seq(): 
    
    print("Sequenza a):")
    for a in range(1, 8):
        print(a)
    print()

    print("Sequenza b):")
    for b in range(3, 24, 5):
        print(b)
    print()

    print("Sequenza c):")
    for c in range(20, -11, -6):
        print(c)
    print()

    print("Sequenza d):")
    for b in range(19, 52, 8):
        print(b)
    print()
    
    return
