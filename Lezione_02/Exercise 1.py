'''Exercise 1
Si scriva un programma che dimostri la natura approssimativa dei numeri in virgola mobile effettuando le seguenti attività:

    • Memorizzare un numero in virgola mobile nella variabile x.
    • Calcolare 1.0/x memorizzare il risultato nella variabile y.
    • Visualizzare il valore di x, y e il prodotto tra x e y.
    • Sottrarre x dal prodotto tra x e y e mostrarne il risultato.
'''
x = float(input('insert a number: '))
y = 1.0 / x
print(f'The value of x is: {x}\nThe value of y is: {y}\ny multiplied by x: {x*y}\nlast result:{(x*y)-x}')