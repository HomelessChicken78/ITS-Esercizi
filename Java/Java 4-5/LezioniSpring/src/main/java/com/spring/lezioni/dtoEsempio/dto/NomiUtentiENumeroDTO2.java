package com.spring.lezioni.dtoEsempio.dto;

import java.util.List;

public class NomiUtentiENumeroDTO2 {
	private List<String> nomi;
	private int numeroNomi;

	public NomiUtentiENumeroDTO2(List<String> nomi, int numeroNomi) {
		super();
		this.nomi = nomi;
		this.numeroNomi = numeroNomi;
	}

	public List<String> getNomi() {
		return nomi;
	}

	public void setNomi(List<String> nomi) {
		this.nomi = nomi;
	}

	public int getNumeroNomi() {
		return numeroNomi;
	}

	public void setNumeroNomi(int numeroNomi) {
		this.numeroNomi = numeroNomi;
	}
}
