package java2.eccezioni.MyExceptions;

public class AlreadyPresentException extends Exception {

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
