'''
Esercizio 2.
 
Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe).
L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza,
oppure sono stati inseriti 30 nomi distinti. Inoltre, si deve porre il vincolo che ciascun nome sia
una stringa di lunghezza inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più
lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora
 
Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.

'''

def InseritoreNomi() -> list[str]:
    nomi: list[str] = []

    while True:
        while True:
            nome: str = input("Inserisci un nome: ")
            if nome != "" and len(nome) <= 20:
                break

        if nome in nomi or len(nomi) >= 30:
            break
        nomi.append(nome)
    
    return nomi

def LongestString(strings: list[str]) -> str:
    max: str = ""
    for s in strings:
        if len(s) > len(max):
            max = s
    
    return max

def main() -> None:
    lista_nomi: list[str] = InseritoreNomi()
    n_nomi: int = len(lista_nomi)
    longest_name: str = LongestString(lista_nomi)

    print(f"Hai inserito {n_nomi} nom{'e' if n_nomi == 1 else 'i'} distint{'o' if n_nomi == 1 else 'i'}.")
    print(f"Il più lungo è {longest_name} con {len(longest_name)} caratter{'e' if len(longest_name) == 1 else 'i'}")

main()