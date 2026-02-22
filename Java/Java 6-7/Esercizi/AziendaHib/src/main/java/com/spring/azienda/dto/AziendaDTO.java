package com.spring.azienda.dto;

import java.util.Collection;
import java.util.HashSet;

public class AziendaDTO {
	private int id;

	private String intestazione;
	private double capitaleSociale;

	private Collection<DipendenteDTO> dipendenti = new HashSet<>();

	public AziendaDTO() {
	}

	public AziendaDTO(String intestazione, double capitaleSociale) {
		this.intestazione = intestazione;
		this.capitaleSociale = capitaleSociale;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getIntestazione() {
		return intestazione;
	}

	public void setIntestazione(String intestazione) {
		this.intestazione = intestazione;
	}

	public double getCapitaleSociale() {
		return capitaleSociale;
	}

	public void setCapitaleSociale(double capitaleSociale) {
		this.capitaleSociale = capitaleSociale;
	}

	public Collection<DipendenteDTO> getDipendenti() {
		return new HashSet<>(dipendenti);
	}

	public void setDipendenti(Collection<DipendenteDTO> dipendenti) {
		this.dipendenti = new HashSet<>(dipendenti);
	}
}
