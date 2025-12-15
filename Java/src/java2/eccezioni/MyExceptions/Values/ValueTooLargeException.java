package java2.eccezioni.MyExceptions.Values;

public class ValueTooLargeException extends ValueNotAllowedException {

	public ValueTooLargeException() {
	}

	public ValueTooLargeException(String message) {
		super(message);
	}

	public ValueTooLargeException(Throwable cause) {
		super(cause);
	}

	public ValueTooLargeException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValueTooLargeException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
