import React, { useEffect } from 'react'
import { useState } from 'react'

const UserAlbum = () => {
    const [users, setUsers] = useState([])
    const [selectedUser, setSelectedUser] = useState()
    const [albums, setAlbums] = useState([])
    const [selectedAlbum, setSelectedAlbum] = useState()
    const [photos, setPhotos] = useState([])

    // User lists
    const getUsers = async () => {
        const users = await fetch("https://jsonplaceholder.typicode.com/users").then(ris => ris.json())
        setUsers(users)
    };

    useEffect(() => {
        getUsers();
    }, []);

    // Selected user
    const handleUser = (e) => {
        setSelectedUser(e.target.value)
        setAlbums([])
        setSelectedAlbum('')
        setPhotos([])

    };

    // Album lists
    const getAlbums = async () => {
        const albums = await fetch(`https://jsonplaceholder.typicode.com/albums?userId=${selectedUser}`).then(ris => ris.json())
        setAlbums(albums)
    };

    useEffect(() => {
        getAlbums()
    }, [selectedUser]);

    // Selected album
    const handleAlbum = (e) => {
        setSelectedAlbum(e.target.value)
    };

    // Photo lists
    const getPhoto = async () => {
        const photos = await fetch(`https://jsonplaceholder.typicode.com/photos?albumId=${selectedAlbum}`).then(ris => ris.json())
        setPhotos(photos)
    };

    useEffect(() => {
        getPhoto()
    }, [selectedAlbum])



    return (
        <>
            <div className='container'>
                <div className='row'>
                    <div className='col-3'></div>
                    <div className='col-3'>
                        <select value={selectedUser} onChange={handleUser} className='form-select'>
                            <option value=''>Seleziona Utente</option>
                            {users.map((u) => {
                                return (
                                    <option value={u.id} key={u.id}>
                                        {u.name}
                                    </option>
                                )
                            })}
                        </select>
                    </div>
                    <div className='col-3'>
                        <select value={selectedAlbum} onChange={handleAlbum} className='form-select'>
                            <option value=''>Seleziona Album</option>
                            {selectedUser && albums.map((a) => {
                                return (
                                    <option value={a.id} key={a.id}>
                                        {a.title}
                                    </option>
                                )
                            })}
                        </select>
                    </div>

                </div>
                {selectedAlbum && photos.map((p) => {
                    return (
                        <>
                            <div className='row'>
                                <div className='col-4'></div>
                                <div className='col-4' key={p.id}>{p.title}</div>
                                <div className='col-4'></div>
                            </div>
                        </>
                    )
                })}
            </div>
        </>
    )
}

export default UserAlbum