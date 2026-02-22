package com.spring.azienda.entity;

import jakarta.persistence.*;

@Entity
public class PostoAuto {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;

	private String posizione;

	@OneToOne
	private Dipendente dipendente;

	public PostoAuto() {
	}

	public PostoAuto(String posizione, Dipendente dipendente) {
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

	public Dipendente getDipendente() {
		return dipendente;
	}

	public void setDipendente(Dipendente dipendente) {
		this.dipendente = dipendente;
	}
}
