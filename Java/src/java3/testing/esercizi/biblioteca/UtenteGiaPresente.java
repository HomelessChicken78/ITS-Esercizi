package java3.testing.esercizi.biblioteca;

public class UtenteGiaPresente extends Exception {

	public UtenteGiaPresente() {
	}

	public UtenteGiaPresente(String message) {
		super(message);
	}

	public UtenteGiaPresente(Throwable cause) {
		super(cause);
	}

	public UtenteGiaPresente(String message, Throwable cause) {
		super(message, cause);
	}

	public UtenteGiaPresente(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}
}
