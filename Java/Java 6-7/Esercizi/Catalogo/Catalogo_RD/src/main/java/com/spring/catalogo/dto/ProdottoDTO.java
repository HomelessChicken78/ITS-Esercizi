package com.spring.catalogo.dto;


public class ProdottoDTO {
	private Integer id;
	private String nome;
	private double prezzoUnitario;
	private int quantitaDisponibile;
	private String categoria;
	private int version;

	public ProdottoDTO() {
	}

	public ProdottoDTO(String nome, double prezzoUnitario, int quantitaDisponibile, String categoria, int version) {
		this.nome = nome;
		this.prezzoUnitario = prezzoUnitario;
		this.quantitaDisponibile = quantitaDisponibile;
		this.categoria = categoria;
	}

	public ProdottoDTO(Integer id, String nome, double prezzoUnitario, int quantitaDisponibile, String categoria, int version) {
		this(nome, prezzoUnitario, quantitaDisponibile, categoria, version);
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