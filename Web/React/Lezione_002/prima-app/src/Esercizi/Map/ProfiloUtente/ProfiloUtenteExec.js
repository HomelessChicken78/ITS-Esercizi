import React from 'react'
import ProfiloUtente from './ProfiloUtente'

const persone = [{
    id: 1,
    nome: "Alice",
    cognome: "Amato",
    eta: 21,
    professione: "Studente",
    email: "alice.amato@example.com"
}, {
    id: 2,
    nome: "Bob",
    cognome: "Bianchi",
    eta: 41,
    professione: "Idraulico",
    email: "bob.bianchi@example.com"
}, {
    id: 3,
    nome: "Charley",
    cognome: "Conti",
    eta: 24,
    professione: "Cameriera",
    email: "charley.conti@example.com"
}, {
    id: 4,
    nome: "David",
    cognome: "De Luca",
    eta: 36,
    professione: "Dentista",
    email: "david.deluca@example.com"
}, {
    id: 5,
    nome: "Eve",
    cognome: "Evangelista",
    eta: 38,
    professione: "Elettricista",
    email: "eve.evangelista@example.com"
}]

let dividi = (arr) => {
    let res = []
    for (let i = 0; i < arr.length; i += 3) {
        res.push(arr.slice(i, i + 3))
    }

    return res
}

const ProfiloUtenteExec = () => {
    let splitted_persone = dividi(persone)
    // console.log("res array:", splitted_persone[0], "\n", splitted_persone[1])

    return (
        <>
            <div className="container">
                {splitted_persone.map((riga, indice_riga) => {
                    return (
                        <div className="row" key={indice_riga}>
                            {riga.map((pers) => {
                                return (
                                    <div className="col-md-4" key={pers.id}>
                                        <ProfiloUtente utente={pers} />
                                    </div>
                                )
                            })}
                        </div>
                    )
                })}
            </div>
        </>
    );
}

export default ProfiloUtenteExec