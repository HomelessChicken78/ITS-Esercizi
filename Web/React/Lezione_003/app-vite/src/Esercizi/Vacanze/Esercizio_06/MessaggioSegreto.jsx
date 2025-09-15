// Obiettivo: Mostrare o nascondere elementi della UI in base a una condizione. Componente
// da creare: MessaggioSegreto.js
// Istruzioni:
// 1. Crea il componente MessaggioSegreto.js.
// 2. Usa useState per creare uno stato booleano mostra, inizializzato a false.
// 3. Crea un bottone che al onClick inverte il valore di mostra.
// 4. Usa l'operatore ternario per cambiare il testo del bottone.
// 5. Usa l'operatore && per mostrare un paragrafo con un "messaggio segreto" solo se
// mostra è true.
// 6. Importa e usa <MessaggioSegreto /> in App.js

import { useState } from "react"

const MessaggioSegreto = () => {
    const [mostra, setMostra] = useState(false)

    const changeShowing = () => {
        setMostra((attuale) => {
            return attuale ? false : true
        })
    }

    return (
        <div className="container">
            <div className="row">
                <div className="col-4"></div>
                <div className="col-4 d-flex justify-content-center">
                    <button className="btn btn-outline-primary btn-sm rounded-pill" onClick={changeShowing}>{mostra ? "Nascondi ▴" : "Mostra ▾"}</button>
                </div>
                <div className="col-4"></div>
            </div>

            <div className="row">
                <div className="col-4"></div>
                <div className="col-4 d-flex justify-content-center">
                    {mostra && <p className="my-4">messaggio segreto🤫</p>}
                </div>
                <div className="col-4"></div>
            </div>
        </div>
    )
}

export default MessaggioSegreto