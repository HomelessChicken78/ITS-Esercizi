// 3. Echo Input
// Obiettivo: Quello che scrivi nell'input appare sotto in tempo reale
// Requisiti:
// ● Un campo input
// ● useState per il testo
// ● Mostra sotto l'input: "Hai scritto: [testo]"
// ● Si aggiorna mentre scrivi
// Concetti: input handling, onChange event

import React, { useState } from 'react'

const EchoInput = () => {

    const [text, changeText] = useState("")

    const handleText = (e) => {
        e.preventDefault()
        changeText(e.target.value)
    }

    return (
        <>
            <h3 className='d-flex justify-content-center'>Digita qualcosa:</h3>
            <div className='d-flex justify-content-center'>
                <input type='text' className='border border-primary rounded-pill w-50' onChange={handleText}/>
            </div>
            <h5 className='d-flex justify-content-center mt-5'>{text ? `Hai scritto: ${text}` : "Non hai scritto niente!"}</h5>
        </>
    )
}

export default EchoInput