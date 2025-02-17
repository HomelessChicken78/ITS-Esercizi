'''Exercise 4 - Solution I'''
'''number = input('insert a number')
print(f'{number[0]}\n{number[1]}\n{number[2]}\n{number[3]}\n')'''

'''Exercise 4 - Solution II'''
number = input('insert a number: ')
while (len(number) != 4):
    number = input('Incorect number, insert a number: ')
i = 0
while (i < 4):
    print(f'{number[i]}')
    i += 1