package com.rubrica.java.dto;

import java.util.ArrayList;
import java.util.List;

public class RubricaDTO {
	private int id;
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	private String proprietario;
	private int annoCreazione;
	private List<ContattoDTO> listaContatti = new ArrayList<>();

	public RubricaDTO() {}

	public RubricaDTO(String proprietario, int annoCreazione) {
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

	public List<ContattoDTO> getListaContatti() {
		return new ArrayList<>(listaContatti);
	}

	public void addContattoDTO(ContattoDTO contatto) {
		listaContatti.add(contatto);
	}

	public void removeContattoDTO(ContattoDTO contatto) {
		listaContatti.remove(contatto);
	}

	public void removeContattoDTO(int index) {
		listaContatti.remove(index);
	}
}
