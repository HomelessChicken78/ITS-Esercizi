package com.spring.azienda.dto;

import java.util.Objects;

public class DipendenteDTO {
	private String matricola;

	private String nome, cognome;
	private double salario;

	public DipendenteDTO() {
	}

	public DipendenteDTO(String matricola, String nome, String cognome, double salario) {
		super();
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.salario = salario;
	}

	public String getMatricola() {
		return matricola;
	}

	public void setMatricola(String matricola) {
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

	public double getSalario() {
		return salario;
	}

	public void setSalario(double salario) {
		this.salario = salario;
	}

	@Override
	public int hashCode() {
		return Objects.hash(matricola);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		DipendenteDTO other = (DipendenteDTO) obj;
		return Objects.equals(matricola, other.matricola);
	}
}
