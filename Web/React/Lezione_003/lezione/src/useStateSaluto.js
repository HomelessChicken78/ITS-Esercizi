import './App.css';
import { useState } from 'react';
import Persona from './Persona';

function App() {

  // let saluto = "ciao"

  // const cambioSaluto = () => {
  //   if (saluto === "ciao") {
  //     saluto = "arrivederci"
  //   } else if (saluto === "arrivederci") {
  //     saluto = "ciao"
  //   }
  //   console.log(saluto)
  // }
  // return (
  //   <div className='App'>
  //     <h1>Componente principale</h1>
  //     <h2>{saluto}</h2>
  //     <button onClick={cambioSaluto}>Cambia</button>
  //   </div>
  // );


  console.log(useState)

  let [saluto, setSaluto] = useState("buongiorno")
  console.log(saluto, "\n", setSaluto)

  const cambioSaluto = () => {
    if (saluto === "buongiorno") {
      setSaluto("arrivederci")
    }
    else if (saluto === "arrivederci") {
      setSaluto("buongiorno")
    }
    console.log(saluto)
  }

  return (
    <div className='App'>
      <h1>Componente principale</h1>
      <h2>{saluto}</h2>
      <button onClick={cambioSaluto}>Cambia</button>
      <Persona></Persona>
    </div>
  );
}

export default App;
