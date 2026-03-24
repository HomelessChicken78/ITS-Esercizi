package com.spring.banca.dto;

import java.util.Collection;

import lombok.*;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class UtenteConDatiSalienteDTO {
	private Integer idUtente;
	private String nome, cognome;

	private Collection<ContoConDataUltimaAperturaDTO> listaConti;
}
