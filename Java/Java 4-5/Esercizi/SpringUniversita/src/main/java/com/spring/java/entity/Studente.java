package com.spring.java.entity;

public class Studente {
	private int matricola;
	private String nome, cognome, indirizzo;
	private int annoNascita, annoImmatricolazione;

	public Studente() {}

	public Studente(int matricola, String nome, String cognome, String indirizzo, int annoNascita,
			int annoImmatricolazione) {
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.indirizzo = indirizzo;
		this.annoNascita = annoNascita;
		this.annoImmatricolazione = annoImmatricolazione;
	}

	public void setMatricola(int matricola) {
		this.matricola = matricola;
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

	public String getIndirizzo() {
		return indirizzo;
	}

	public void setIndirizzo(String indirizzo) {
		this.indirizzo = indirizzo;
	}

	public int getAnnoNascita() {
		return annoNascita;
	}

	public void setAnnoNascita(int annoNascita) {
		this.annoNascita = annoNascita;
	}

	public int getAnnoImmatricolazione() {
		return annoImmatricolazione;
	}

	public void setAnnoImmatricolazione(int annoImmatricolazione) {
		this.annoImmatricolazione = annoImmatricolazione;
	}

	public int getMatricola() {
		return matricola;
	}

	@Override
	public String toString() {
		return "matricola=" + matricola + ", nome=" + nome + ", cognome=" + cognome + ", indirizzo=" + indirizzo
				+ ", annoNascita=" + annoNascita + ", annoImmatricolazione=" + annoImmatricolazione;
	}
}
