package databaseconnection.java.esercizi.gestioneutenti;

import java.util.Objects;

public class Utente {
	private String nome;
	private String cognome;
	private final String username;
	private String password;
	private int annoNascita;

	public Utente(String nome, String cognome, String username, String password, int annoNascita) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.username = username;
		this.password = password;
		this.annoNascita = annoNascita;
	}

	public String getNome() {
		return nome;
	}

	public String getCognome() {
		return cognome;
	}

	public String getUsername() {
		return username;
	}

	public String getPassword() {
		return password;
	}

	public int getAnnoNascita() {
		return annoNascita;
	}

	@Override
	public String toString() {
		return username;
	}

	@Override
	public int hashCode() {
		return Objects.hash(annoNascita, username);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Utente other = (Utente) obj;
		return annoNascita == other.annoNascita && Objects.equals(username, other.username);
	}
}
