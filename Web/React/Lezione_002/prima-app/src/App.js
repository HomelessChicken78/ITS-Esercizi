import Component1 from './Component1';
import './App.css';
import Clock from './Clock';

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
      <button onClick={(e)=>saluta(e)}>Saluta</button>
    </div>
  );
}

export default App;