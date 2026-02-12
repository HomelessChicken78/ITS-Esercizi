package com.spring.java.dto;

import java.util.Objects;

public class ProdottoNoIdDTO {
	private String marca, modello, descrizione;
	private double prezzoConsigliato, prezzoMassimo;
	private int quantita;
	private String categoria;

	public ProdottoNoIdDTO() {}

	public ProdottoNoIdDTO(String marca, String modello, String descrizione, double prezzoConsigliato,
			double prezzoMassimo, int quantita, String categoria) {
		this.marca = marca;
		this.modello = modello;
		this.descrizione = descrizione;
		this.prezzoConsigliato = prezzoConsigliato;
		this.prezzoMassimo = prezzoMassimo;
		this.quantita = quantita;
		this.categoria = categoria;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModello() {
		return modello;
	}

	public void setModello(String modello) {
		this.modello = modello;
	}

	public String getDescrizione() {
		return descrizione;
	}

	public void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}

	public double getPrezzoConsigliato() {
		return prezzoConsigliato;
	}

	public void setPrezzoConsigliato(double prezzoConsigliato) {
		this.prezzoConsigliato = prezzoConsigliato;
	}

	public double getPrezzoMassimo() {
		return prezzoMassimo;
	}

	public void setPrezzoMassimo(double prezzoMassimo) {
		this.prezzoMassimo = prezzoMassimo;
	}

	public int getQuantita() {
		return quantita;
	}

	public void setQuantita(int quantita) {
		this.quantita = quantita;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	@Override
	public int hashCode() {
		return Objects.hash(marca);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ProdottoNoIdDTO other = (ProdottoNoIdDTO) obj;
		return marca == other.marca;
	}

	@Override
	public String toString() {
		return marca + " " + modello + ", descrizione=" + descrizione + ", prezzoConsigliato="
				+ prezzoConsigliato + ", prezzoMassimo=" + prezzoMassimo + ", quantita=" + quantita + ", categoria="
				+ categoria;
	}	
}
