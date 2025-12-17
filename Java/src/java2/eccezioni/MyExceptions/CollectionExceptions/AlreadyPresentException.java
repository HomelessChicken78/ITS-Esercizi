package java2.eccezioni.MyExceptions.CollectionExceptions;

public class AlreadyPresentException extends CollectionException {

	public AlreadyPresentException() {
	}

	public AlreadyPresentException(String message) {
		super(message);
	}

	public AlreadyPresentException(Throwable cause) {
		super(cause);
	}

	public AlreadyPresentException(String message, Throwable cause) {
		super(message, cause);
	}

	public AlreadyPresentException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
