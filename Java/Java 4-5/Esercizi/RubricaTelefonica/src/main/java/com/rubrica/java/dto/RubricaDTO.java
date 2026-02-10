package com.rubrica.java.dto;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class RubricaDTO {
	private int id;
	private String proprietario;
	private int annoCreazione;
	private Set<ContattoDTO> listaContatti = new HashSet<>();

	public RubricaDTO() {}

	public RubricaDTO(String proprietario, int annoCreazione) {
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

	public List<ContattoDTO> getListaContatti() {
		return new ArrayList<>(listaContatti);
	}

	public boolean addContattoDTO(ContattoDTO contatto) {
		return listaContatti.add(contatto);
	}

	public ContattoDTO removeContattoDTO(int idContatto) {
		for (ContattoDTO c : listaContatti)
			if (c.getId() == idContatto) {
				listaContatti.remove(c);
				return c;
			}

		return null;
	}
}
