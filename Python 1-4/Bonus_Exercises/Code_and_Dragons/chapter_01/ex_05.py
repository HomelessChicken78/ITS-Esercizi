'''Prossimo: La soglia finale delle liste chiede di fondere ogni trama in un'unica linea.

Trama Lineare
Prima di continuare, fonde le fibre raccolte in un'unica trama lineare.
Realizza l'intreccio con `flatten_once(nested)`, che appiattisce di un livello una lista di liste concatenando le sottoliste.
Mantieni la firma e verifica che i test scorrano senza nodi.'''

def flatten_once(nested: list[list[int]]) -> list[int]:
    new_list: list[int] = []
    
    for lst in nested:
        for el in lst:
            new_list.append(el)

    return new_list

'''La Trama Lineare intreccia ogni fibra della Biblioteca: capitolo pronto.
La Biblioteca degli Specchi canta di nuovo: hai intrecciato ogni frammento in una trama unica.'''