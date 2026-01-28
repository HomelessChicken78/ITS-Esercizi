package java3.testing.esercizi.biblioteca;

public class PubblicazioneGiaPresente extends Exception {

	public PubblicazioneGiaPresente() {
	}

	public PubblicazioneGiaPresente(String message) {
		super(message);
	}

	public PubblicazioneGiaPresente(Throwable cause) {
		super(cause);
	}

	public PubblicazioneGiaPresente(String message, Throwable cause) {
		super(message, cause);
	}

	public PubblicazioneGiaPresente(String message, Throwable cause, boolean enableSuppression,
			boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}
}