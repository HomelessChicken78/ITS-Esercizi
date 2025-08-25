import { useState } from 'react';

function Saluto() {

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
    <div className='Saluto'>
      <h2>{saluto}</h2>
      <button onClick={cambioSaluto}>Cambia</button>
    </div>
  );
}

export default Saluto;
