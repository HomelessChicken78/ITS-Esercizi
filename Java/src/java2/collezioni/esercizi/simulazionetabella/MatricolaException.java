package java2.collezioni.esercizi.simulazionetabella;

import java2.eccezioni.MyExceptions.CollectionExceptions.DuplicateElementException;

public class MatricolaException extends DuplicateElementException {

	public MatricolaException() {
	}

	public MatricolaException(String message) {
		super(message);
	}

	public MatricolaException(Throwable cause) {
		super(cause);
	}

	public MatricolaException(String message, Throwable cause) {
		super(message, cause);
	}

	public MatricolaException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
