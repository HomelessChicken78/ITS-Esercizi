package com.rubrica.java.entity;

import java.time.LocalDate;
import java.util.Objects;

public class Contatto {
	private String nome, cognome, numero, gruppoAppartenenza;
	private LocalDate dataNascita;
	private boolean isPreferito;

	public Contatto() {}

	public Contatto(String nome, String cognome, String numero, String gruppoAppartenenza, LocalDate dataNascita,
			boolean isPreferito) {
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.numero = numero;
		this.gruppoAppartenenza = gruppoAppartenenza;
		this.dataNascita = dataNascita;
		this.isPreferito = isPreferito;
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

	public String getNumero() {
		return numero;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}

	public String getGruppoAppartenenza() {
		return gruppoAppartenenza;
	}

	public void setGruppoAppartenenza(String gruppoAppartenenza) {
		this.gruppoAppartenenza = gruppoAppartenenza;
	}

	public LocalDate getDataNascita() {
		return dataNascita;
	}

	public void setDataNascita(LocalDate dataNascita) {
		this.dataNascita = dataNascita;
	}

	public boolean isPreferito() {
		return isPreferito;
	}

	public void setPreferito(boolean isPreferito) {
		this.isPreferito = isPreferito;
	}

	@Override
	public int hashCode() {
		return Objects.hash(numero);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Contatto other = (Contatto) obj;
		return Objects.equals(numero, other.numero);
	}
}
