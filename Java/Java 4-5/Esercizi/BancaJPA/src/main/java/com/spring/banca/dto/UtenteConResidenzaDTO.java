package com.spring.banca.dto;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class UtenteConResidenzaDTO {
	private Integer idUtente;
	private String nome, cognome;
	private String cittaResidenza, provinciaResidenza;
	private Double saldoComplessivoUtente;
}
