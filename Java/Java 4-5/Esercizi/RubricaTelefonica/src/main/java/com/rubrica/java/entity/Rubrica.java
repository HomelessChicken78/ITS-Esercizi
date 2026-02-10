package com.rubrica.java.entity;

import java.util.ArrayList;
import java.util.List;

public class Rubrica {
	private int id;
	private String proprietario;
	private int annoCreazione;
	private List<Contatto> listaContatti = new ArrayList<>();

	public Rubrica() {}

	public Rubrica(String proprietario, int annoCreazione) {
		this.proprietario = proprietario;
		this.annoCreazione = annoCreazione;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
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

	public boolean addContatto(Contatto contatto) {
		return listaContatti.add(contatto);
	}

	public Contatto removeContatto(int idContatto) {
		for (Contatto c : listaContatti)
			if (c.getId() == idContatto) {
				listaContatti.remove(c);
				return c;
			}

		return null;
	}
}
