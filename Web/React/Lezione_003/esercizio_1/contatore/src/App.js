import './App.css';
import { useState } from 'react';
// Esercizio
// Creare un componente che rappresenta per la mia
// applicazione un contatore utilizzando useState con
// valore di default uguale a zero. Sotto al contatore
// andiamo a creare due bottoni, uno «diminuisci» ed
// uno «aumenta» che al loro click andranno ad
// aumentare e a diminuire il valore del contatore.
// Utilizziamo bootstrap per rendere gradevole il
// nostro componente (a nostro piacimento)

function App() {
  let [contatore, updateContatore] = useState(0);

  const aumenta = () => {
    updateContatore(contatore + 1)
  };

  const diminuisci = () => {
    updateContatore(contatore - 1)
  };

  return (
    <>
      <div class="alert alert-info" role="alert"><h1 style={{ textAlign : 'center'}}>contatore</h1></div>
      <div class="card-body">
        <h2 style={{ textAlign : 'center'}} class="display-5">{contatore}</h2>
      </div>
      <div style={{ textAlign : 'center'}}>
        <button type="button" class="btn btn-success" onClick={aumenta}>Aumenta</button>
        <button type="button" class="btn btn-danger" onClick={diminuisci}>Diminuisci</button>
      </div>
    </>
  );
}

export default App;
