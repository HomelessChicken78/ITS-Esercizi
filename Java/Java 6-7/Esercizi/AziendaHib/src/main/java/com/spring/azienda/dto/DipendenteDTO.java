package com.spring.azienda.dto;

import java.util.Objects;

public class DipendenteDTO extends NominativoDipendente {
	private String matricola;

	private double salario;
	private PostoAutoDTO postoAuto;

	public DipendenteDTO() {
	}

	public DipendenteDTO(String matricola, String nome, String cognome, double salario, PostoAutoDTO postoAuto) {
		super(nome, cognome);
		this.matricola = matricola;
		this.salario = salario;
		this.postoAuto = postoAuto;
	}

	public String getMatricola() {
		return matricola;
	}

	public void setMatricola(String matricola) {
		this.matricola = matricola;
	}

	public double getSalario() {
		return salario;
	}

	public void setSalario(double salario) {
		this.salario = salario;
	}

	public PostoAutoDTO getPostoAuto() {
		return postoAuto;
	}

	public void setPostoAuto(PostoAutoDTO postoAuto) {
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
		DipendenteDTO other = (DipendenteDTO) obj;
		return Objects.equals(matricola, other.matricola);
	}
}
