package java2.eccezioni.MyExceptions.ValidationExceptions;

public class ValuePositiveException extends ValueNotAllowedException {

	public ValuePositiveException() {
	}

	public ValuePositiveException(String message) {
		super(message);
	}

	public ValuePositiveException(Throwable cause) {
		super(cause);
	}

	public ValuePositiveException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValuePositiveException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
