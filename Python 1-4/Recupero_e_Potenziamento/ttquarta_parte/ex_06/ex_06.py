'''
In biologia molecolare, le molecole di DNA possono essere viste come stringhe sull’alfabeto dei nucleotidi
A = adenina, C = citosina, G =guanina, T = timina.

Ad esempio: DNA: CAGCTGATCGATGCTAGCCTG.

Scrivere un programma in linguaggio Python che legge dall’utente due stringhe s1 e s2 corripondenti a frammenti di
DNA e verifica se s2 puo' essere sovrapposta su s1 in modo che una parte iniziale (prefisso) di s2 coincida con
una parte finale (suffisso) di s1.
 
Il programma dovra' dare la lunghezza della massima sovrapposizione (0 se non si possono sovrapporre).
 
Ad esempio, se l’utente ha inserito:
s1= CAGCTGATCGATGCTAGCCTG
s2= AGCCTGTTGCACCTAGA

Le due stringhe si sovrappongono come segue:
CAGCTGATCGATGCTAGCCTG
        CGATGCTAGCCTGTTGCACCTAGA

Il programma dovra' quindi stampare in output:

    le stringhe sovrapposte come nell'esempio.

    La massima lunghezza di sovrapposizione e' 6.

NOTA1:
il programma dovra' anche verificare la correttezza dell’input, ovvero le stringhe inserite dall’utente devono essere
effettivamente frammenti di DNA.
Suggerimento: scrivere una funzione isDNA() che, data in input una sequenza, restituisca True se la sequenza passata è
una valida sequenza del DNA formata dai soli caratteri A, C, G o T, e che restituisca False altirmenti.
Può essere utile usare una regex.

Nota2: trovare una soluzione che eviti di scrivere codice replicato per inizializzare le sequenze s1 e s2.

Infine, verificare le seguenti coppie di frammenti di DNA:
- s1= TTGACCAGGTCA
- s2= AACCGGTTAA
La massima lunghezza è 1

- s1= GGTACCGTGA
- s2= CGTGAACCTT
La massima lunghezza è 5

- s1= AAGCTTACG
- s2= ACGTTCGA
La massima lunghezza è 3

- s1= TTACGAGTACGCTAGT
- s2= ACGCTAGTCCGA
La massima lunghezza è 8
'''

def overlapping(s1: str, s2: str) -> tuple[str, int]:
    count: int = 0
    nuova_stringa: str = ""

    for char in s1:
        if char == s2[count]:
            count += 1

            nuova_stringa += char

        elif char == s2[0]:
            count = 1
            nuova_stringa = char

        else:
            count = 0
            nuova_stringa = ""
    
    if count > 0:
        return nuova_stringa, count
    else:
        return "", 0

# print(overlapping("asABCDE", "ABCDEjadioufwgt"))
print(overlapping("GGTACCGTGA", "CGTGAACCTT"))

a, b = overlapping("A", "A")

def isDNA(s: str) -> bool:
    from re import fullmatch
    s = s.upper()

    if fullmatch(r"^[ACGT]+$", s):
        return True
    return False

def overlapping_dna() -> None:
    s1: str = input("Inserire la prima stringa\n->\t")
    s2: str = input("Inserire la seconda stringa\n->\t")

    if isDNA(s1) and isDNA(s2):
        overlapping_str: str
        matching_char: int

        overlapping_str, matching_char = overlapping(s1, s2)
        print(f"{overlapping_str}\nLa massima lunghezza è {matching_char}")
    
# overlapping_dna()