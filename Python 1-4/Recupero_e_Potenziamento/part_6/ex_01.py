'''

Nota.
Prima di scivere la funzione in Python, è obbligatorio produrre uno schema che rappresenti ricorsivamente quanto richiesto.
Dopo aver prodotto lo schema, procedere con l'implementazione solo quando indicato dal docente.
 
Un palindromo è una stringa che non cambia anche se letta al contrario, come la stringa "radar".
Si scriva una funzione ricorsiva chiamata recursivePalindrome() che accetti in input un parametro di tipo stringa e restituisca
True se l'argomento è un palindromo e False altrimenti.

Non si tenga conto degli spazi nella stringa e non si faccia distinzione tra lettere maiuscole e minuscole.

La funzione dovrebbe considerare palindrome le seguenti stringhe:
"radar"
"Anna"
" I topi non avevano nipoti"

La funzione non dovrebbe considerare palindrome le seguenti stringhe:
"casa"
"Marta"
"Roma e Amore"

Suggerimento: usare la funzione replace() per sostituire gli spazi con una stringa vuota.
'''

def improve_string(s: str) -> str:
    s = s.lower()
    res = ""
    for char in s:
        if char != " ":
            res += char
    
    return res

def recursivePalindrome(s: str) -> bool:
    s = improve_string(s)
    if s == "":
        return True
    return s[0] == s[-1] and recursivePalindrome(s[1:-1])

print(recursivePalindrome("radar"))
print(recursivePalindrome("redar"))
print(recursivePalindrome("Anna"))
print(recursivePalindrome(" I topi non avevano nipoti"))
print(recursivePalindrome("casa"))
print(recursivePalindrome("Marta"))
print(recursivePalindrome("Roma e Amore"))