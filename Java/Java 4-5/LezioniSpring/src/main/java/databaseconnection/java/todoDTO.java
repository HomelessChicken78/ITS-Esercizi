package databaseconnection.java;

//Short for Data Transfer object
public class todoDTO {
	private final int id;
	private String task;
	private boolean done;

	public todoDTO(int id, String task, boolean done) {
		super();
		this.id = id;
		this.task = task;
		this.done = done;
	}

	public int getId() {
		return id;
	}

	public String getTask() {
		return task;
	}

	public void setTask(String task) {
		this.task = task;
	}

	public boolean isDone() {
		return done;
	}

	public void setDone(boolean done) {
		this.done = done;
	}

	@Override
	public String toString() {
		return id + " " + task + ", done=" + done;
	}
}
