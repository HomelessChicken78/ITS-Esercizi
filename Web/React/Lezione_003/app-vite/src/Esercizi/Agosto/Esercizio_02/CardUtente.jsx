// Esercizio 2: Componenti Dinamici con le Props
// Obiettivo: Imparare a passare dati a un componente per renderlo riutilizzabile.
// Componente da creare: CardUtente.js
// Istruzioni:
// 1. Crea il file CardUtente.js.
// 2. Modifica il componente affinché accetti props come argomento.
// 3. Il componente deve visualizzare un nome, un'email e un'immagine avatar. Usa
// props.nome, props.email e props.imgUrl per accedere ai dati.
// ○ Esempio di JSX: <h2>{props.nome}</h2> <p>{props.email}</p>
// <img src={props.imgUrl} alt="Avatar utente" />
// 4. In App.js, importa CardUtente e usalo almeno due volte, passando dati diversi
// per ogni card. Puoi usare un'immagine placeholder come
// https://placehold.co/

const CardUtente = (props) => {
  return (
    <div><img src={props.imgUrl} alt="Avatar utente" style={{ width: "50px", height: "50px", objectFit: "cover" }}/> {props.nome} - {props.email}</div>
  )
}

export default CardUtente