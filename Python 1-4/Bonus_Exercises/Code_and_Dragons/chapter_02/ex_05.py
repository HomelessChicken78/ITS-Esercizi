'''Prossimo: Fra pochi passi seguirai percorsi annidati nelle pagine, pronto a recuperare un valore nascosto o accettare il silenzio.

Bastone dei Sentieri
Il custode ti affida un bastone da viaggio: raggiungi ogni nodo dell'albero arcano seguendo sentieri annidati, o accetta il silenzio.
Cammina con `deep_get(d, path, default)` seguendo chiavi e indici in `path` tra dizionari e liste `d`;
restituisci il passo ma, se manca, restituisci `default`. Mantieni la firma e apri i test come portali.'''

def deep_get(d, path: list, default=None):
    current = d

    for instruction in path:
        try:
            current = current[instruction]
        except:
            return default

    return current

if __name__ == "__main__":
    print(deep_get({'a': {'b': [10, 20]}}, ["a", "b", 1], "Pop"))
    print(deep_get({'a': {'b': [10, 20]}}, ["a", "c", 1], "Pop"))

'''Il Bastone degli Itinerari Arcani ti guida sempre al nodo corretto o si ferma con prudenza.
Il Bastone dei Sentieri pulsa: i registri arcani ora rispondono a ogni ricerca.'''