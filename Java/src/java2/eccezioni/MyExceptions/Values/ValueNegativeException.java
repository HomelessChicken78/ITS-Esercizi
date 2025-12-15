package java2.eccezioni.MyExceptions.Values;

public class ValueNegativeException extends ValueTooSmallException {

	public ValueNegativeException() {
	}

	public ValueNegativeException(String message) {
		super(message);
	}

	public ValueNegativeException(Throwable cause) {
		super(cause);
	}

	public ValueNegativeException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValueNegativeException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
