import React, { useState, useEffect } from "react";
import TodoForm from "./TodoForm";
import TodoList from "./TodoList";

const API_URL = "http://localhost:3123/tasks";
const TodoApp = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchTasks = async () => {
        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error("Errore nella fetch");
            const data = await response.json();
            setTasks(data);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    const deleteTask = async (id) => {
        await fetch(API_URL + "/" + id, { method: "DELETE" })
        fetchTasks();
    }

    const toggleTask = async (id, completed) => {
        await fetch(API_URL + "/" + id, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ completed: !completed })
        })
        fetchTasks();
    };

    const updateTask = async (id, text) => {
        await fetch(API_URL + "/" + id, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        })
        fetchTasks();
    }

    const addTask = async (text) => {
        await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text, completed: false })
        })
        fetchTasks();

    }

    useEffect(() => {
        fetchTasks();
    }, []);
    return (
        <div>
            <h1>Todolist</h1>
            <TodoForm onAddTask={addTask}></TodoForm>
            <TodoList tasks={tasks} onDeleteTask={deleteTask} onToggleTask={toggleTask} onUpdateTask={updateTask}></TodoList>
        </div>
    );
};

export default TodoApp;