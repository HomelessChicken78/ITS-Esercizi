package com.spring.catalogo.entity;

import jakarta.persistence.*;

@Entity
public class Prodotto {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;
	private String nome;
	private double prezzoUnitario;
	private int quantitaDisponibile;
	private String categoria;

	@Version
	private int version;

	public Prodotto() {
	}

	public Prodotto(String nome, double prezzoUnitario, int quantitaDisponibile, String categoria) {
		this.nome = nome;
		this.prezzoUnitario = prezzoUnitario;
		this.quantitaDisponibile = quantitaDisponibile;
		this.categoria = categoria;
	}

	public Prodotto(int id, String nome, double prezzoUnitario, int quantitaDisponibile, String categoria) {
		this(nome, prezzoUnitario, quantitaDisponibile, categoria);
		this.id = id;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getPrezzoUnitario() {
		return prezzoUnitario;
	}

	public void setPrezzoUnitario(double prezzoUnitario) {
		this.prezzoUnitario = prezzoUnitario;
	}

	public int getQuantitaDisponibile() {
		return quantitaDisponibile;
	}

	public void setQuantitaDisponibile(int quantitaDisponibile) {
		this.quantitaDisponibile = quantitaDisponibile;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	public int getVersion() {
		return version;
	}

	public void setVersion(int version) {
		this.version = version;
	}
}