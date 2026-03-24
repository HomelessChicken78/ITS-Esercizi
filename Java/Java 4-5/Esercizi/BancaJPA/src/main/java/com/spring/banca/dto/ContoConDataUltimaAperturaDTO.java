package com.spring.banca.dto;

import java.time.LocalDate;

import lombok.*;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ContoConDataUltimaAperturaDTO {
	private Integer numeroConto;
	private Double saldo;
	private LocalDate dataUltimoMovimento;
}
