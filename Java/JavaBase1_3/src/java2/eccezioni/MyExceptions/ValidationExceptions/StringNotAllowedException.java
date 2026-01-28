package java2.eccezioni.MyExceptions.ValidationExceptions;

public class StringNotAllowedException extends ValidationException {

	public StringNotAllowedException() {
	}

	public StringNotAllowedException(String message) {
		super(message);
	}

	public StringNotAllowedException(Throwable cause) {
		super(cause);
	}

	public StringNotAllowedException(String message, Throwable cause) {
		super(message, cause);
	}

	public StringNotAllowedException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
