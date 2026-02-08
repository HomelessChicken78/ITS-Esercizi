package databaseconnection.java;
import java.sql.*;

public class App {
	private  static final String URL = "jdbc:postgresql://localhost:5432/accademia";
	private static final String USER = "postgres";
	private static final String PASS = "postgres";

	public static void main(String[] args) {
		Connection conn = null;
		try {
			conn = DriverManager.getConnection(URL,USER, PASS);
			String sql="SELECT * FROM Persona AS p WHERE stipendio > ?";
			PreparedStatement ps = conn.prepareStatement(sql);
			ps.setDouble(1, 38000);
			ResultSet res = ps.executeQuery();

			while (res.next()) {
				int id = res.getInt("id");
				String nomeCognome = res.getString("nome") + " " + res.getString("cognome");
				double stipendio = res.getDouble("stipendio");
				System.out.println(id + "|" + nomeCognome + " - stipendio: " + stipendio + "€");
			}
		} catch (SQLException e) {
			System.err.println("Errore di sql: " + e.getMessage());
		}
	}
}
