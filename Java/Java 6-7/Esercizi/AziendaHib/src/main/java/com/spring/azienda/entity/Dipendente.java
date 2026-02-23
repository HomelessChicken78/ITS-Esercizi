package com.spring.azienda.entity;

import java.util.Objects;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.OneToOne;

@Entity
public class Dipendente {
	@Id
	private String matricola;

	private String nome, cognome;
	private double salario;

	@OneToOne(cascade = CascadeType.PERSIST)
	private PostoAuto postoAuto;

	public Dipendente() {
	}

	public Dipendente(String matricola, String nome, String cognome, double salario, PostoAuto postoAuto) {
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.salario = salario;
		this.postoAuto = postoAuto;
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

	public PostoAuto getPostoAuto() {
		return postoAuto;
	}

	public void setPostoAuto(PostoAuto postoAuto) {
		this.postoAuto = postoAuto;
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
		Dipendente other = (Dipendente) obj;
		return Objects.equals(matricola, other.matricola);
	}
}
