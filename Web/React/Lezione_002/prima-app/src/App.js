import Component1 from './Lezioni/Props/Component1';
import './App.css';
import Clock from './Lezioni/Props/Clock';


import Persona from './Esercizi/Map/Esercizio_1';
import Tabellina from './Esercizi/Map/Esercizio_2';
import Stampanumeri from './Esercizi/Map/Esercizio_3';
import BetterStampanumeri from './Esercizi/Map/Esercizio_4';
import Biblioteca from './Esercizi/Map/Esercizio_5'

// function getDate(date){
//   return date.toLocaleDateString()+" "+ date.toLocaleTimeString()
// }

function saluta(e) {
  alert("ciao ", e)
}

function App() {
  let nome = "Cristiano"
  return (
    <div className="App">
      {/* Esercizi sul map */}
      <Persona name="Mario" cognome="Rossi"></Persona>
      <Tabellina multiplier="2"></Tabellina>
      <Stampanumeri></Stampanumeri>
      <BetterStampanumeri></BetterStampanumeri>
      <Biblioteca></Biblioteca>
  

      <Component1>Roberto</Component1>
      <Component1>Cristiano</Component1>
      <Component1>Nicol</Component1>
      <Component1>Stefano</Component1>

      <h1>Prima app con React di {nome}</h1>
      {/* <h2>
        {getDate(new Date())}
      </h2> */}
      <Clock timezone="0" country="Italia"></Clock>
      <Clock timezone="-6" country="USA"></Clock>
      <Clock timezone="7" country="Japan"></Clock>
      {/* <button onClick={saluta}> Ciao </button> */}
      <button onClick={(e) => saluta(e)}>Saluta</button>
    </div>
  );
}

export default App;