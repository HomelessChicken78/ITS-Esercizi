import React from 'react'

const Tabellina = (props) => {
  let multiplier = parseInt(props.multiplier)
  let multiplicand = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8,
    9, 10
  ]

  return (
    <ul>{
      multiplicand.map((num, index)=>{
        return <li key={index}>{multiplier * num}</li>
      })
      }</ul>
  )
}

export default Tabellina