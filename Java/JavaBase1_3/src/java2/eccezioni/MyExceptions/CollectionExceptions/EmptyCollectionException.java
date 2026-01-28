package java2.eccezioni.MyExceptions.CollectionExceptions;

public class EmptyCollectionException extends CollectionSizeException {

	public EmptyCollectionException() {
	}

	public EmptyCollectionException(String message) {
		super(message);
	}

	public EmptyCollectionException(Throwable cause) {
		super(cause);
	}

	public EmptyCollectionException(String message, Throwable cause) {
		super(message, cause);
	}

	public EmptyCollectionException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
