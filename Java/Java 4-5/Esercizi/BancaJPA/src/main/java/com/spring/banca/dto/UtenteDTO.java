package com.spring.banca.dto;

import lombok.*;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class UtenteDTO {
	private Integer idUtente;
	private String nome, cognome, mail, telefono;
}
