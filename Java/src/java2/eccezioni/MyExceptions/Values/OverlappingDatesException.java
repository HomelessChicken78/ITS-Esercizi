package java2.eccezioni.MyExceptions.Values;

public class OverlappingDatesException extends ValueNotAllowedException {

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
