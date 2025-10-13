// sercizio 7: Effetti Collaterali con useEffect
// Obiettivo: Usare useEffect per eseguire un'azione (un "effetto collaterale") in risposta a
// un cambiamento di stato. Componente da creare: AggiornaTitolo.js
// Istruzioni:
// 1. Crea il componente AggiornaTitolo.js.
// 2. Crea un campo di input controllato (come nell'Esercizio 5) con una variabile di stato
// chiamata nome.
// 3. Importa l'hook useEffect da React.
// 4. Aggiungi un useEffect che si attivi ogni volta che il valore di nome cambia. Per
// farlo, dovrai usare l'array delle dipendenze: useEffect(() => { ... },
// [nome]);.
// 5. All'interno della funzione useEffect, aggiorna il titolo della scheda del browser. Se
// il campo nome è vuoto, il titolo sarà "Benvenuto!", altrimenti document.title =
// \Ciao, ${nome}!`;`.
// 6. Quando il componente viene montato, il titolo dovrebbe essere "Benvenuto!".
// Appena l'utente inizia a scrivere, il titolo della pagina si aggiornerà in tempo reale.
// 7. Importa e usa <AggiornaTitolo /> in App.js.

import { useEffect, useState } from "react"

const AggiornaTitolo = () => {
    const [nome, setNome] = useState('');

    const handleInput = (e) => {
        setNome(e.target.value)
    };

    useEffect(() => {
        document.title = nome ? `Ciao, ${nome}!` : "Benvenuto!"
    }, [nome])

    return (
        <div className="container my-5">
            <div className="row">
                <div className="col-4"></div>
                <div className="col-4 d-flex justify-content-center">
                    <input className="border-secondary rounded p-1" placeholder="Inserire il tuo nome qui..." type="text" onChange={handleInput} />
                </div>
                <div className="col-4"></div>
            </div>
        </div>
    )
}

export default AggiornaTitolo