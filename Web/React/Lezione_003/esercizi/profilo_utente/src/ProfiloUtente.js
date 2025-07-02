import React from 'react'

const ProfiloUtente = (props) => {


  let person = props.utente
  return (
    <>
        <div className="card h-100">
            <div className="card-header text-center">
                Titolo o icona 
            </div>
            <div className="card-body text-center">
                <h5>{person.nome} {person.cognome} <span className="badge bg-secondary">{person.eta} anni</span></h5>
                <div>Lavora come {person.professione.toLowerCase()}</div>
                contatta: <span className="font-monospace fw-lighter">{person.email}</span>
            </div>
            <div className="card-footer text-center">
                <button type="button" className="btn btn-primary"onClick={() => {alert(person.nome)}}>
                    Clicca qui
                </button>
            </div>
        
        </div>
    </>
  )
}

export default ProfiloUtente