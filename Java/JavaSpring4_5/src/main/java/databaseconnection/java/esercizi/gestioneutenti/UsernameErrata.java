package databaseconnection.java.esercizi.gestioneutenti;

public class UsernameErrata extends Exception {
	public UsernameErrata() {
	}

	public UsernameErrata(String message) {
		super(message);
	}

	public UsernameErrata(Throwable cause) {
		super(cause);
	}

	public UsernameErrata(String message, Throwable cause) {
		super(message, cause);
	}

	public UsernameErrata(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}
}
