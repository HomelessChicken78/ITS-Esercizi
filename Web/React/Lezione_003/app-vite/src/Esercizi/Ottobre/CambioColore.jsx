// 2. Cambio Colore Testo
// Obiettivo: 3 bottoni (Rosso, Verde, Blu) che cambiano il colore di un testo
// Requisiti:
// ● Un titolo "Ciao Mondo!"
// ● 3 bottoni colorati
// ● useState per memorizzare il colore scelto
// ● Il testo cambia colore quando clicchi un bottone
// Concetti: string state, inline styles

import React, { useState } from 'react'

const CambioColore = () => {
    const [color, changeColor] = useState("red")

    return (
        <>
            <h2 className='d-flex justify-content-center my-5' style={{color : color}}>
                Ciao Mondo!
            </h2>
            <div className='d-flex justify-content-center my-5'>
                <button className='btn btn-danger w-25 mx-2' onClick={() => changeColor('red')}>Rosso</button>
                <button className='btn btn-success w-25 mx-2' onClick={() => changeColor('green')}>Verde</button>
                <button className='btn btn-primary w-25 mx-2' onClick={() => changeColor('blue')}>Blu</button>
            </div>
        </>
    )
}

export default CambioColore