package com.spring.azienda.dto;

public class PostoAutoDTO {
	private int id;

	private String posizione;

	private String dipendente;

	public PostoAutoDTO() {
	}

	public PostoAutoDTO(String posizione, String dipendente) {
		this.posizione = posizione;
		this.dipendente = dipendente;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getPosizione() {
		return posizione;
	}

	public void setPosizione(String posizione) {
		this.posizione = posizione;
	}

	public String getDipendente() {
		return dipendente;
	}

	public void setDipendente(String dipendente) {
		this.dipendente = dipendente;
	}
}
