package com.spring.banca.dto;

import lombok.Data;

@Data
public class RegistraUtenteDTO {
	private String nome, cognome, mail, telefono;
	private String via;
	private int cap;
	private String citta, provincia;
}
