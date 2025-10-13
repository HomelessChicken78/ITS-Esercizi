// 4. Selettore Pizza
// Obiettivo: Dropdown per scegliere la tua pizza preferita e mostrare la scelta
// Requisiti:
// ● Select con 4-5 tipi di pizza (Margherita, Diavola, Capricciosa...)
// ● useState per la pizza selezionata
// ● Mostra: "Hai scelto: [nome pizza]"
// Concetti: select handling, string stat

import React, { useState } from 'react'

const SelettorePizza = () => {

    const [pizza, changePizza] = useState("Margherita")

    const handleChange = (e) => {
        changePizza(e.target.value)
    }

    return (
        <>
            <div className='d-flex justify-content-center'>
                <select className='form-select w-25 border border-primary' onChange={handleChange}>
                    <option>Margherita</option>
                    <option>Diavola</option>
                    <option>4 Stagioni</option>
                    <option>Capricciosa</option>
                    <option>Boscaiola</option>
                    <option>Marinara</option>
                </select>
            </div>
            <div className='my-5'>{'\u00A0'}</div>
            <h4 className='d-flex justify-content-center mt-5'>Hai selezionato:</h4>
            <div className='d-flex justify-content-center'>
                {pizza}
            </div>
        </>
    )
}

export default SelettorePizza