package java2.eccezioni.MyExceptions.Values;

public class ValueOutOfRangeException extends ValueNotAllowedException {

	public ValueOutOfRangeException() {
	}

	public ValueOutOfRangeException(String message) {
		super(message);
	}

	public ValueOutOfRangeException(Throwable cause) {
		super(cause);
	}

	public ValueOutOfRangeException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValueOutOfRangeException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
