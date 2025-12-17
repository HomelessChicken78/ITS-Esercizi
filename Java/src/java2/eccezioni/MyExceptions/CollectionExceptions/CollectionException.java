package java2.eccezioni.MyExceptions.CollectionExceptions;

import java2.eccezioni.MyExceptions.CustomException;

public class CollectionException extends CustomException {

	public CollectionException() {
	}

	public CollectionException(String message) {
		super(message);
	}

	public CollectionException(Throwable cause) {
		super(cause);
	}

	public CollectionException(String message, Throwable cause) {
		super(message, cause);
	}

	public CollectionException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
