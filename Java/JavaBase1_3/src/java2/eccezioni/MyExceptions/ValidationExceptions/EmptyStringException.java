package java2.eccezioni.MyExceptions.ValidationExceptions;

public class EmptyStringException extends StringNotAllowedException {

	public EmptyStringException() {
	}

	public EmptyStringException(String message) {
		super(message);
	}

	public EmptyStringException(Throwable cause) {
		super(cause);
	}

	public EmptyStringException(String message, Throwable cause) {
		super(message, cause);
	}

	public EmptyStringException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
