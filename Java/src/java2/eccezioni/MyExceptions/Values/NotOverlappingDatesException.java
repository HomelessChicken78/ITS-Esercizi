package java2.eccezioni.MyExceptions.Values;

public class NotOverlappingDatesException extends ValueNotAllowedException {

	public NotOverlappingDatesException() {
	}

	public NotOverlappingDatesException(String message) {
		super(message);
	}

	public NotOverlappingDatesException(Throwable cause) {
		super(cause);
	}
	
	public NotOverlappingDatesException(String message, Throwable cause) {
		super(message, cause);
	}

	public NotOverlappingDatesException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
