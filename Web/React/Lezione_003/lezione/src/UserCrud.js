import React from 'react'
import UserForm from './UserForm'
import { useRef, useState } from 'react'

const UserCrud = () => {
    let id = useRef(null);
    let nome = useRef(null);
    let cognome = useRef(null);
    let email = useRef(null);
    let numero = useRef(null);
    let [utenti, setUtenti] = useState([])

    const handleSubmit = (e) => {
        console.log("eseguo la funzione")
        e.preventDefault()
        let idR = id.current.value.trim()
        let nomeR = nome.current.value.trim()
        let cognomeR = cognome.current.value.trim()
        let emailR = email.current.value.trim()
        let numeroR = numero.current.value.trim()
        if (idR && nomeR && cognomeR && emailR && numeroR) {
            setUtenti([
                ...utenti,
                { idR, nomeR, cognomeR, emailR, numeroR }
            ])
            console.log(utenti)
            id.current.value = '';
            nome.current.value = '';
            cognome.current.value = '';
            email.current.value = '';
            numero.current.value = '';
        } else {
            alert("Perfavore riempire tutti i campi!")
        }
    }


    return (
        <>
            <form onSubmit={handleSubmit} className="container">
                <div className="container">
                    <div className="row">
                        <div className="col-3"></div>
                        <div className="col-6">
                            <input
                                type="text"
                                className="form-control"
                                placeholder="id"
                                aria-label="id"
                                ref={id}
                            />
                        </div>
                        <div className="col-3"></div>
                        <div className="col-3"></div>
                        <div className="col-6">
                            <input
                                type="text"
                                className="form-control"
                                placeholder="First name"
                                aria-label="First name"
                                ref={nome}
                            />
                        </div>
                        <div className="col-3"></div>
                        <div className="col-3"></div>
                        <div className="col-6">
                            <input
                                type="text"
                                className="form-control"
                                placeholder="Last name"
                                aria-label="Last name"
                                ref={cognome}
                            />
                        </div>
                        <div className="col-3"></div>
                        <div className="col-3"></div>
                        <div className="col-6">
                            <input
                                type="text"
                                className="form-control"
                                placeholder="Email"
                                aria-label="Email"
                                ref={email}
                            />
                        </div>
                        <div className="col-3"></div>
                        <div className="col-3"></div>
                        <div className="col-6">
                            <input
                                type="text"
                                className="form-control"
                                placeholder="Phone number"
                                aria-label="Phone number"
                                ref={numero}
                            />
                        </div>
                        <div className="col-3"></div>
                        <div className="col-3"></div>
                        <div className="col-6 d-flex justify-content-center"><button type="submit" class="btn btn-outline-secondary">Invia</button></div>
                        <div className="col-3"></div>
                    </div>
                </div>
            </form>
        </>
    )
}

export default UserCrud