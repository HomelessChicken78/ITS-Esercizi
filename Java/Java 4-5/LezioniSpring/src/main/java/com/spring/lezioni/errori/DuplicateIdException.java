package com.spring.lezioni.errori;

public class DuplicateIdException extends RuntimeException {
	public DuplicateIdException() {
		super();
	}

	public DuplicateIdException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

	public DuplicateIdException(String message, Throwable cause) {
		super(message, cause);
	}

	public DuplicateIdException(String message) {
		super(message);
	}

	public DuplicateIdException(Throwable cause) {
		super(cause);
	}
}
