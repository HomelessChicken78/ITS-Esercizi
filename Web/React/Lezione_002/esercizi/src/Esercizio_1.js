import React from 'react'

// Scrivere un componente Persona che mostri a video i dati anagrafici contenuti in
// un oggetto persona. Formattare il layout con bootstrap

const Persona = (props) => {
    function persona(nome, cognome) {
        this.nome = nome
        this.cognome = cognome
    }
    let p1 = new persona(props.nome, props.cognome)
  return (
    <div>{[p1.nome, " ", p1.cognome]}</div>
  )
}

export default Persona