package com.spring.azienda.exceptions;

public class EliminazioneNonConcessaException extends ConflictException {
	public EliminazioneNonConcessaException() {
	}

	public EliminazioneNonConcessaException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

	public EliminazioneNonConcessaException(String message, Throwable cause) {
		super(message, cause);
	}

	public EliminazioneNonConcessaException(String message) {
		super(message);
	}

	public EliminazioneNonConcessaException(Throwable cause) {
		super(cause);
	}
}
