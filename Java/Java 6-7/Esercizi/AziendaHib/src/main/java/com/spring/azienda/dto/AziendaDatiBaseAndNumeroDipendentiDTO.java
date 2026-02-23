package com.spring.azienda.dto;

public class AziendaDatiBaseAndNumeroDipendentiDTO extends AziendaDatiBaseDTO {
	private int numeroDipendenti;

	public AziendaDatiBaseAndNumeroDipendentiDTO() {
		super();
	}

	public AziendaDatiBaseAndNumeroDipendentiDTO(String intestazione, double capitaleSociale, int numeroDipendenti) {
		super(intestazione, capitaleSociale);
		this.numeroDipendenti = numeroDipendenti;
	}

	public int getNumeroDipendenti() {
		return numeroDipendenti;
	}

	public void setNumeroDipendenti(int numeroDipendenti) {
		this.numeroDipendenti = numeroDipendenti;
	}
}
