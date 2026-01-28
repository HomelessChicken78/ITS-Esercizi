package java3.multithreading.esercizi.bancanosync;

public class StessoContoException extends Exception {

	public StessoContoException() {
	}

	public StessoContoException(String message) {
		super(message);
	}

	public StessoContoException(Throwable cause) {
		super(cause);
	}

	public StessoContoException(String message, Throwable cause) {
		super(message, cause);
	}

	public StessoContoException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
