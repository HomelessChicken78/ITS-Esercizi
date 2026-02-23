package com.spring.azienda.dto;

public class SpostamentoDipendente {
	private DipendenteDTO dipendente;
	private AziendaDTO da;
	private AziendaDTO a;

	public SpostamentoDipendente() {
	}

	public SpostamentoDipendente(DipendenteDTO dipendente, AziendaDTO da, AziendaDTO a) {
		this.dipendente = dipendente;
		this.da = da;
		this.a = a;
	}

	public DipendenteDTO getDipendente() {
		return dipendente;
	}

	public void setDipendente(DipendenteDTO dipendente) {
		this.dipendente = dipendente;
	}

	public AziendaDTO getDa() {
		return da;
	}

	public void setDa(AziendaDTO da) {
		this.da = da;
	}

	public AziendaDTO getA() {
		return a;
	}

	public void setA(AziendaDTO a) {
		this.a = a;
	}
}
