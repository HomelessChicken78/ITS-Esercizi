// Esercizio 4: Introduzione allo Stato con useState
// Obiettivo: Rendere un componente interattivo usando l'hook useState. Componente da
// creare: Termostato.js
// Istruzioni:
// 1. Crea il componente Termostato.js.
// 2. Importa useState da React.
// 3. Inizializza uno stato per la temperatura: temperatura
// 4. Visualizza la temperatura in un <h1>.
// 5. Aggiungi due bottoni, "+" e "-", che al onClick aumentino o diminuiscano la
// temperatura di 1 grado, chiamando setTemperatura.
// 6. Importa e usa <Termostato /> in App.js.

import { useState } from "react";

const Termostato = () => {
    const [Termostato, setTemperatura] = useState(20)

    const aumenta = () => {
        setTemperatura(attuale => {
            return attuale + 1
        })
    }

    const diminuisci = () => {
        setTemperatura(attuale => {
            return attuale - 1
        })
    }

    return (
        <>
            <div className="contaiter">
                <div className="row">
                    <div className="col-4"></div>
                    <div className="col-4 d-flex justify-content-center">
                        <h1 className="fw-lighter" style={{fontSize:"800%"}}>{Termostato}°C</h1>

                    </div>
                    <div className="col-4"></div>
                </div>
                <div className="row">
                    <div className="col-4"></div>
                    <div className="col-4 d-flex justify-content-center">
                        <button className="btn btn-primary" onClick={aumenta}>+</button>
                        <button className="btn btn-danger" onClick={diminuisci}>-</button>
                    </div>
                    <div className="col-4"></div>
                </div>
            </div>

        </>
    )
}

export default Termostato