const API_URL = "http://localhost:3000/tasks";

export const fetchTasksService = async () => {
  const response = await fetch(API_URL);
  if (!response.ok) throw new Error("Errore nella fetch");
  const data = await response.json();
  return data;
};

export const deleteTaskService = async (id) => {
    await fetch(API_URL + "/" + id, { method: "DELETE" });
  };