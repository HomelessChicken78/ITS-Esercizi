
// import { useState, useEffect } from "react"

// const usersUrl = 'https://jsonplaceholder.typicode.com/users'

// const UserCrud = () => {
//   const [users, setUsers] = useState([])

//   const getUsers = () => {
//     fetch(usersUrl).then(response => response.json()).then(ris => setUsers(ris))
//   }

//   useEffect(() => {
//     getUsers()
//   }, [])

//   const deleteUser = (id) => {
//     const newUsers = users.filter((u) => u.id !== id);
//     if (window.confirm("Sei sicuro di voler cancellare questo utente")) {
//       setUsers(newUsers);
//     }
//   }

//   return (
//     <>
//       <div className="container">
//         <h1>USER CRUD</h1>
//         <div>
//           <div className="row">
//             <div className="col-8">Utente</div>
//             <div className="col-4">Azioni</div>
//           </div>
//           {users.map((u) => {
//             return (
//               <div className="row my-1 border">
//                 <div className="col-8 p-2 d-flex justify-content-start">{u.name}</div>
//                 <div className="col-4 p-2 d-flex justify-content-end">
//                   <button className="btn btn-success btn-sm">Update</button>
//                   <button className="btn btn-danger btn-sm" onClick={() => (deleteUser(u.id))}>Delete</button>
//                 </div>
//               </div>
//             );
//           })}
//         </div>
//       </div>
//     </>
//   )
// }
// // json-server -p 3001 --watch db.json

// export default UserCrud;



























import { useEffect, useState } from "react";

const urlUser = "http://localhost:3238/users";
const UserCrud = () => {
  const [users, setUsers] = useState([]);

  const getUsers = () => {
    fetch(urlUser)
      .then((response) => response.json())
      .then((ris) => setUsers(ris));
  };
  useEffect(() => {
    getUsers();
  }, []);

  const deleteUser = (id) => {
    const newUsers = users.filter((u) => u.id !== id);
    if (window.confirm("Sei sicuro di voler cancellare questo utente?")) {
      setUsers(newUsers);
    }
  };

  return (
    <>
      <div className="container">
        <h1>USER CRUD</h1>

        <div className="mb-3 row">
          <label htmlFor="staticEmail" className="col-sm-2 col-form-label">
            Email
          </label>
          <div className="col-sm-10">
            <input
              type="text"
              readOnly
              className="form-control-plaintext"
              id="staticEmail"
              value="email@example.com"
            ></input>
          </div>
        </div>
        <div className="mb-3 row">
          <label htmlFor="inputPassword" className="col-sm-2 col-form-label">
            Password
          </label>
          <div className="col-sm-10">
            <input
              type="password"
              className="form-control"
              id="inputPassword"
            ></input>
          </div>
        </div>

        <div className="row">
          <div className="col-8 p-2 d-flex justify-content-start bg-secondary text-white">
            Utente
          </div>
          <div className="col-4 p-2 d-flex justify-content-end bg-secondary text-white">
            Azioni
          </div>
        </div>
        <div>
          {users.map((u) => {
            return (
              <div className="row my-1 border" key={u.id}>
                <div className="col-8 p-2 d-flex justify-content-start">
                  {u.name}
                </div>
                <div className="col-4 p-2 d-flex justify-content-end gap-2">
                  <button className="btn btn-primary">Update</button>
                  <button
                    className="btn btn-danger"
                    onClick={() => {
                      deleteUser(u.id);
                    }}
                  >
                    Delete
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
};
export default UserCrud;
