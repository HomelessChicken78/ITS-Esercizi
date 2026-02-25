package java3.design_pattern.factory;

import java.sql.*;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Setting {
	@SuppressWarnings("resource")
	public static void main(String[] args) {
		Map<Integer, String> validExporters = new HashMap<>();

		Connection conn;
		try {
			conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/factoryeconsumer", "postgres",
					"postgres");
			Statistiche stat = new Statistiche();

			PreparedStatement ps = conn.prepareStatement("SELECT * FROM exporttype");
			ResultSet rs = ps.executeQuery();

			System.out.println("Possibili scelte:");
			while (rs.next()) {
				int id = rs.getInt("idexporttype");
				String name = rs.getString("name");

				validExporters.put(id, name);
				System.out.println(id + ") " + name);
			}

			System.out.print("Inserisci l'ID -> ");
			int choice = new Scanner(System.in).nextInt();

			String exporterChosen = validExporters.get(choice);

			try {
				if (exporterChosen != null)
					System.out.println("Hai scelto: " + exporterChosen);
				else
					throw new ClassNotFoundException();

				System.out.println("Inserire un ID di una categoria -> ");
				stat.exportCategory(new Scanner(System.in).nextInt(), exporterChosen);
			} catch (ClassNotFoundException e) {
				System.out.println("Hai inserito un ID che non esiste!");
			}

		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}