package com.spring.impiegati.dto;

import java.time.LocalDate;

public class ImpiegatoDTO {
	private String matricola;
	private String nome, cognome;
	private double salarioMensile;
	private LocalDate dataAssunzione;

	public ImpiegatoDTO() {
	}

	public ImpiegatoDTO(String matricola, String nome, String cognome, double salarioMensile, LocalDate dataAssunzione) {
		super();
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.salarioMensile = salarioMensile;
		this.dataAssunzione = dataAssunzione;
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

	public double getSalarioMensile() {
		return salarioMensile;
	}

	public void setSalarioMensile(double salarioMensile) {
		this.salarioMensile = salarioMensile;
	}

	public LocalDate getDataAssunzione() {
		return dataAssunzione;
	}

	public void setDataAssunzione(LocalDate dataAssunzione) {
		this.dataAssunzione = dataAssunzione;
	}
}
