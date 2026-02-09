package com.rubrica.java.dto;

public class ProprietarioAndNumeroContatti {
	private String proprietario;
	private int numeroContatti;

	public ProprietarioAndNumeroContatti() {}

	public ProprietarioAndNumeroContatti(String proprietario, int numeroContatti) {
		this.proprietario = proprietario;
		this.numeroContatti = numeroContatti;
	}

	public String getProprietario() {
		return proprietario;
	}

	public void setProprietario(String proprietario) {
		this.proprietario = proprietario;
	}

	public int getNumeroContatti() {
		return numeroContatti;
	}

	public void setNumeroContatti(int numeroContatti) {
		this.numeroContatti = numeroContatti;
	}
}
