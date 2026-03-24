package com.spring.banca.dto;

import java.time.LocalDateTime;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ErrorDTO {
	private String message;
	private LocalDateTime timestamp;
	private Integer statusCode;
	
	public ErrorDTO(String message, Integer statusCode) {
		this.message = message;
		this.statusCode = statusCode;
		this.timestamp = LocalDateTime.now();
	}

	public ErrorDTO(String message) {
		this.message = message;
		this.statusCode = 200;
		this.timestamp = LocalDateTime.now();
	}
}