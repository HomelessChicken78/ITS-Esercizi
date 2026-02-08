package com.spring.lezioni.dtoEsempio.entity;

public class Utente2 {
	private String nome, cognome, mail, telefono;
	private int idUtente;

	public Utente2(String nome, String cognome, String mail, String telefono, int idUtente) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.mail = mail;
		this.telefono = telefono;
		this.idUtente = idUtente;
	}

	public Utente2() {
		System.out.println("spring sta costruendo l'utente");
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public String getMail() {
		return mail;
	}

	public void setMail(String mail) {
		this.mail = mail;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public int getIdUtente() {
		System.out.println("getId");
		return idUtente;
	}

	public void setIdUtente(int idUtente) {
		System.out.println("setId");
		this.idUtente = idUtente;
	}

	@Override
	public String toString() {
		return "nome=" + nome + ", cognome=" + cognome + ", mail=" + mail + ", telefono=" + telefono + ", idUtente="
				+ idUtente;
	}
}
