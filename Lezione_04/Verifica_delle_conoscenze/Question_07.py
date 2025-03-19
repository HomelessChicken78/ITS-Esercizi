'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

For example:
print(check_parentheses("()()"))
>>>True

print(check_parentheses("(()))("))
>>>False'''

def check_parentheses(expression: str) -> bool:
    parentheses = 0
    
    #Check each character. If it is a '(' the counter increases, else, if it is a ')' it decreases
    for char in expression:
        if char == "(":
            parentheses += 1
        elif char == ")":
            #If there was an open parenthesis before:
            if parentheses >= 1:
                parentheses -= 1

            #This is to avoid that the program may find in future closed parenthesis
            else:
                 return False
    
    #If there is no disparity between "(" and ")" return True. Else something does not add up and you return False
    if parentheses == 0:
        return True
    else:
        return False
        




if __name__ ==  "__main__":
 	print(check_parentheses("((()))"))