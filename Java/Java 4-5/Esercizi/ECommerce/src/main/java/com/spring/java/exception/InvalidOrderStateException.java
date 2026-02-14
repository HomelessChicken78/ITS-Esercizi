package com.spring.java.exception;

public class InvalidOrderStateException extends ConflictException {
	public InvalidOrderStateException() {
	}

	public InvalidOrderStateException(String message) {
		super(message);
	}

	public InvalidOrderStateException(Throwable cause) {
		super(cause);
	}

	public InvalidOrderStateException(String message, Throwable cause) {
		super(message, cause);
	}

	public InvalidOrderStateException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}
}
