package com.spring.lezioni.errori.dto;

public class ErrorDTO {
	private String error;

	public ErrorDTO() {}

	public String getMessage() {
		return error;
	}

	public void setMessage(String error) {
		this.error = error;
	}
}
