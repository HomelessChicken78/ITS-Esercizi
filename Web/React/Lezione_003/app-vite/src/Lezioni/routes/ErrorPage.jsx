import React from 'react'
import { useNavigate } from 'react-router-dom'

const ErrorPage = () => {
  const navigate = useNavigate();
  return (
    <div className="container my-5">
      <div className="row">
        <h1>Questa pagine non esiste!</h1>
        <button className="btn btn-success" onClick={() => navigate("/")}>Torna alla home</button>
        <button className="btn btn-success my-4" onClick={() => navigate(-1)}>Torna indietro</button>
      </div>
    </div>
  )
}

export default ErrorPage