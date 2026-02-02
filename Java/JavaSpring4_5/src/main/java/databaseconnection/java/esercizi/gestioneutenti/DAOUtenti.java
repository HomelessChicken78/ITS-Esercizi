package databaseconnection.java.esercizi.gestioneutenti;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DAOUtenti {
	public static void registra(Utente user) throws SQLException, UsernameGiaInUso {
		try {
			PreparedStatement adding = Database.getConnection().prepareStatement("INSERT INTO utente (username, nome, cognome, password, annoNascita) VALUES  (?, ?, ?, ?, ?)");
			adding.setString(1, user.getUsername());
			adding.setString(2, user.getNome());
			adding.setString(3, user.getCognome());
			adding.setString(4, user.getPassword());
			adding.setInt(5, user.getAnnoNascita());

			adding.executeUpdate();
				
		
		} catch (SQLException e) {
			if (e.getSQLState().equals("23505"))
				throw new UsernameGiaInUso("l'username è già in uso! Scegline un'altra!");
			throw new SQLException(e.getMessage());
		}
	}

	public static Utente login(String username, String password) throws SQLException, CredenzialiErrate {
			PreparedStatement logging = Database.getConnection().prepareStatement("SELECT * FROM utente AS u WHERE u.username = ? AND u.password = ?");
			logging.setString(1, username);
			logging.setString(2, password);
			ResultSet ris = logging.executeQuery();

			if (!ris.next())
				throw new CredenzialiErrate("Credenziali errate");

			return new Utente(ris.getString("nome"), ris.getString("cognome"), ris.getString("username"), ris.getString("password"), ris.getInt("annoNascita"));			
	}

	public static void modificaPassword(String username, String vecchiaPassword, String nuovaPassword) throws UsernameErrata, CredenzialiErrate {
		try {
			DAOUtenti.login(username, vecchiaPassword);
			PreparedStatement changePW = Database.getConnection().prepareStatement("UPDATE utente SET password=? WHERE username=?;");
			changePW.setString(1, nuovaPassword);
			changePW.setString(2, username);

			if (changePW.executeUpdate() != 1)
				throw new UsernameErrata("Username non trovato");
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public static void cancellaUtente(String username) throws UsernameErrata {
		try {
			PreparedStatement cancUt = Database.getConnection().prepareStatement("DELETE FROM utente WHERE username = ?");
			cancUt.setString(1, username);
			if (cancUt.executeUpdate() != 1)
				throw new UsernameErrata("Username non trovato");
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	public static ResultSet listaUtenti() throws SQLException {
		return Database.getConnection().prepareStatement("SELECT username,nome, cognome, annoNascita FROM utente AS u;").executeQuery();
	}
}
