import React, { useState } from 'react'

const Persona = () => {
  let [persona, updatePerson] = useState({
    nome : "Cristiano",
    cognome : "Coccia",
    eta : 21
  })

  let compleanno = () => {
    let anni = persona.eta + 1;
    updatePerson({
        ...persona, // prova a commentare questa linea e vedi che succede
        eta : anni
    })
  }

  return (
    <>
        <div>{persona.nome} {persona.cognome}, {persona.eta} anni</div>
        <button onClick={compleanno}>Compie compleanno</button>
    </>
  )
}

export default Persona