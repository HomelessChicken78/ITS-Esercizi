package java2.collezioni.esercizi.contest;

import java2.eccezioni.MyExceptions.AlreadyPresentException;

public class PerformerDuplicatoException extends AlreadyPresentException {

	public PerformerDuplicatoException() {
	}

	public PerformerDuplicatoException(String message) {
		super(message);
	}

	public PerformerDuplicatoException(Throwable cause) {
		super(cause);
	}

	public PerformerDuplicatoException(String message, Throwable cause) {
		super(message, cause);
	}

	public PerformerDuplicatoException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
