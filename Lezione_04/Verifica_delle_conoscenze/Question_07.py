'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

For example:
print(check_parentheses("()()"))
>>>True

print(check_parentheses("(()))("))
>>>False'''

def check_parentheses(expression: str) -> bool:
    remove_parenthesis: list[str] = list(expression)
    print("".join(remove_parenthesis))
    for char in expression:
        print(f"Currently checking {char}:")
        if char == '(':
            found = False

            #Try to find a ")"
            for nxt_char in remove_parenthesis:
                if nxt_char == ')':
                    remove_parenthesis.remove('(')
                    remove_parenthesis.remove(')')
                    print(f"New expression: {remove_parenthesis}")
                    found = True
                    break
            
            #If there is no ")" return false
            if found == False:
                return False
    
        if char == ')':
            print("found a )")
            return False

    if remove_parenthesis:
        print("list is not empty, returning false")
        return False

    return True
        




if __name__ ==  "__main__":
    print(check_parentheses("()()"))