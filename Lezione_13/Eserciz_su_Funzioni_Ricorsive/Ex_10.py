'''
Esercizio 10.

Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa e restituisca il risultato sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator, la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".
'''

def charDuplicator(string: str, duplicator: int = 2):
    if len(string) == 0:
        return string
    else:
        return string[0]*duplicator + charDuplicator(string[1:])
    
if __name__ == "__main__":
    print(charDuplicator("libro"))