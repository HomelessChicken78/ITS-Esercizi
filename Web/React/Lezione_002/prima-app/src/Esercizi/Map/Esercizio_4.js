import React from 'react'
// Scrivere un programma che conta da 0 a 20 con passo 2 e stampa i numeri ottenuti
// (0,2,...,20)

let arr1 = []

for (let num=0; num <=20; num += 2) {
    arr1.push(num)
}

const BetterStampanumeri = () => {
  return (
    <div>{arr1.map((i, key) => {
        return <span key={key}>{i} </span>
    })}</div>
  )
}

export default BetterStampanumeri