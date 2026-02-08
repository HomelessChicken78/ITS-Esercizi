package gestioneutenti;

public class CredenzialiErrate extends Exception {
	public CredenzialiErrate() {
	}

	public CredenzialiErrate(String message) {
		super(message);
	}

	public CredenzialiErrate(Throwable cause) {
		super(cause);
	}

	public CredenzialiErrate(String message, Throwable cause) {
		super(message, cause);
	}

	public CredenzialiErrate(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}
}
