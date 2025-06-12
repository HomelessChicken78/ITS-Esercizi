import Component1 from './Component1';
import './App.css';

function getDate(date){
  return date.toLocaleDateString()+" "+ date.toLocaleTimeString()
}

function App() {
  let nome = "Cristiano"
  return (
    <div className="App">
      <Component1></Component1>
      <h1>Prima app con React di {nome}</h1>
      <h2>
        {
          new Date().toLocaleDateString()+" "+ new Date().toLocaleTimeString()
        }
      </h2>
      <h2>
        {getDate(new Date())}
      </h2>
    </div>
  );
}

export default App;