import React, { use } from 'react'
import { useState } from 'react'

const RenderCondizionale = () => {
    const [isLoading, setisloading] = useState(true)
    const [isError, setError] = useState(true)
    const [users, setUsers] = useState([])

    if (isLoading){
        return <Loading />
    }

    if (isError){
        return (<h2>Attenzione c'è un errore</h2>)
    }

    return (
        <div>RenderCondizionale</div>
    )
}

const Loading=() => {
    return(<h2>Loading...</h2>)
}

export default RenderCondizionale