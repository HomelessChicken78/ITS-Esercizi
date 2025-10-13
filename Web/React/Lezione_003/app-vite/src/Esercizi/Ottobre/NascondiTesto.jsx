// 1. Mostra/Nascondi Testo
// Obiettivo: Un bottone che mostra/nasconde un paragrafo di testo
// Requisiti:
// ● Un bottone con scritto "Mostra" o "Nascondi"
// ● useState con valore booleano (true/false)
// ● Quando clicchi, il testo appare o scompare
// Concetti: boolean state, conditional rendering

import React, { useState } from 'react'

const NascondiTesto = () => {
    const [showed, setShow] = useState(false)

    const toggleShow = () => {
        setShow(!showed)
    }

    return (
        <>
            <div className='d-flex justify-content-center'>
                <button
                    onClick={() => toggleShow()}
                    className='btn btn-primary rounded-pill'
                >
                    {showed ? "Nascondi" : "Mostra"}
                </button>
            </div>
            <div className='d-flex justify-content-center'>
                {showed ?
                    <div className='border border-secondary rounded p-4 my-2'>Ecco un messaggio!</div>
                    :
                    ""}
            </div>
        </>
    )
}

export default NascondiTesto