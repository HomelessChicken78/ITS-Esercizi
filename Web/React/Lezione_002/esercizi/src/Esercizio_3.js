import React from 'react'
// Scrivere un componente Stampanumeri che stampa i numeri da 0 a 10 ;

const Stampanumeri = () => {
    let arr1 = [];
    for (let i = 0; i<=10; i++) {
        arr1.push(i)
    };

  return (
    <div>{arr1.map((i, key)=>{
        return <span key={key}>{i} </span>
    })}</div>
  )
}

export default Stampanumeri

/*
import React from 'react';

function Tabellina({ numero }) {
  if (numero < 1 || numero > 10) {
    return <p>Il numero deve essere compreso tra 1 e 10.</p>;
  }

  const righe = [];
  for (let i = 1; i <= 10; i++) {
    righe.push(
      <li key={i}>
        {numero} × {i} = {numero * i}
      </li>
    );
  }

  return (
    <div>
      <h2>Tabellina del {numero}</h2>
      <ul>
        {righe}
      </ul>
    </div>
  );
}

export default Tabellina;
*/