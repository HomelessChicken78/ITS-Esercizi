package java2.eccezioni.MyExceptions;

public class ValueTooSmallException extends ValueNotAllowedException {

	public ValueTooSmallException() {
	}

	public ValueTooSmallException(String message) {
		super(message);
	}

	public ValueTooSmallException(Throwable cause) {
		super(cause);
	}

	public ValueTooSmallException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValueTooSmallException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
