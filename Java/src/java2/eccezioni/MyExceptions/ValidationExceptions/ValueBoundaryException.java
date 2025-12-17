package java2.eccezioni.MyExceptions.ValidationExceptions;

public abstract class ValueBoundaryException extends ValidationException {

	public ValueBoundaryException() {
	}

	public ValueBoundaryException(String message) {
		super(message);
	}

	public ValueBoundaryException(Throwable cause) {
		super(cause);
	}

	public ValueBoundaryException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValueBoundaryException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
