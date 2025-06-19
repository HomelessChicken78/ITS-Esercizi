import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';
import reportWebVitals from './reportWebVitals';
import Persona from './Esercizio_1';
import Tabellina from './Esercizio_2';
import Stampanumeri from './Esercizio_3';
import BetterStampanumeri from './Esercizio_4';
import Biblioteca from './Esercizio_5';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Persona nome="Mario" cognome="Rossi"></Persona>
    <Tabellina multiplier="2"></Tabellina>
    <Stampanumeri></Stampanumeri>
    <BetterStampanumeri></BetterStampanumeri>
    <Biblioteca></Biblioteca>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
