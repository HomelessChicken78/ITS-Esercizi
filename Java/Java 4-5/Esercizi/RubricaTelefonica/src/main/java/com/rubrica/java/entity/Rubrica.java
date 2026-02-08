package com.rubrica.java.entity;

import java.util.ArrayList;
import java.util.List;

public class Rubrica {
	private int id;
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	private String proprietario;
	private int annoCreazione;
	private List<Contatto> listaContatti = new ArrayList<>();

	public Rubrica() {}

	public Rubrica(String proprietario, int annoCreazione) {
		this.proprietario = proprietario;
		this.annoCreazione = annoCreazione;
	}

	public String getProprietario() {
		return proprietario;
	}

	public void setProprietario(String proprietario) {
		this.proprietario = proprietario;
	}

	public int getAnnoCreazione() {
		return annoCreazione;
	}

	public void setAnnoCreazione(int annoCreazione) {
		this.annoCreazione = annoCreazione;
	}

	public List<Contatto> getListaContatti() {
		return new ArrayList<>(listaContatti);
	}

	public void addContatto(Contatto contatto) {
		listaContatti.add(contatto);
	}

	public void removeContatto(Contatto contatto) {
		listaContatti.remove(contatto);
	}

	public void removeContatto(int index) {
		listaContatti.remove(index);
	}
}
