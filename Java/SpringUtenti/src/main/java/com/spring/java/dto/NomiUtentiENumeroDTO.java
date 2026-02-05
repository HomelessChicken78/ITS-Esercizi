package com.spring.java.dto;

import java.util.List;

public class NomiUtentiENumeroDTO {
	private List<String> nomi;
	private int numeroNomi;

	public NomiUtentiENumeroDTO(List<String> nomi, int numeroNomi) {
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
