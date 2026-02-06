package com.spring.java.entity;

public class Professore {
	private int id;
	private String nome, cognome, materiaInsegna;

	public Professore() {}

	public Professore(int id, String nome, String cognome, String materiaInsegna) {
		this.id = id;
		this.nome = nome;
		this.cognome = cognome;
		this.materiaInsegna = materiaInsegna;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
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

	public String getMateriaInsegna() {
		return materiaInsegna;
	}

	public void setMateriaInsegna(String materiaInsegna) {
		this.materiaInsegna = materiaInsegna;
	}
}
