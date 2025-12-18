package java2.eccezioni.MyExceptions.CollectionExceptions;

public class DuplicateElementException extends CollectionException {

	public DuplicateElementException() {
	}

	public DuplicateElementException(String message) {
		super(message);
	}

	public DuplicateElementException(Throwable cause) {
		super(cause);
	}

	public DuplicateElementException(String message, Throwable cause) {
		super(message, cause);
	}

	public DuplicateElementException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
