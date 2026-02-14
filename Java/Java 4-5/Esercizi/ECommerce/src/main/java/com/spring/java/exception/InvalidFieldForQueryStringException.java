package com.spring.java.exception;

public class InvalidFieldForQueryStringException extends RuntimeException {
	public InvalidFieldForQueryStringException() {
		super();
	}

	public InvalidFieldForQueryStringException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

	public InvalidFieldForQueryStringException(String message, Throwable cause) {
		super(message, cause);
	}

	public InvalidFieldForQueryStringException(String message) {
		super(message);
	}

	public InvalidFieldForQueryStringException(Throwable cause) {
		super(cause);
	}
}
