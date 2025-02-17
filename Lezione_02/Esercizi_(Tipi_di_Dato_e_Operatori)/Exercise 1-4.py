'''Exercise 1-4
Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

2
0
2
4
'''
'''Solution I
number = input('insert a number')
print(f'{number[0]}\n{number[1]}\n{number[2]}\n{number[3]}\n')'''

'''Solution II'''
number = input('insert a number: ')
while (len(number) != 4):
    number = input('Incorect number, insert a number: ')
i = 0
while (i < 4):
    print(f'{number[i]}')
    i += 1