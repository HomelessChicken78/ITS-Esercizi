'''Esercizio 3C-8. Scrivere un programma in Python che legga una frase di una riga e mostri una delle seguenti risposte:
- "Si" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è pari;
- "No" -> se la frase termina con un punto interrogativo (?) ed il numero dei caratteri è dispari;
- "Wow!" -> se la frase termina con un punto esclamativo (!)
- "Tu dici" seguito dalla frase inserita racchiusa tra doppi apici in tutti gli altri casi.

Expected Output:

frase: di essere bellissimo
Output: Tu dici "di essere bellissimo"
'''

#Input
phrase: str = input("Inserire una frase: \n>\t")

#Verifica se l'ultima lettera della frase è un "!", un "?" o nessuno dei due
match phrase[-1]:
    case "?":
        #Pari
        if len(phrase) % 2 == 0: 
            print("Si")
        #Dispari
        else:
            print("No")
    case "!":
        print("Wow")
    case _:
        print(f"Tu dici \"{phrase}\"")