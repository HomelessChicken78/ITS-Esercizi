package java2.eccezioni.MyExceptions.CollectionExceptions;

public class CollectionSizeException extends CollectionException {

	public CollectionSizeException() {
	}

	public CollectionSizeException(String message) {
		super(message);
	}

	public CollectionSizeException(Throwable cause) {
		super(cause);
	}

	public CollectionSizeException(String message, Throwable cause) {
		super(message, cause);
	}

	public CollectionSizeException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
