package java2.eccezioni.MyExceptions.ValidationExceptions;

public class DateNotAllowedException extends ValidationException {

	public DateNotAllowedException() {
	}

	public DateNotAllowedException(String message) {
		super(message);
	}

	public DateNotAllowedException(Throwable cause) {
		super(cause);
	}

	public DateNotAllowedException(String message, Throwable cause) {
		super(message, cause);
	}

	public DateNotAllowedException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
