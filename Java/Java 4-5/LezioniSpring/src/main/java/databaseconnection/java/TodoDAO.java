package databaseconnection.java;

import java.sql.*;
import java.util.Collection;
import java.util.LinkedList;

import databaseconnection.java.*;

// Short for "Data access object". Used for method to access the database
public class TodoDAO {
	public static boolean inserisciTask(String task) {
		String sql = "INSERT INTO todo (task) VALUES (?)";

		PreparedStatement ps = null;

		try {
			Connection conn = DatabaseTODO.getConnection();
			ps = conn.prepareStatement(sql);
			ps.setString(1, task);

			return ps.executeUpdate() == 1;
		} catch (SQLException e) {
			throw new RuntimeException(e.getMessage());
		}
	}

	public static boolean rimuoviTask(int idTask) {
		String sql = "DELETE FROM todo WHERE id = ?";

		PreparedStatement ps = null;

		try {
			ps = DatabaseTODO.getConnection().prepareStatement(sql);
			ps.setInt(1, idTask);

			return ps.executeUpdate() == 1;
		} catch (SQLException e) {
			throw new RuntimeException(e.getMessage());
		}
	}

	public static Collection<todoDTO> findAll() {
		Collection<todoDTO> allTODOs = new LinkedList<>();

		try {
			PreparedStatement ps = DatabaseTODO.getConnection().prepareStatement("SELECT * FROM todo");

			ResultSet resQuery = ps.executeQuery();

			while (resQuery.next()) {
				int id = resQuery.getInt("Id");
				String task = resQuery.getString("task");
				boolean done = resQuery.getBoolean("done");
				allTODOs.add(new todoDTO(id, task, done));
			}

			return allTODOs;
		} catch (SQLException e) {
			throw new RuntimeException(e.getMessage());
		}
	}

	public static boolean setCompleted(int id) {
		try {
			PreparedStatement ps = DatabaseTODO.getConnection().prepareStatement("UPDATE todo SET done = true WHERE id = ?");
			ps.setInt(1, id);
			return ps.executeUpdate() == 1;
		} catch (SQLException e) {
			throw new RuntimeException(e.getMessage());
		}
	}
}
