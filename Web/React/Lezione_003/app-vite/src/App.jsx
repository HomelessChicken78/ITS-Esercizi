import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import Navigation from './Esercizi/Agosto/Navigation';
import MainComponent from './Lezioni/MainComponent';
import ProvaRoutes from './Lezioni/routes/ProvaRoutes';

import CheckboxMultiple from './Esercizi/Ottobre/CheckboxMultiple';
import NascondiTesto from './Esercizi/Ottobre/NascondiTesto';
import CambioColore from './Esercizi/Ottobre/CambioColore';
import EchoInput from './Esercizi/Ottobre/EchoInput';
import SelettorePizza from './Esercizi/Ottobre/SelettorePizza';


function App() {
  return (
    <>
      <NascondiTesto />
      <CambioColore />
      <EchoInput />
      <SelettorePizza />
    </>
  )
}

export default App
