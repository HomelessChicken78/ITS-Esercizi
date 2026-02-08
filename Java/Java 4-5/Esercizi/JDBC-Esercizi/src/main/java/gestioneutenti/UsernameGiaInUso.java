package gestioneutenti;

public class UsernameGiaInUso extends Exception {
	public UsernameGiaInUso() {
	}

	public UsernameGiaInUso(String message) {
		super(message);
	}

	public UsernameGiaInUso(Throwable cause) {
		super(cause);
	}

	public UsernameGiaInUso(String message, Throwable cause) {
		super(message, cause);
	}

	public UsernameGiaInUso(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}
}
