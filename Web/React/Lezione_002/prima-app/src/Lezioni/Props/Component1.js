import React from 'react'

// Esempio di come usare i props
const Component1 = (props) => {
  return (
    <>
    <div style={{
      color:"red",
      border:"10px #000 solid",
      fontWeight:"600",
      margin:"15px",
      padding:"15px",
      width:"300px",
      display:"flex",
      }}>
    <div>Component1 di {props.children}</div>
    <div></div>{/* da un problema se dovesse mancare il fragment */}
    </div>
    </>
  )
}

export default Component1