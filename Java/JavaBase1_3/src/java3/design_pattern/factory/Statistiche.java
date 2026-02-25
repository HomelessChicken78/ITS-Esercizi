package java3.design_pattern.factory;

import java.sql.*;
import java.util.ArrayList;

public class Statistiche {
	private String url = "jdbc:postgresql://localhost:5432/factoryeconsumer";
	private String user = "postgres";
	private String password = "postgres";
	private DataExport exporter;

	public Statistiche() {
	}

	private Connection getConnection() throws SQLException {
		return DriverManager.getConnection(url, user, password);
	}

	public void exportCategory(int idCategory, String type) throws ClassNotFoundException {
		PreparedStatement ps;
		try {
			this.exporter = FactoryDataExport.getExport(type);
			ps = getConnection().prepareStatement("SELECT * FROM category WHERE idcategory = ?");
			ps.setInt(1, idCategory);
			ResultSet rs = ps.executeQuery();

			ArrayList<String> categ = new ArrayList<>();

			if (rs.next()) {
				int id = rs.getInt("idcategory");
				categ.add("idcategory : " + id);

				String description = rs.getString("description");
				categ.add("description: " + description);

				exporter.export(categ, "new_category");
			} else
				System.out.println("Nessuna categoria trovata con ID: " + idCategory);

		} catch (SQLException e) {
			System.out.println("Qualcosa è andato storto =/");
		}
	}

	public void exportCity(String cityName, String type) throws ClassNotFoundException {
		PreparedStatement ps;
		try {
			this.exporter = FactoryDataExport.getExport(type);
			ps = getConnection().prepareStatement("SELECT * FROM city WHERE cityname = ?");
			ps.setString(1, cityName);
			ResultSet rs = ps.executeQuery();

			ArrayList<String> city = new ArrayList<>();

			if (rs.next()) {
				String name = rs.getString("cityname");
				city.add("name : " + name);

				String region = rs.getString("region");
				city.add("region: " + region);

				exporter.export(city, "new_city");
			} else
				System.out.println("Nessuna città trovata con nome: " + cityName);

		} catch (SQLException e) {
			System.out.println("Qualcosa è andato storto =/");
		}
	}
}