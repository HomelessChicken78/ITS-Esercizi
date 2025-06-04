'''
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45
'''

def a() -> None:
    for i in range(1, 7):
        print(i*2, end=", ")
    print(14)

def b() -> None:
    for i in range(1, 11, 3):
        print(i, end=", ")
    print(13)

def c() -> None:
    for i in range(30, 4, -5):
        print(i, end=", ")
    print(0)

def d() -> None:
    for i in range(5, 36, 10):
        print(i, end=", ")
    print(45)

a()
b()
c()
d()