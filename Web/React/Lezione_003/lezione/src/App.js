import './App.css';
import { useState } from 'react';
// import Persona from './useState/Persona';
// import UserCrud from './UserCrud';
import 'bootstrap/dist/css/bootstrap.css';
import RenderCondizionale from './conditional_render/RenderCondizionale';

function App() {
  // return (
  //   <>
  //       <UserCrud />
  //   </>
  // );
  return (
    <RenderCondizionale />
  )
}

export default App;
