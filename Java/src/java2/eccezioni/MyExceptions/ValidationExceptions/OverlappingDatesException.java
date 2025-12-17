package java2.eccezioni.MyExceptions.ValidationExceptions;

public class OverlappingDatesException extends DateNotAllowedException {

	public OverlappingDatesException() {
	}

	public OverlappingDatesException(String message) {
		super(message);
	}

	public OverlappingDatesException(Throwable cause) {
		super(cause);
	}

	public OverlappingDatesException(String message, Throwable cause) {
		super(message, cause);
	}

	public OverlappingDatesException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
