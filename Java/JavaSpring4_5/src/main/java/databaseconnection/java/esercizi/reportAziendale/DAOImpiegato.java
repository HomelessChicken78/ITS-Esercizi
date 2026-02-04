package databaseconnection.java.esercizi.reportAziendale;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

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

	public static List<Impiegato> getAllImpiegati() throws SQLException {
		ArrayList<Impiegato> res = new ArrayList<>();

		ResultSet allImpiegati = Database.getConnection().prepareStatement("SELECT matricola, imp.nome imp_nome, salario_mensile, bonus_annuale, mansione_id, m.nome m_nome, stipendio_min, stipendio_max FROM impiegati AS imp JOIN mansioni AS m ON imp.mansione_id = m.id").executeQuery();

		while (allImpiegati.next()) {
			Mansione mansioneImpiegato = new Mansione(allImpiegati.getInt("mansione_id"), allImpiegati.getString("m_nome"), allImpiegati.getDouble("stipendio_min"), allImpiegati.getDouble("stipendio_max"));
			Impiegato impiegatoToReturn = new Impiegato(allImpiegati.getInt("matricola"), allImpiegati.getString("imp_nome"), allImpiegati.getDouble("salario_mensile"), allImpiegati.getDouble("bonus_annuale"), mansioneImpiegato);
			res.add(impiegatoToReturn);
		}

		return res;
	}
}
