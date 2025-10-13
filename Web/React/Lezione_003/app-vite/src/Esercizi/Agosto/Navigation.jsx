import Saluto from './Esercizio_01/Saluto';
import CardUtente from './Esercizio_02/CardUtente';
import MenuRistorante from './Esercizio_03/MenuRistorante';
import Termostato from './Esercizio_04/Termostato';
import CampoRicerca from './Esercizio_05/CampoRicerca';
import MessaggioSegreto from './Esercizio_06/MessaggioSegreto';
import AggiornaTitolo from './Esercizio_07/AggiornaTitolo';
import GalleriaFoto from './Esercizio_08/GalleriaFoto';
import ModuloContatti from './Esercizio_09/ModuloContatti';
import BlogApp from './Esercizio_10/BlogApp';
import TodoApp from './Esercizio_11/TodoApp';

import { React, useState } from 'react';

const Navigation = () => {
    let [currentPage, setPage] = useState("Saluto")
    let Pages = ["Saluto", "Card Utente", "Menu Ristorante", "Termostato",
        "Campo Ricerca", "Messaggio Segreto", "Aggiorna Titolo",
        "Galleria Foto", "Modulo Contatti", "Blog App", "Todo App",]
    function RenderCondizionale() {
        switch (currentPage) {
            case "Saluto":
                return (
                    <Saluto />
                )
            case "Card Utente":
                return (
                    <>
                        <CardUtente nome="Cristiano" email="cristiano003@gmail.com" imgUrl="https://placehold.co/600x400" />
                        <CardUtente nome="Gianluca" email="gianl@yahoo.com" imgUrl="https://placehold.co/250x600" />
                    </>
                )
            case "Menu Ristorante":
                return (
                    <MenuRistorante />
                )

            case "Termostato":
                return (
                    <Termostato />
                )

            case "Campo Ricerca":
                return (
                    <CampoRicerca />
                )

            case "Messaggio Segreto":
                return (
                    <MessaggioSegreto />
                )

            case "Aggiorna Titolo":
                return (
                    <AggiornaTitolo />
                )

            case "Galleria Foto":
                return (
                    <GalleriaFoto />
                )

            case "Modulo Contatti":
                return (
                    <ModuloContatti />
                )

            case "Blog App":
                return (
                    <BlogApp />
                )

            case "Todo App":
                return (
                    <>
                        <TodoApp />
                    </>
                )
        }
    }
    return (
        <>
            {/* <div style={{ marginLeft: "10px" }}>
        <h1>Esercizio 1</h1>
        <Saluto />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 2</h1>
        <CardUtente nome="Cristiano" email="cristiano003@gmail.com" imgUrl="https://placehold.co/600x400" />
        <CardUtente nome="Gianluca" email="gianl@yahoo.com" imgUrl="https://placehold.co/250x600" />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 3</h1>
        <MenuRistorante />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 4</h1>
        <Termostato />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 5</h1>
        <CampoRicerca />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 6</h1>
        <MessaggioSegreto />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 7</h1>
        <AggiornaTitolo />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 8</h1>
        <GalleriaFoto />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 9</h1>
        <ModuloContatti />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 10</h1>
        <BlogApp />

        <hr className='my-4 border-primary border border-5' />

        <h1>Esercizio 11</h1>
        <TodoApp />
      </div> */}

            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <button
                    className="navbar-toggler"
                    type="button"
                    data-toggle="collapse"
                    data-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon" />
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item active">
                            <a className="nav-link">
                                <b>Esercizi</b>
                            </a>
                        </li>
                        {Pages.map((page, ind) => {
                            if (page == currentPage) {
                                return (
                                    <li className="nav-link">
                                        <a className=" btn btn-primary" href="#" key={ind} onClick={() => setPage(page)}>
                                            {page}
                                        </a>
                                    </li>
                                )
                            }
                            else {
                                return (
                                    <li className="nav-item">
                                        <a className="nav-link btn btn-secondary" href="#" key={ind} onClick={() => setPage(page)}>
                                            {page}
                                        </a>
                                    </li>
                                )
                            }
                        })}
                    </ul>
                </div>
            </nav>
            <div>{RenderCondizionale()}</div>
        </>
    )
}

export default Navigation