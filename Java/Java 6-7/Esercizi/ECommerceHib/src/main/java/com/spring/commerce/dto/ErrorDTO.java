package com.spring.commerce.dto;

import java.time.LocalDate;

public class ErrorDTO {
	private LocalDate timestamp;
	private String message;
	private int status;

	public ErrorDTO() {
	}

	public ErrorDTO(LocalDate timestamp, String message, int status) {
		this.timestamp = timestamp;
		this.message = message;
		this.status = status;
	}

	public ErrorDTO(String message, int status) {
		this.timestamp = LocalDate.now();
		this.message = message;
		this.status = status;
	}

	public ErrorDTO(String message) {
		this.timestamp = LocalDate.now();
		this.message = message;
		this.status = 400;
	}

	public LocalDate getTimestamp() {
		return timestamp;
	}

	public void setTimestamp(LocalDate timestamp) {
		this.timestamp = timestamp;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}

	public int getStatus() {
		return status;
	}

	public void setStatus(int status) {
		this.status = status;
	}
}
