// Esercizio 9: Gestire Form Complessi con un Singolo Stato
// Obiettivo: Gestire un form con più campi usando un singolo oggetto per lo stato.
// Componente da creare: ModuloContatti.js
// Istruzioni:
// 1. Crea il componente ModuloContatti.js.
// 2. Usa useState per inizializzare uno stato come oggetto: { nome: '', email:
// '', messaggio: '' };.
// 3. Crea un form con tre input (nome, email) e una textarea (messaggio). Aggiungi
// a ognuno l'attributo name corrispondente.
// 4. Crea una sola funzione handleChange per tutti i campi. All'interno, usa lo spread
// operator per aggiornare solo il campo modificato.
// 5. Gestisci l'evento onSubmit del form per stampare l'oggetto datiForm in console.
// 6. Importa e usa <ModuloContatti /> in App.js

import { useEffect, useRef, useState } from "react"

const ModuloContatti = () => {
    const [persona, setPersona] = useState({ nome: '', email: '', messaggio: '' });
    const nome = useRef('');
    const email = useRef('');
    const messaggio = useRef('');

    const handleChange = (e) => {
        e.preventDefault()

        setPersona({
            ...persona,
            nome: nome.current.value,
            email: email.current.value,
            messaggio: messaggio.current.value
        })
    }

    useEffect(() => {
        console.log(persona)
    }, [persona])

    return (
        <>
            <form onSubmit={handleChange}>
                <div className="row">
                    <div className="col">
                        <input type="text" name="nome" ref={nome} className="form-control" placeholder="Nome" />
                    </div>
                    <div className="col">
                        <input type="text" name="email" ref={email} className="form-control" placeholder="name@example.com" />
                    </div>
                </div>
                <div className="row my-2">
                    <div className="col">
                        <textarea name="messaggio" ref={messaggio} className="form-control" />
                    </div>
                </div>
                <div className="row">
                    <div className="col d-flex justify-content-center my-4">
                        <button type="submit" className="btn btn-outline-primary rounded-pill">Invia messaggio</button>
                    </div>
                </div>
            </form>
        </>
    )
}

export default ModuloContatti