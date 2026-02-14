package com.spring.java.exception;

public class DuplicateIDException extends ConflictException {
	public DuplicateIDException() {
		super();
	}

	public DuplicateIDException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

	public DuplicateIDException(String message, Throwable cause) {
		super(message, cause);
	}

	public DuplicateIDException(String message) {
		super(message);
	}

	public DuplicateIDException(Throwable cause) {
		super(cause);
	}
}
