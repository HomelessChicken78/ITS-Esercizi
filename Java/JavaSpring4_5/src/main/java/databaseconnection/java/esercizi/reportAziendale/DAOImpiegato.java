package databaseconnection.java.esercizi.reportAziendale;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DAOImpiegato {
	public static Impiegato aggiungiNuovo(int matricola, String nome, double salario_mensile, double bonus_annuale,
			int idMansione) throws SQLException {
		PreparedStatement ps = Database.getConnection().prepareStatement(
				"INSERT INTO impiegati (matricola, nome, salario_mensile, bonus_annuale, mansione_id) VALUES (?, ?, ?, ?, ?)");
		ps.setInt(1, matricola);
		ps.setString(2, nome);
		ps.setDouble(3, salario_mensile);
		ps.setDouble(4, bonus_annuale);
		ps.setInt(5, idMansione);

		// cerca mansione
		Mansione mansioneImpiegato = null;
		PreparedStatement cercaMansione = Database.getConnection()
				.prepareStatement("SELECT * FROM mansioni WHERE id = ?");
		cercaMansione.setInt(1, idMansione);
		ResultSet mansioneTrovata = cercaMansione.executeQuery();
		if (mansioneTrovata.next())
			mansioneImpiegato = new Mansione(mansioneTrovata.getInt("id"), mansioneTrovata.getString("nome"),
					mansioneTrovata.getDouble("stipendio_min"), mansioneTrovata.getDouble("stipendio_max"));

		if (ps.executeUpdate() == 1)
			return new Impiegato(matricola, nome, salario_mensile, bonus_annuale, mansioneImpiegato);
		return null;
	}

	public static Impiegato aggiungiNuovo(int matricola, String nome, double salario_mensile, double bonus_annuale,
			int idMansione, String nomeMansione, double stipendio_min_mansione, double stipendio_max_mansione) throws SQLException {
		Mansione nuovaMansione = DAOMansione.aggiungiNuova(idMansione, nomeMansione, stipendio_min_mansione, stipendio_max_mansione);
		PreparedStatement ps = Database.getConnection().prepareStatement(
				"INSERT INTO impiegati (matricola, nome, salario_mensile, bonus_annuale, mansione_id) VALUES (?, ?, ?, ?, ?)");
		ps.setInt(1, matricola);
		ps.setString(2, nome);
		ps.setDouble(3, salario_mensile);
		ps.setDouble(4, bonus_annuale);
		ps.setInt(5, idMansione);

		if (ps.executeUpdate() == 1)
			return new Impiegato(matricola, nome, salario_mensile, bonus_annuale, nuovaMansione);
		return null;
	}

	public static boolean aggiungiNuovo(Impiegato impiegato) throws SQLException {
		PreparedStatement ps = Database.getConnection().prepareStatement(
				"INSERT INTO impiegati (matricola, nome, salario_mensile, bonus_annuale, mansione_id) VALUES (?, ?, ?, ?, ?)");
		ps.setInt(1, impiegato.getMatricola());
		ps.setString(2, impiegato.getNome());
		ps.setDouble(3, impiegato.getSalario_mensile());
		ps.setDouble(4, impiegato.getBonus_annuale());
		ps.setInt(5, impiegato.getMansione().getId());

		return ps.executeUpdate() == 1;
	}

	public static boolean existsWithMatricola(int matricola) throws SQLException {
		PreparedStatement ps = Database.getConnection().prepareStatement("SELECT * FROM impiegati WHERE matricola = ?");
		ps.setInt(1, matricola);

		return ps.executeQuery().next();
	}
}
