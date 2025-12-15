package java2.eccezioni.MyExceptions;

public class ValueNotAllowedException extends RuntimeException {

	public ValueNotAllowedException() {
	}

	public ValueNotAllowedException(String message) {
		super(message);
	}

	public ValueNotAllowedException(Throwable cause) {
		super(cause);
	}

	public ValueNotAllowedException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValueNotAllowedException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
