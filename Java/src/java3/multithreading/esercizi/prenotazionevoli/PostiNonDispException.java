package java3.multithreading.esercizi.prenotazionevoli;

import java2.eccezioni.MyExceptions.CollectionExceptions.FullCollectionException;

public class PostiNonDispException extends FullCollectionException {

	public PostiNonDispException() {
	}

	public PostiNonDispException(String message) {
		super(message);
	}

	public PostiNonDispException(Throwable cause) {
		super(cause);
	}

	public PostiNonDispException(String message, Throwable cause) {
		super(message, cause);
	}

	public PostiNonDispException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
