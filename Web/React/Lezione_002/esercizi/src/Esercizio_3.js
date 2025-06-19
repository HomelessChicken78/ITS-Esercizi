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