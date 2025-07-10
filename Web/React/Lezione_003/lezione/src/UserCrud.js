import React from 'react'
import UserForm from './UserForm'

const UserCrud = () => {
    
  return (
    <>
    <div class="container">
    <div className="row">
    <div className="col-3"></div>
    <div className="col-6">
    <input
      type="text"
      className="form-control"
      placeholder="id"
      aria-label="id"
    /> 
  </div>
  <div className="col-3"></div>
  <div className="col-3"></div>
  <div className="col-6">
    <input
      type="text"
      className="form-control"
      placeholder="First name"
      aria-label="First name"
    />
  </div>
  <div className="col-3"></div>
  <div className="col-3"></div>
  <div className="col-6">
    <input
      type="text"
      className="form-control"
      placeholder="Last name"
      aria-label="Last name"
    />
  </div>
  <div className="col-3"></div>
  <div className="col-3"></div>
    <div className="col-6">
    <input
      type="text"
      className="form-control"
      placeholder="Email"
      aria-label="Email"
    />
  </div>
  <div className="col-3"></div>
  <div className="col-3"></div>
      <div className="col-6">
    <input
      type="text"
      className="form-control"
      placeholder="Phone number"
      aria-label="Phone number"
    />
  </div>
  <div className="col-3"></div>
  <div className="col-3"></div>
  <div className="col-6 d-flex justify-content-center"><button type="button" class="btn btn-outline-secondary">Invia</button></div>
  <div className="col-3"></div>
</div>
</div>
</>
  )
}

export default UserCrud