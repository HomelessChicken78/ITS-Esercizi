package com.spring.azienda.dto;

public class PostoAutoDTO {
	private int id;

	private String posizione;

	private DipendenteDTO dipendente;

	public PostoAutoDTO() {
	}

	public PostoAutoDTO(String posizione, DipendenteDTO dipendente) {
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

	public DipendenteDTO getDipendente() {
		return dipendente;
	}

	public void setDipendente(DipendenteDTO dipendente) {
		this.dipendente = dipendente;
	}
}
