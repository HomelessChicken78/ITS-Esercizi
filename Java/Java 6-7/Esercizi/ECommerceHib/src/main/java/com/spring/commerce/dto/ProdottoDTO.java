package com.spring.commerce.dto;

import java.util.Objects;

public class ProdottoDTO {
	private int id;

	private String descrizione;
	private int quantita;
	private double prezzoUnitario;
	private int sconto;
	private String categoria;

	public ProdottoDTO() {
	}

	public ProdottoDTO(String descrizione, int quantita, double prezzoUnitario, int sconto, String categoria) {
		this.descrizione = descrizione;
		this.quantita = quantita;
		this.prezzoUnitario = prezzoUnitario;
		this.sconto = sconto;
		this.categoria = categoria;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDescrizione() {
		return descrizione;
	}

	public void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}

	public int getQuantita() {
		return quantita;
	}

	public void setQuantita(int quantita) {
		this.quantita = quantita;
	}

	public double getPrezzoUnitario() {
		return prezzoUnitario;
	}

	public void setPrezzoUnitario(double prezzoUnitario) {
		this.prezzoUnitario = prezzoUnitario;
	}

	public int getSconto() {
		return sconto;
	}

	public void setSconto(int sconto) {
		this.sconto = sconto;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ProdottoDTO other = (ProdottoDTO) obj;
		return id == other.id;
	}
}
