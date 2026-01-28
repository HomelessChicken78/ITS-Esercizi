package java2.collezioni.esercizi.simulazionetabella;

public class TabellaInesistenteException extends Exception {

	public TabellaInesistenteException() {
	}

	public TabellaInesistenteException(String message) {
		super(message);
	}

	public TabellaInesistenteException(Throwable cause) {
		super(cause);
	}

	public TabellaInesistenteException(String message, Throwable cause) {
		super(message, cause);
	}

	public TabellaInesistenteException(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

}
