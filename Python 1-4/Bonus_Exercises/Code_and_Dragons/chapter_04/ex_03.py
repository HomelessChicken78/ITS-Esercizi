'''Prossimo: Nella stanza successiva, la sfida intreccera funzioni per creare un unico canale di potere.

Canale Intrecciato
I diagrammi intrecciano formule e chiedono un canale dove un incanto scorra dentro l'altro: costruisci `compose(f, g)`,
restituendo una funzione che, chiamata con `x`, calcola `g(x)` e poi `f` del risultato. Mantieni la firma e placa i test.'''

def compose(f, g):
    def h(x):
        return f(g(x))
    return h

'''Hai intessuto un canale arcano dove un incanto scorre dentro l'altro.'''