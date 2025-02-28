'''
Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4,
affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat.
Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci,
oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type.
Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.
'''

#Chiedi l'animale e l'habitat e mettilo minuscolo (per evitare problemi di case sensitive)
animale: str = input("Digita il nome di un animale a tuo piacimento:\n>\t")
animale = animale.lower()
habitat: str = input("Digita il suo habitat:\n>\t")
habitat = habitat.lower()
print("\n----------------------------------------------\n")

#Di che tipo di animale si tratta?
match animale:
    case "cane"|"gatto"|"cavallo"|"elefante"|"leone"|"balena"|"delfino":
        print(f"{animale.title()} appartiene alla categoria dei Mammiferi")
        animal_type = "mammifero"
    case "serpente"|"lucertola"|"tartaruga"|"coccodrillo":
        print(f"{animale.title()} appartiene alla categoria dei Rettili")
        animal_type = "rettile"
    case "aquila"|"pappagallo"|"gufo"|"falco"|"cigno"|"anatra"|"gallina"|"tacchino":
        print(f"{animale.title()} appartiene alla categoria degli Uccelli")
        animal_type = "uccello"
    case "squalo"|"trota"|"salmone"|"carpa":
        print(f"{animale.title()} appartiene alla categoria dei Pesci")
        animal_type = "pesce"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale.title()}")
        animal_type = "unknown"

#L'animale appartiene nell'habitant inserito dall'utente? Controlla l'habitat e poi controlla se l'animale appartiene in quell'habitat
animal_info = {"name" : animale, "type" : animal_type, "habitat" : habitat}
match animal_info:
    case {"name" : animale, "type" : animal_type, "habitat" : "terra"}:
        match animal_info["name"]:
            case "cane"|"gatto"|"cavallo"|"elefante"|"leone"|"serpente"|"lucertola"|"tartaruga"|"coccodrillo"|"gallina"|"tacchino":
                print(f"L'animale {animale} è un {animal_type} che può vivere sulla {habitat}")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")
    case {"name" : animale, "type" : animal_type, "habitat" : "aria"}:
        match animal_info["name"]:
            case "aquila"|"pappagallo"|"gufo"|"falco"|"cigno"|"anatra":
                print(f"L'animale {animale} è un {animal_type} che può vivere nell'{habitat}")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")
    case {"name" : animale, "type" : animal_type, "habitat" : "acqua"}:
        match animal_info["name"]:
            case "delfino"|"balena"|"tartaruga"|"coccodrillo"|"cigno"|"anatra"|"squalo"|"trota"|"salmone"|"carpa":
                print(f"L'animale {animale} è un {animal_type} che può vivere in {habitat}")
            case _:
                print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}.")
    case _:
        print("Non conosco l'habitat a cui ti riferisci")