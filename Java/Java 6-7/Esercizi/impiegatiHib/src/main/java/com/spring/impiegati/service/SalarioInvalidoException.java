package com.spring.impiegati.service;

public class SalarioInvalidoException extends RuntimeException {
	public SalarioInvalidoException() {
		super();
	}

	public SalarioInvalidoException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

	public SalarioInvalidoException(String message, Throwable cause) {
		super(message, cause);
	}

	public SalarioInvalidoException(String message) {
		super(message);
	}

	public SalarioInvalidoException(Throwable cause) {
		super(cause);
	}
}
