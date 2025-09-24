import React, { useEffect, useState } from 'react'
import TodoForm from './TodoForm'
import TodoList from './TodoList'

const API_URl = 'http://localhost:3123/tasks'

const TodoApp = () => {
    const [task, setTasks] = useState([]);
    const [load, setLoad] = useState(true);
    const [error, setErr] = useState(null);

    const fetchTasks = async () => {
        try {
            const res = await fetch(API_URl);
            if (!res.ok) throw new Error("Errore nella fetch");

            const data = await res.json();

            setTasks(data);
        } catch (err) {
            setErr(err)
        } finally {
            setLoad(false)
        }
    };

    const deleteTask = async (id) => {
        await fetch(API_URl + "/" + id,
            { method: "DELETE" }
        )
        fetchTasks();
    };

    const toggleTask = async (id, completed) => {
        await fetch(API_URl + "/" + id,
        {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ completed: !completed })
        }
        )
    fetchTasks();
};

useEffect(() => {
    fetchTasks()
}, []);

return (
    <>
        <TodoForm />
        <TodoList tasks={task} onDeleteTask={deleteTask} onToggleTask={toggleTask}></TodoList>
    </>
)
}

export default TodoApp