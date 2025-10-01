import React, { useState, useEffect } from "react";
import TodoForm from "./TodoForm";
import TodoList from "./TodoList";
import { fetchTasksService, deleteTaskService, toggleTaskService, updateTaskService, addTaskService } from "./api";

const API_URL = "http://localhost:3123/tasks";
const TodoApp = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchTasks = async () => {
        try {
            const data = await fetchTasksService();
            setTasks(data);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    const deleteTask = async (id) => {
        await deleteTaskService(id)
        fetchTasks();
    }

    const toggleTask = async (id, completed) => {
        await toggleTaskService(id, completed)
        fetchTasks();
    };

    const updateTask = async (id, text) => {
        await updateTaskService(id, text)
        fetchTasks();
    }

    const addTask = async (text) => {
        await addTaskService(text)
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