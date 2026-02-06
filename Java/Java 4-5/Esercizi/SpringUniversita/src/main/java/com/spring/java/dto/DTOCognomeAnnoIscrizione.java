package com.spring.java.dto;

public class DTOCognomeAnnoIscrizione {
	private String cognome;
	private int annoIscrizione;

	public DTOCognomeAnnoIscrizione(String cognome, int annoIscrizione) {
		super();
		this.cognome = cognome;
		this.annoIscrizione = annoIscrizione;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public int getAnnoIscrizione() {
		return annoIscrizione;
	}

	public void setAnnoIscrizione(int annoIscrizione) {
		this.annoIscrizione = annoIscrizione;
	}
}
