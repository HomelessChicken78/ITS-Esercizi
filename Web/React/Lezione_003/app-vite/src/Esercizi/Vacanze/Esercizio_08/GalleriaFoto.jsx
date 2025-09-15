// Esercizio 8: Caricare Dati da un Server (Data Fetching)
// Obiettivo: Usare useEffect per caricare dati da un'API esterna e gestire gli stati di
// caricamento ed errore. Componente da creare: GalleriaFoto.js
// Istruzioni:
// 1. Crea il componente GalleriaFoto.js.
// 2. Definisci tre stati: foto (array vuoto), staCaricando (true), errore (null).
// 3. Usa useEffect (con dipendenza []) per fare una fetch all'URL:
// https://jsonplaceholder.typicode.com/photos?_limit=10.
// 4. Dentro useEffect, usa una funzione async/await e un blocco try/catch.
// 5. Nel try, se la richiesta va a buon fine, popola lo stato foto e imposta
// staCaricando a false.
// 6. Nel catch, imposta lo stato errore con il messaggio di errore e staCaricando a
// false.
// 7. Nel JSX, gestisci i tre stati: mostra un messaggio di caricamento, un messaggio di
// errore, o la galleria di foto (mappando l'array foto e mostrando le immagini).

import { useEffect, useState } from "react"

const GalleriaFoto = () => {

  const [foto, setFoto] = useState([])
  const [staCaricando, setLoad] = useState(true)
  const [errore, setErr] = useState(null)

  useEffect(() => {
    const fetchFoto = async () => {
      try {
        const res = await fetch("https://jsonplaceholder.typicode.com/photos?_limit=10")
        const dati = await res.json()
        setFoto(dati)
        setLoad(false)
      } catch {
        setErr("Fetching non riuscito")
        setLoad(false)
      }
    }

    fetchFoto()
  }, [])

  return (
    <>
      {staCaricando && <div>Caricamento in corso...</div>}
      {errore && <div>{errore}</div>}
      {foto.map((f) => {
        return (
          <div key={f.id}>{f.title}</div>
        )
      })}
    </>
  )
}

export default GalleriaFoto