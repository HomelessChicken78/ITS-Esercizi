package java2.eccezioni.MyExceptions;

public class FullCollectionException extends CollectionSizeException {

	public FullCollectionException() {
	}

	public FullCollectionException(String message) {
		super(message);
	}

	public FullCollectionException(Throwable cause) {
		super(cause);
	}

	public FullCollectionException(String message, Throwable cause) {
		super(message, cause);
	}

	public FullCollectionException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
