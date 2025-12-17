package java2.eccezioni.MyExceptions.ValidationExceptions;

public class InvalidIntervalDatesException extends DateNotAllowedException {

	public InvalidIntervalDatesException() {
	}

	public InvalidIntervalDatesException(String message) {
		super(message);
	}

	public InvalidIntervalDatesException(Throwable cause) {
		super(cause);
	}

	public InvalidIntervalDatesException(String message, Throwable cause) {
		super(message, cause);
	}

	public InvalidIntervalDatesException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
