import React from 'react'
import { posts } from './dati'
import { useState } from 'react'

const Cards = () => {
    console.log(posts)

    const [show, setShow] = useState(true)
    const [tema, setTema] = useState(true)

    return (
        <div style={{ backgroundColor: tema ? "white" : "black" }}>
            <>
                <div className="row">
                    <div className="col-4"></div>
                    <div className="col-4" style={{ marginLeft: "40%", marginRight: "60%" }} >
                        <button type="button" className="btn btn-primary" onClick={() => setShow(!show)}>{show ? "Nascondi" : "Visualizza"}</button>
                        <button type="button" className="btn btn-primary" onClick={() => setTema(!tema)}>Tema {tema ? "Scuro" : "Chiaro"}</button>
                    </div>
                    <div className="col-4"></div>
                </div>
                <div className="row">
                    {show &&
                        posts.map((p) => {
                            return (
                                <div key={p.id} className="col-3">
                                    <div className="card" style={{ width: "18rem", backgroundColor: tema ? "white" : "black", borderColor: tema ? "gray" : "darkgray" }} >
                                        <div className="card-body">
                                            <h5 className="card-title" style={{ color: tema ? "black" : "white" }}>{p.titolo}</h5>
                                            <p className="card-text" style={{ color: tema ? "black" : "white" }}>
                                                {p.descrizione}
                                            </p>
                                        </div>
                                    </div>

                                </div>
                            )
                        })
                    }
                </div>
            </>
        </div>
    )
}

export default Cards