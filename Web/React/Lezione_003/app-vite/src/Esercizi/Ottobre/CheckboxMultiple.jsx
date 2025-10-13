// Esercizio: Checkbox Multiple con
// Counter
// Obiettivo
// Creare un componente React che permetta di selezionare delle skills tramite checkbox, con
// conteggio delle selezioni e controllo del limite massimo.
// Requisiti
// Crea un array precompilato di 10 skills tecnologiche. Ogni skill deve avere:
// ● id (number)
// ● name (string)
// Esempio: JavaScript, React, Vue, Angular, TypeScript, Node.js, PHP, Laravel, WordPress,
// CSS/SASS
// Funzionalità richieste
// 1. Visualizzazione lista
// ○ Mostra tutte le skills come checkbox
// ○ Ogni checkbox deve essere cliccabile
// 2. Gestione selezioni (useState)
// ○ Usa useState per mantenere l'array degli ID delle skills selezionate
// ○ Quando clicchi una checkbox, aggiungi o rimuovi l'ID dall'array
// 3. Counter visivo
// ○ Mostra quante skills sono state selezionate (es: "Selezionate: 3 / 10")
// ○ Il counter deve aggiornarsi in tempo reale
// 4. Controllo limite (useEffect)
// ○ Usa useEffect per monitorare il numero di selezioni
// ○ Se l'utente seleziona più di 5 skills, mostra un alert() di avviso
// ○ L'useEffect deve attivarsi solo quando cambia l'array delle selezioni
// 5. Feedback visivo (opzionale)
// ○ Cambia il colore del counter quando superi le 5 selezioni
// ○ Evidenzia le checkbox selezionate
// 6. Mostra un riepilogo delle skills selezionate sotto la lista
// 7. Aggiungi un bottone "Reset" per deselezionare tutto

import React, { useEffect, useState } from 'react'

const skills = [
    { id: 1, name: "JavaScript" },
    { id: 2, name: "Node.js" },
    { id: 3, name: "React" },
    { id: 4, name: "Angular" },
    { id: 5, name: "Java" },
    { id: 6, name: "C" },
    { id: 7, name: "Python" },
    { id: 8, name: "Django" },
    { id: 9, name: "Flask" },
    { id: 10, name: "Docker" },
];

const CheckboxMultiple = () => {
    const [skillChecked, setSkill] = useState([])

    const handleCheckbox = (id) => {
        if (skillChecked.includes(id)) {
            setSkill(skillChecked.filter((skill => skill !== id)))
        } else {
            setSkill([
                ...skillChecked,
                id
            ])
        }
    }

    useEffect(() => {
        if (skillChecked.length > 5) {
            alert("Limite di skill raggiunte. Non puoi più selezionarne!")
        }
    }, [skillChecked])

    return (
        <>
            <h2 className='d-flex justify-content-center mt-5'>Seleziona skills:</h2>
            <div className='d-flex justify-content-center'>
                <div className="form-check">
                    {skills.map((skill) => {
                        // if (!skillChecked.includes(skill.id) && skillChecked.length > 5) {
                        //     return (
                        //         <div className="form-check" key={skill.id}>
                        //             <input
                        //                 className="form-check-input"
                        //                 type="checkbox"
                        //                 id={'checkbox_skill ' + skill.id}
                        //                 onChange={() => (handleCheckbox(skill.id))}
                        //                 disabled
                        //             />
                        //             <label className="form-check-label" htmlFor={'checkbox_skill ' + skill.id}>
                        //                 {skill.name}
                        //             </label>
                        //         </div>
                        //     )
                        // }
                        // else {

                        return (
                            <div key={skill.id}>

                                <input
                                    className="form-check-input"
                                    type="checkbox"
                                    id={'checkbox_skill ' + skill.id}
                                    onChange={() => (handleCheckbox(skill.id))}
                                    checked={skillChecked.includes(skill.id)}
                                />
                                <label className={"form-check-label " + (skillChecked.includes(skill.id) ? "fw-bold" : "")}
                                    htmlFor={'checkbox_skill ' + skill.id}
                                >
                                    {skill.name}
                                </label>
                            </div>
                        )

                        // }
                    })}
                </div>
            </div>
            <div style=
                {{ color: skillChecked.length > 5 ? "red" : "black" }}
                className='d-flex justify-content-center'
            >
                {skillChecked.length === 0 ? "Nessuna skill selezionata!" : skillChecked.length === 1 ? `È stata selezionata 1 / 10 skill.` : `Sono state selezionate ${skillChecked.length} / 10 skills.`}
            </div>


            <h2 className='d-flex justify-content-center mt-5'>Riepilogo skills:</h2>
            {skills.map((skill) => {
                if (skillChecked.includes(skill.id)) {
                    return (
                        <div className='d-flex justify-content-center' >
                            {skill.name}
                        </div>
                    )
                }
            })}
            <div className='d-flex justify-content-center'>
                <button onClick={() => (setSkill([]))} className='btn btn-danger'>Reset</button>
            </div>

        </>
    )
}

export default CheckboxMultiple