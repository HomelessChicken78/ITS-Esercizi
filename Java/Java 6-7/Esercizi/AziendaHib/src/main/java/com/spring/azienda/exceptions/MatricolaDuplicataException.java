package com.spring.azienda.exceptions;

public class MatricolaDuplicataException extends ConflictException {
	public MatricolaDuplicataException() {
	}

	public MatricolaDuplicataException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

	public MatricolaDuplicataException(String message, Throwable cause) {
		super(message, cause);
	}

	public MatricolaDuplicataException(String message) {
		super(message);
	}

	public MatricolaDuplicataException(Throwable cause) {
		super(cause);
	}

}
