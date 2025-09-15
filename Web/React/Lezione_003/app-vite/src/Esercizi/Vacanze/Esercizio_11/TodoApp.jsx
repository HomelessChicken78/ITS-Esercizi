import { useEffect, useState } from "react"

const TodoApp = () => {
    const [tasks, setTasks] = useState([])
    const [err, setErr] = useState(false)
    const [load, setLoad] = useState(true)

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch("http://localhost:3238/tasks")
                const data = await res.json()
                setTasks(data)
                setLoad(false)
            } catch {
                setErr(true)
                setLoad(false)
            }
        }
        fetchData()
    }, [])

    return (
        <>
            {load && <div>Caricamento in corso...</div>}
            {err && <div>Errore</div>}
        </>
    )
}

export default TodoApp