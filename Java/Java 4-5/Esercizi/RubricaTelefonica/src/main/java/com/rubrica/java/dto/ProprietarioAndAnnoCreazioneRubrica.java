package com.rubrica.java.dto;

public class ProprietarioAndAnnoCreazioneRubrica {
	private String proprietario;
	private int annoCreazione;

	public ProprietarioAndAnnoCreazioneRubrica() {}

	public ProprietarioAndAnnoCreazioneRubrica(String proprietario, int annoCreazione) {
		super();
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
}
