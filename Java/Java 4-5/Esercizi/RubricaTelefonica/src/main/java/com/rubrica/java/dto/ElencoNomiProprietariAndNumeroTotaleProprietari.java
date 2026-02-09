package com.rubrica.java.dto;

import java.util.ArrayList;
import java.util.List;

public class ElencoNomiProprietariAndNumeroTotaleProprietari {
	List<String> nomiProprietari;
	private int numTotale;

	public ElencoNomiProprietariAndNumeroTotaleProprietari() {}

	public ElencoNomiProprietariAndNumeroTotaleProprietari(List<String> nomiProprietari, int numTotale) {
		this.nomiProprietari = new ArrayList<>(nomiProprietari);
		this.numTotale = numTotale;
	}

	public List<String> getNomiProprietari() {
		return nomiProprietari;
	}

	public void setNomiProprietari(List<String> nomiProprietari) {
		this.nomiProprietari = nomiProprietari;
	}

	public int getNumTotale() {
		return numTotale;
	}

	public void setNumTotale(int numTotale) {
		this.numTotale = numTotale;
	}
}
