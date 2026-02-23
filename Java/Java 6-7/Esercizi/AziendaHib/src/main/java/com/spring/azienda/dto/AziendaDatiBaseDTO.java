package com.spring.azienda.dto;

public class AziendaDatiBaseDTO {
	private int id;

	private String intestazione;
	private double capitaleSociale;

	public AziendaDatiBaseDTO() {
	}

	public AziendaDatiBaseDTO(String intestazione, double capitaleSociale) {
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
}
