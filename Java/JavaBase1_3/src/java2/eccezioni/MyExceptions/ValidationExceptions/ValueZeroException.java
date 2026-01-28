package java2.eccezioni.MyExceptions.ValidationExceptions;

public class ValueZeroException extends ValueNotAllowedException {

	public ValueZeroException() {
	}

	public ValueZeroException(String message) {
		super(message);
	}

	public ValueZeroException(Throwable cause) {
		super(cause);
	}

	public ValueZeroException(String message, Throwable cause) {
		super(message, cause);
	}

	public ValueZeroException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
