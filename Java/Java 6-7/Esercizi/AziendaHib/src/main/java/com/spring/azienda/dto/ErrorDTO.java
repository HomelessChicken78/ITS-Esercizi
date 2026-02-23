package com.spring.azienda.dto;

import java.time.Instant;

public class ErrorDTO {
	private int statusCode;
	private String message;
	private Instant timestamp;

	public ErrorDTO() {
	}

	public ErrorDTO(String message) {
		this.statusCode = 400;
		this.message = message;
		this.timestamp = Instant.now();
	}

	public ErrorDTO(int statusCode, String message) {
		this.statusCode = statusCode;
		this.message = message;
		this.timestamp = Instant.now();
	}

	public ErrorDTO(int statusCode, String message, Instant timestamp) {
		this.statusCode = statusCode;
		this.message = message;
		this.timestamp = timestamp;
	}

	public int getStatusCode() {
		return statusCode;
	}

	public void setStatusCode(int statusCode) {
		this.statusCode = statusCode;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public Instant getTimestamp() {
		return timestamp;
	}

	public void setTimestamp(Instant timestamp) {
		this.timestamp = timestamp;
	}
}
