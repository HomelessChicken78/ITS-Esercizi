import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'

// import Component1 from './Lezioni/Props/Component1';
// import Clock from './Lezioni/Props/Clock';
// import UserAdder from './Lezioni/Hooks/UseRefExample';

// import Persona from './Esercizi/Map/Esercizio_1';
// import Tabellina from './Esercizi/Map/Esercizio_2';
// import Stampanumeri from './Esercizi/Map/Esercizio_3';
// import BetterStampanumeri from './Esercizi/Map/Esercizio_4';
// import Biblioteca from './Esercizi/Map/Esercizio_5'
// import ProfiloUtenteExec from './Esercizi/Map/ProfiloUtente/ProfiloUtenteExec';

// import Counter from './Esercizi/Hook/Counter';

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
      {/* Esercizi sul map<br /> */}
      {/* <Persona name="Mario" cognome="Rossi"></Persona>
      <Tabellina multiplier="2"></Tabellina>
      <Stampanumeri></Stampanumeri>
      <BetterStampanumeri></BetterStampanumeri>
      <Biblioteca></Biblioteca> */}
      {/* <ProfiloUtenteExec></ProfiloUtenteExec> */}

      {/* Esercizi su UseState<br /> */}
      {/* <Counter></Counter> */}

      {/* Prima Lezione<br /> */}
      {/* <h1>Prima app con React di {nome}</h1> */}
      {/* <h2>
        {getDate(new Date())}
      </h2> */}
      {/* <Component1>Roberto</Component1>
      <Component1>Cristiano</Component1>
      <Component1>Nicol</Component1>
      <Component1>Stefano</Component1> */}
      {/* <Clock timezone="0" country="Italia"></Clock>
      <Clock timezone="-6" country="USA"></Clock>
      <Clock timezone="7" country="Japan"></Clock> */}
      {/* <button onClick={saluta}> Ciao </button> */}
      {/* <button onClick={(e) => saluta(e)}>Saluta</button> */}

      {/* Lezione su UseRef<br /> */}
      {/* <UserAdder></UserAdder> */}
    </div>
  );
}

export default App;